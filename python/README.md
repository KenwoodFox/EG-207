Gold Standard
=============

# Intro
Gold Standard is a data characterization program  
writen by Team Gold, for use with the EG-207  
lab1 and lab2.

# Usage

## Plot data
```
$ python goldstandard --port /dev/ttyACM0 -o MyOutputFile.csv
```

## Read data
```
$ python goldstandard --data MyOutputFile.csv
``` 

## Histogram data

### With time constant

```
$ python goldhist --data resources/Photoresistor_Delta_Response.csv -t --tcut 10
```

### Std deviation

```
$ python goldhist --data resources/Photoresistor_Background_Response.csv --std 241
$ python goldhist --data resources/Photoresistor_Nominal_Response.csv --std 1170
```
