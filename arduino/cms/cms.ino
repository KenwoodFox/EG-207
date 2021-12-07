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

#include <Servo.h>

Servo myservo;  // create servo object to control a servo
// twelve servo objects can be created on most boards

int pos = 0;    // variable to store the servo position
int max = 145;
int min = 20;

void setup() {
  myservo.attach(3);  // attaches the servo on pin 9 to the servo object
}

void loop() {
  for (pos = min; pos <= max; pos += 1) { // goes from 0 degrees to 180 degrees
    // in steps of 1 degree
    myservo.write(pos);              // tell servo to go to position in variable 'pos'
    delay(10);                       // waits 15ms for the servo to reach the position
  }

  delay(2000);

  for (pos = max; pos >= min; pos -= 1) { // goes from 180 degrees to 0 degrees
    myservo.write(pos);              // tell servo to go to position in variable 'pos'
    delay(10);                       // waits 15ms for the servo to reach the position
  }

  delay(2000);
}
