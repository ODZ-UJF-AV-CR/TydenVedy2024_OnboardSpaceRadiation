# [Týden vědy na Jaderce 2024](https://tydenvedy.fjfi.cvut.cz/)
# Radiation Exposure from Cosmic Rays on Aircraft

**Mentor:** Ing. Ondřej Ploc, Ph.D. ([ODZ ÚJF AV ČR](https://www.ujf.cas.cz/cs/oddeleni/oddeleni-dozimetrie-zareni/))

![EOSR2791](https://github.com/ODZ-UJF-AV-CR/TydenVedy2024_OnboardSpaceRadiation/assets/5196729/b872b631-2bc0-4136-8cd6-d5eab8463123)


## Project Overview

How is [cosmic radiation](https://en.wikipedia.org/wiki/Cosmic_ray) detected on aircraft? What is the relationship between radiation intensity, altitude, and geographical location? How is the radiation exposure of aircraft crews evaluated? During this mini-project, we will attempt to answer these questions and more. If weather conditions permit, the project will include a measurement flight with a radiation detector reaching an altitude of 4000 meters.

### Instrumentation
Several instruments were onboard to measure cosmic radiation:

- 2x [AIRDOS04](https://docs.dos.ust.cz/airdos/AIRDOS04)
- 3x [LABDOS01](https://docs.dos.ust.cz/labdos/LABDOS01)
- 2x RT Particle Detector
- 1x (another detector)
- 1x Barometer with GPS

#### AIRDOS04

The [AIRDOS04](https://docs.dos.ust.cz/airdos/AIRDOS04) is a dosimeter specifically designed for measuring ionizing radiation in aviation environments. This device is tailored to monitor radiation levels encountered during flights at high altitudes, providing essential data for assessing the exposure of both passengers and crew. The AIRDOS04 is capable of detecting various forms of ionizing radiation, including gamma rays, and is built to operate reliably under the conditions found in aircraft. Its measurements help in understanding the radiation environment at different flight levels and can be used to evaluate the potential health risks associated with prolonged exposure to cosmic radiation during flights.

### LABDOS01

[LABDOS01](https://docs.dos.ust.cz/labdos/LABDOS01) is a versatile dosimeter used for the precise measurement of ionizing radiation. While it is often used in laboratory settings, its robust design makes it suitable for field use, including on aircraft. During the flight, LABDOS01 units were used to gather additional data alongside the AIRDOS04 devices.

### RT

### Another detector

### Barometer with GPS

The barometric pressure was measured using the [MLAB I2C sensor ALTIMET01](https://www.mlab.cz/module/ALTIMET01). This sensor is designed to accurately measure atmospheric pressure, which can be used to determine altitude. The ALTIMET01A provides high-resolution pressure readings, making it suitable for applications requiring precise altitude calculations, such as aviation.

In addition to the barometric sensor, the flight data included positional information provided by the [MLAB GPS sensor GPS02B](https://www.mlab.cz/module/GPS02). This GPS module offers accurate geographic coordinates, including latitude, longitude, and altitude, which are essential for tracking the flight path and correlating with the barometric altitude measurements. The GPS02B ensures that the positional data is accurate and reliable, supporting comprehensive analysis of the radiation measurements in relation to the aircraft's altitude and location.

The data from the barometric sensor ALTIMET01A and the GPS module GPS02B were logged using a computer with Python [script](/sw/altimet_gps_logger.py), using [PyMLAB](https://github.com/MLAB-project/pymlab) python library.

### Objectives

- To understand the detection methods of cosmic radiation on aircraft.
- To analyze the variation of radiation intensity with altitude and geographical location.
- To assess the radiation exposure of aircraft crews using collected data.


### Flight details
This measurement flight was conducted on June 16, 2024, 14:25:50 CEST (12:25:50 UTC; takeoff-time), from the [Příbram Airport](https://www.letiste-pribram.cz/). Dlouhá lhota, near to Příbram city. This flight resembled those typically used for skydiving jumps. The aircraft ascended to an altitude of approximately 4000 meters, providing an ideal environment for detecting cosmic radiation.

### Flight Altitude Profile

The graph below illustrates the altitude profile of the flight, showcasing data from both barometric (BAR) and GPS measurements. The ascent and descent phases are clearly marked, with a peak altitude of around 4000 meters.


<p align="center">
  <img src="/data/ALTIMET01_GPS02/mapa_3d.png" alt="První obrázek" width="48%">
  <img src="/data/ALTIMET01_GPS02/trajectory_over_map.png" alt="Druhý obrázek" width="48%">
</p>

![obrazek](https://github.com/ODZ-UJF-AV-CR/TydenVedy2024_OnboardSpaceRadiation/assets/5196729/ae842b6e-afdc-411a-9d97-bd838b8f65de)
