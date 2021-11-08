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
theme: Ilmenau
navigation: frame
date: "Build Date: &date"
aspectratio: 1610
logo: resources/logo.png
fontsize: 8pt
section-titles: false
toc: false
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

![Functional Block Diagram](resources/placeholder.png){ width=180 }

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

### Notes

> This page still needs work.


## Environmental Sensors & Interfaces

::: columns

:::: {.column width=25%}

![DHT 11](resources/dht11.png){ width=90 }

The DHT 11 is an inexpensive  
serial type thermometer and  
hydrometer.

::::

:::: {.column width=25%}

![CDS 55 Photoresistor](resources/placeholder.png){ width=90 }

The CDS 55 is a commonly used  
visible light detecting photoresistor.

::::

:::: {.column width=25%}

![Parallax UV Light Sensor](resources/placeholder.png){ width=90 }

The parallax UV Sensor Breakout  
board is a breakout board  
used in prototypes  
to sense UV Light.

::::

:::: {.column width=25%}

![Water Level Sensor](resources/placeholder.png){ width=90 }

It get wet, idk

::::

:::

### Notes

> This page still needs work.


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

 ### Notes

> This page still needs work.


# Prototypes

## Front Panel Display Design (LabVIEW)

### Notes

> This page still needs work.


## Sensor Package Assembly Model

### Notes

> This page still needs work.


## Baseplate Design Drawing

### Notes

> This page still needs work.


## Housing Design - Solid Model

### Notes

> This page still needs work.


## Housing Design - Drawing

### Notes

> This page still needs work.


# Analyses

## List and Summary of Analyses

### Notes

> This page still needs work.


## Calibration Plan

### Notes

> This page still needs work.


# Appendix

## References/Citations

### Notes

> This page still needs work.


## Next Steps

### Notes

> This page still needs work.


# Extra Material

## Backup Slides

### Notes

> This page still needs work.
Idk, stuff
