---
title:
 - Team Gold Preliminary Design Review
subtitle:
 - Version &hash
author:
 - Joe
 - Maria
 - Noah
 - Josh
 - William
institute:
 - Southern New Hampshire University
description: |
    This should be filled out...
theme: Madrid
navigation: frame
date: "Build Date: &date"
aspectratio: 1610
logo: resources/logo.png
fontsize: 8pt
---


# PDR Agenda

 - Con-Ops Summary
 - Environmental System Description
 - Enviornmental Sensors
 - Performance Requirements/Compliance
  - Functional
  - Performance
  - Verification
 - Baseplate/Housing Design Concepts
 - Next Steps


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

![Con Ops Flow Chart (Arduino)](resources/PDR_Flowchart_Arduino.png){ width=22%} ![Con Ops Flow Chart (Labview)](resources/PDR_Flowchart_LabView.png){ width=25% }


# Environmental System Description

 - Instrument: LabVIEW 2019
 - Data Acquisition: Arduino AVR (mega)
 - DAC Software: Arduino + pyplot and numpy
 - Sensors:
   - Temp/RH: DHT11
   - UV Light: TBD
   - Visible Light: Photoresistor


# Environmental Sensors

 - Sensors:
   - Temp/RH: DHT-11
   - Visible Light: CDS-55
   - UV Light: Parallax 28091

![DHT 11 Sensor](resources/dht11.png)
![Sensor Package Schematic](resources/sensor_package_schematic.png){ width=26% }


# Performance Requirements - Compliance

| Reqt  | Owner     | Title                           | Reqt Value           | Perf.           | Margin | Notes/Bias                                                        |
|-------|-----------|---------------------------------|----------------------|-----------------|--------|-------------------------------------------------------------------|
| 3.1.1 | Team Gold | Virtual Instruments Front Panel | Demonstrate, Inspect | Complies        |        |                                                                   |
| 3.1.2 | Team Gold | Sensor Update/Read Rate         | Demonstrate, Inspect | Inturrupt Based | ISR    |                                                                   |
| 3.1.3 | Team Gold | Warning and Alarm Indication    | Demonstrate, Test    | Complies        |        | Sensor yellow and red limits and decision-making flow chart req’d |
| 3.1.4 | Team Gold | Waveform Display                | Demonstrate          | Complies        |        |                                                                   |
| 3.1.5 | Team Gold | Data Logging                    | Demonstrate, Inspect | Complies        |        | Data file to be provided in ADP                                   |
| 3.1.6 | Team Gold | Operational Modes               | Demonstrate          | Complies        |        |                                                                   |
| 3.2.1 | Team Gold | Sensor Accuracy                 | Validation           | Characterized   |        | Standard to be used for accuracy determination                    |
| 3.2.2 | Team Gold | Sensor Percision                | Analysis, Validation | Characterized   |        | Standard deviation analysis req’d                                 |
| 3.2.3 | Team Gold | Calibration or Diagnostics      | Demonstration        | Built in        |        |                                                                   |


# Performance Requirements - Compliance Cont.

| Reqt    | Owner     | Title                    | Reqt Value                | Perf.           | Margin    | Notes/Bias                                                            |
|---------|-----------|--------------------------|---------------------------|-----------------|-----------|-----------------------------------------------------------------------|
| 3.3.1   | Team Gold | Mounting                 | Analysis, Demonstration   | Complies        |           |                                                                       |
| 3.3.1.1 | Team Gold | Baseplate Bottom Surface | Demonstration             | Complies        | Flush     |                                                                       |
| 3.3.1.2 | Team Gold | Housing to Baseplate     | Demonstration             | Complies        | Flush     |                                                                       |
| 3.3.2   | Team Gold | Electrical               | Validation, Demonstration | Complies        | Proto     | System Electrical Circuit Diagram req’d (including Arduino functions) |
| 3.3.3   | Team Gold | Data Power and Access    | Demonstration             | Complies        | TTY       |                                                                       |
| 3.4.1   | Team Gold | Housing                  | Validation, Demonstration | Complies        |           | *STL file and outline drawing required for fabrication                |
| 3.4.2   | Team Gold | Baseplate                | Validation                | Complies        |           |                                                                       |
| 3.4.3   | Team Gold | Electrical               | Validation                | Complies        |           |                                                                       |
| 3.4.4   | Team Gold | Hardware                 | Validation, Inspection    | Complies        | Collected |                                                                       |
| 3.5.1   | Team Gold | Team Structure           | Demonstration             | Does Not Comply |           |                                                                       |


# Performance Requirements - Compliance Cont.

| Reqt    | Owner     | Title                     | Reqt Value                | Perf.        | Margin    | Notes/Bias                                                           |
|---------|-----------|---------------------------|---------------------------|--------------|-----------|----------------------------------------------------------------------|
| 3.5.2   | Team Gold | Team Communications       | Demonstration, Inspection | Complies[^1] |           | Weekly email status reports                                          |
| 3.5.3   | Team Gold | PDR and CDR Presentations | Demonstration             | Complies     | Automatic | Presentation templates provided, reviewed class before presentations |
| 3.5.4.1 | Team Gold | System Fabrication        | Demonstration, Inspection | Complies     |           | Baseplate part file/fab drawing and cover STL file/outline drawing   |
| 3.5.4.2 | Team Gold | System Demonstration      | Demonstration             | Complies     |           | Instructor executes final verification activity                      |
| 3.5.5   | Team Gold | System ADP                | Inspection                | Complies     |           | ZIP file of all native files                                         |

[^1]: See our [discord](https://discord.gg/gQ547MBvgA).


# Verification Requirements

| Reqt  | Title                   | Method | Notes/Bias |
|-------|-------------------------|--------|------------|
| 3.1   | Functional Requirements |        |            |
| 3.1.1 | FILL ME OUT...          |        |            |


# Concepts/RC0

## Base Plate

![Baseplate Drawing](resources/BasePlate.png)

The base plate is ready to machine and has its drawings written up.


# Concepts/RC0 Cont.

## Shell

![Shell 3D Render](resources/ShellRender.png)

The Upper shell contains all the mounting for each sensor save for the light sensor, witch has its own, actuated housing.


# Concepts/RC0 Cont.

## LabView

FILL THIS OUT


# Next Steps[^2]

 - Complete RC1 manufacturing on plastic cover
 - Complete prototyping of light sensor housing
 - Machine Baseplate
 - Construct/Finalize VI

[^2]: Next steps coppied from kaban, see cards for latest status: [Link](https://github.com/KenwoodFox/EG-207-CCEMS/projects/1)
