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
fontsize: 9pt
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
 - Impact consideration and risks
   - **This has to be filled out**

**A Flow chart is needed here**


# Environmental System Description

 - Instrument: LabVIEW 2019
 - Data Acquisition: Arduino AVR (mega)
 - DAC Software: Arduino + pyplot and numpy
 - Sensors:
   - Temp/RH: DHT11
   - UV Light: TBD
   - Visible Light: TBD
   - Water Collection: TBD


# Environmental Sensors

 - Sensors:
   - Temp/RH:[Specify Model]
   - Visible Light: CDS-55
   - UV Light: Parallax 28091
   - Water Collection: TBD


- [Show picture of Temp/RH sensor along with circuit diagrams for sensor setup with your Arduino board]
- [Don’t worry about light and water sensor for PDR... we will cover that at CDR]


# Performance Requirements - Compliance

| Reqt    | Owner | Statement  | Reqt Value | Performance | Margin                      | Notes/Bias                      |
|---------|-------|------------|------------|-------------|-----------------------------|---------------------------------|
| REQ-000 | SNHU  | Have a lab | 1 lab      | a good lab  | 90% of the lab must be good | Its difficulty to quantify "good" |
| REQ-001 | ...   | ...        | ...        | ...         | ...                         | ...                             |

