---
title:
 - Team Gold Critical Design Review
subtitle:
 - Version &hash
author:
 - Joe
 - Maria
 - Noah
 - Josh
 - William
institute:
 - SNHU/CETA, EG-207
titlegraphic: resources/SNHU-CETA.png
theme: Madrid
navigation: frame
date: "Build Date: &date"
aspectratio: 1610
logo: resources/logo.png
fontsize: 8pt
---


# Introduction

## CDR Agenda

 - Concept of Operations (ConOps) Summary
 - Environmental Systems Description
 - Environmental Sensors
 - Requirement Compliance
 - Front Panel Display, Baseplate and Housing Design Details
 - Summary of Analyses
 - Calibration Plan
 - References/Citations
 - Next Steps


## Environmental System Description

::: columns

:::: column

### Functional Block Diagram

![Functional Block Diagram](resources/placeholder.png)

::::

:::: column

- Instrument: LabVIEW 2019 SP1
- Data Acquisition: Arduino Mega 2560
- DAC Software: Ardunio IDE 1.8.15
- Sensors:
  - Temp/RH: DHT11 Sensor
  - Visible Light: CDS55 Photoresistor
  - UV Light: 28091 UV Parallax Sensor
  - Water Collection: DGZZI Water Level Sensor Module

::::

:::


## Environmental Sensors & Interfaces

::: columns

:::: column

![DHT 11](resources/placeholder.png){ width=90 }

::::

:::: column

![CDS 55 Photoresistor](resources/placeholder.png){ width=90 }

::::

:::: column

![Parallax UV Light Sensor](resources/placeholder.png){ width=90 }

::::

:::: column

![Water Level Sensor](resources/placeholder.png){ width=90 }

::::

:::


# Reqirements

## Functional Requiremenets - Compliance

 | Reqt    | Reqt Title                   | Statement Subject                                       | Reqt Value | Performance | Margin | Notes/Basis |
 |---------|------------------------------|---------------------------------------------------------|------------|-------------|--------|-------------|
 | 3.1.1   | Vi Front Panel               |                                                         |            |             |        |             |
 | 3.1.1.1 | Sensor Read and Indications  | Numeric Indicators, "Warning" and "Alarm" LEDs          |            |             |        |             |
 | 3.1.1.2 | Senors Controls              | Provide necessary controls                              |            |             |        |             |
 | 3.1.1.3 | operation Indications        | Display current system configuration and operating mode |            |             |        |             |
 | 3.1.1.4 | Calibration Updates          |                                                         |            |             |        |             |
 | 3.1.2   | Update/Read Rate             |                                                         |            |             |        |             |
 | 3.1.3   | Warning and Alarm Indication |                                                         |            |             |        |             |
 | 3.1.3.1 | Temperature                  |                                                         |            |             |        |             |
 | 3.1.3.2 | Humidity                     |                                                         |            |             |        |             |
 | 3.1.3.3 | Visible Light                |                                                         |            |             |        |             |
 | 3.1.3.4 | UV Light                     |                                                         |            |             |        |             |
 | 3.1.3.5 | Water Level                  |                                                         |            |             |        |             |
 | 3.1.4   | Waveform Display             |                                                         |            |             |        |             |
 | 3.1.5   | Data Logging                 |                                                         |            |             |        |             |
 | 3.1.6   | Operational Mode             |                                                         |            |             |        |             |


## Front Panel Display Design (LabVIEW)

Stuff here


## Sensor Package Assembly Model

Stuff here too


## Baseplate Design Drawing

Stuff here


## Housing Design - Solid Model

Doot


## Housing Design - Drawing

Doot


## List and Summary of Analyses

Stuff


## Calibration Plan

Stuff for calibration


## References/Citations

Doot 


## Next Steps

Step


## Backup Slides

Idk, stuff
