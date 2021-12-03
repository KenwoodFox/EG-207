// EG-207, SNHU
// Team Gold


// Public libraries
#include "Arduino.h"

// Config/Build
#include "pindefs.h"
#include "version.h"

// Sensors
#include "WaterLevelSensor.cpp"


// Construct Sensor Objects
WaterLevelSensor rainFlow = WaterLevelSensor(ANALOG_WATER, ENABLE_WATER);

void setup()
{
  Serial.begin(115200);
  pinMode(12, OUTPUT);
}

void loop()
{
  Serial.println(rainFlow.getRawValue());
  delay(1000);
}
