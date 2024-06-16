#!/usr/bin/python3

import time
import datetime
import sys
#import logging 
#logging.basicConfig(level=logging.DEBUG) 


from pymlab import config
import gpsd

import math


# Vygenerovano z Chat GPT-4
def barometric_height(P, P0=101325, T0=288.15, L=0.0065, R=8.31447, g=9.80665, M=0.0289644):
    # P: měřený tlak v Pa
    # P0: standardní tlak při hladině moře v Pa
    # T0: standardní teplota při hladině moře v K
    # L: teplotní gradient v K/m
    # R: univerzální plynová konstanta v J/(mol·K)
    # g: gravitační zrychlení v m/s²
    # M: molární hmotnost suchého vzduchu v kg/mol
    
    exponent = (R * L) / (g * M)
    height = (T0 / L) * (1 - (P / P0) ** exponent)
    return height



#### Script Arguments ###############################################

if len(sys.argv) not in (2, 3):
    sys.stderr.write("Invalid number of arguments.\n")
    sys.stderr.write("Usage: %s #I2CPORT\n" % (sys.argv[0], ))
    sys.exit(1)

port = eval(sys.argv[1])


#### Sensor Configuration ###########################################

cfglist=[
    config.Config(
        i2c = {
            "port": port,
        },

        bus = [{
                "name": "altimet",
                "type": "altimet01" ,
                }],
    )
]

try:
    cfg = cfglist[0]
except IndexError:
    sys.stdout.write("Invalid configuration number.")
    sys.exit(1)

while 1:
    try:
        # Connect to the GPS daemon
        gpsd.connect()
        cfg.initialize()

        gauge = cfg.get_device("altimet")
        time.sleep(0.5)

        #### Data Logging ###################################################

        sys.stdout.write(" data acquisition system started \n")

        n = 0
        try:
            filename = "log/TV_log_{}_UTC.csv".format(datetime.datetime.utcnow().strftime("%Y-%m-%d_%H-%M-%S"))
            with open(filename, "a") as f:
                f.write("Index, UTC_time, BAR_temperature, BAR_pressure, GPS_fix_mode, GPS_latitude, GPS_longitude, GPS_speed, GPS_heading, GPS_alt, GPS_time, BAR_alt\n")
                f.flush()
                i = 0
                while True:
                    n += 1
                    
                    # Get the current UTC time
                    utc_time = datetime.datetime.utcnow()
                    mode = 0
                    lat = 0
                    lon = 0
                    alt = 0
                    speed = 0
                    heading = 0
                    alt_bar = 0
                    gps_time = 0


                    (t1, p1) = gauge.get_tp()
                    alt_bar = barometric_height(p1)

                    # Get the current GPS data
                    packet = gpsd.get_current()
                    print(packet)

                    if packet.mode >= 2:
                        mode = packet.mode
                        lat = packet.lat
                        lon = packet.lon
                        alt = packet.alt
                        speed = packet.speed()
                        heading = packet.track
                        gps_time = packet.time
                    else:
                        print("NO GPS FIX ...", packet.mode)

                    #print(alt_bar)
                    #print(speed)

                    print("Temp: {0:.2f},\t Pres: {1:.2f},\t GPS alt: {2:.2f},\t Bar alt: {3:.2f},\t GPS spd: {4:.2f}\n".format(t1, p1, alt, alt_bar, speed))
                    f.write(','.join([str(x) for x in [n, utc_time.timestamp(), t1, p1, mode, lat, lon, speed, heading, alt, gps_time, alt_bar]])+"\n")
                    i += 1
                    if i > 10:
                        i = 0
                        f.flush()
                    time.sleep(0.5)

        except KeyboardInterrupt:
            sys.stdout.write("\r\n")
            sys.exit(0)
            #f.close()



    except Exception as e:
        print(e)
        sys.stdout.write("Initialization failed. Retrying.\n")
        time.sleep(1)