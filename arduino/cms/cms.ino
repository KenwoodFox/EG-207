// EG-207, SNHU
// Team Gold


// Public libraries
#include <Arduino.h>
#include <Servo.h>

// Config/Build
#include "pindefs.h"
#include "version.h"

// Sensors
#include "sensors/WaterLevelSensor.cpp"
#include "sensors/CDS55.cpp"
#include "sensors/ParallaxUVSensor.cpp"

// Construct Sensor Objects
WaterLevelSensor rainFlow = WaterLevelSensor(ANALOG_WATER, ENABLE_WATER);
UVSensor uvSensor = UVSensor(ANALOG_UVSENSOR);
CDS55 cds55 = CDS55(DATA_DHT11);

//Servo myservo;  // create servo object to control a servo
// twelve servo objects can be created on most boards

//int pos = 0;    // variable to store the servo position
//int max = 145;
//int min = 20;

void setup() {
  //myservo.attach(3);  // attaches the servo on pin 9 to the servo object
  Serial.begin(115200);
}

void loop() {
  Serial.println(rainFlow.getRawValue());
  Serial.println(uvSensor.getRawValue());
  Serial.println(cds55.getRawValue());

  //for (pos = min; pos <= max; pos += 1) { // goes from 0 degrees to 180 degrees
  //  // in steps of 1 degree
  //  myservo.write(pos);              // tell servo to go to position in variable 'pos'
  //  delay(10);                       // waits 15ms for the servo to reach the position
  //}

  //delay(2000);

  //for (pos = max; pos >= min; pos -= 1) { // goes from 180 degrees to 0 degrees
  //  myservo.write(pos);              // tell servo to go to position in variable 'pos'
  //  delay(10);                       // waits 15ms for the servo to reach the position
  //}

  //delay(2000);
  delay(1000);
}
