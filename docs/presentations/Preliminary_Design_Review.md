---
title:
 - Team Gold Preliminary Design Review
subtitle:
 - Version &hash
author:
 - Team Gold
institute:
 - Southern New Hampshire University
description: |
    This should be filled out
theme: Madrid
navigation: frame
date: "Build Date: &date"
aspectratio: 1610
logo: resources/logo.png
fontsize: 8pt
---


# Concept of Operations (Con-Ops) Summary

 - Stakeholders
   - (Who has a stake?)
 - Users
   - Scientists and Analysts in the field.
 - Operational Description
   - The sensor should be operated indoors and may be left without supervision to collect data and store it.
 - Support Environment
   - Released under the GNUv3 license, and supported as the license describes, extending absolutely no warranty.
 - Use
   - The operator/analyst will use the sensor in the field, and collect data supervised or not.
 - Calibration
   - Calibration data is stored in the EEPROM and the sensor will not require calibration between regular uses, the sensor is not expected to require calibration often but will have a procedure to do so.


# Concept of Operations (Con-Ops) Summary Cont.

 - Impact consideration
   - Because our enviormental monitoring solution does not have the same level of quality assurance as a similar solution, over-reliance by the end user could result in uncalibrated data, unexpeced failure modes or strange untested bugs over time.
 - Risks
   - Increased risk of the system to malfunction if operation of system is prolonged without proper maintenance.
   - Airborne contaminants can cause the system to malfunction and provide inaccurate data.

**A Flow chart is needed here**


# Environmental System Description

 - Instrument: LabVIEW 2019
 - Data Acquisition: Arduino AVR (mega)
 - DAC Software: Arduino + pyplot and numpy
 - Sensors:
   - Temp/RH: DHT11
   - UV Light: TBD
   - Visible Light: Photoresitor


# Environmental Sensors

 - Sensors:
   - Temp/RH: DHT-11
   - Visible Light: CDS-55
   - UV Light: Parallax 28091

![DHT 11 Sensor](resources/dht11.png)
![Sensor Package Schematic](resources/sensor_package_schematic.png){ width=26% }


# Performance Requirements - Compliance

| Reqt    | Owner     | Title                           | Reqt Value           | Perf. | Margin          | Notes/Bias                                                        |
|---------|-----------|---------------------------------|----------------------|-------|-----------------|-------------------------------------------------------------------|
| 3.1.1   | Team Gold | Virtual Instruments Front Panel | Have                 | N/A   | All or nothing. |                                                                   |
| 3.1.2   | Team Gold | Sensor Update/Read Rate         | Demonstrate, Inspect | N/A   | All or nothing. |                                                                   |
| 3.1.3   | Team Gold | Warning and Alarm Indication    | Demonstrate, Test    | N/A   | All or nothing. | Sensor yellow and red limits and decision-making flow chart req’d |
| 3.1.4   | Team Gold | Waveform Display                | Demonstrate          | N/A   | All or nothing. |                                                                   |
| 3.1.5   |           |                                 |                      |       |                 |                                                                   |
| 3.1.6   |           |                                 |                      |       |                 |                                                                   |
| 3.2.1   |           |                                 |                      |       |                 |                                                                   |
| 3.2.2   |           |                                 |                      |       |                 |                                                                   |
| 3.2.3   |           |                                 |                      |       |                 |                                                                   |
| 3.3.1   |           |                                 |                      |       |                 |                                                                   |
| 3.3.1.1 |           |                                 |                      |       |                 |                                                                   |
| 3.3.1.2 |           |                                 |                      |       |                 |                                                                   |
| 3.3.2   |           |                                 |                      |       |                 |                                                                   |
| 3.3.3   |           |                                 |                      |       |                 |                                                                   |