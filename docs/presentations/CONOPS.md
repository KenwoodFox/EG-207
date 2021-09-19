---
title:
 - Team Gold CONOPS
subtitle:
 - Version &hash
author:
 - Team Gold
institute:
 - Southern New Hampshire University
description: |
    A CONOPS
    (Concept of Operations)
    For Team Gold's Team Project.
theme: Madrid
navigation: frame
date: "Build Date: &date"
aspectratio: 1610
logo: resources/logo.png
---


# System Description

Our sensor package consisting of an:  

 - Arduino Mega 2560 (AVR) with hardware sensors
 - A student Laptop Running LabView


# Physical Environment

The Sensor package will be used in an indoor environment  
and will be subject to changes in temperature, humidity,  
UV light intensity, visible light exposure, and water collection/rate.


# Support Environment

All resources used to build our sensor and sensor package  
will be released at the end of the course under GNUv3  
or similar.


# Operating Modes

The sensor package should operate in the following modes:  

 - A standard mode, where the sensor data is displayed normally and graphed/logged.
 - A calibration/debug mode where the sensors on board can be characterized, or calibrated
 - A safe mode, or safe operation flag where if an error or other circumstance arises, the sensor package makes itself 'safe' and in a known state.


# Use

The Sensor package should capable of operating 24/7 in normal conditions  
but during testing it should be expected to operate 1.5 hours at a time  
with frequent power cycling, re-connections and enable/disable states.


# Impact Considerations

Because our enviormental monitoring solution does not have the rigourous  
testing of other similar products, its over-reliance by an end user may  
produce undiscovered bugs or issues, that may lead to bad results, or  
inaccurate data over time.


# Risks and Potential Issues
 
 - Increased risk of the system to malfunction if operation of system is prolonged without proper maintenance
 - Airborne contaminants can cause the system to malfunction and provide inaccurate data
