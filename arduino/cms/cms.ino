// EG-207, SNHU
// Team Gold


// Public libraries
#include <Arduino.h>
#include <Servo.h>

// Config/Build
#include "pindefs.h"
#include "version.h"
#include "flags.h"

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
  // Cleanup mainloop.
  cleanup();

  // This is one of the few holding commands in our program, it scales excecution speed.
  delay(50);
}


void cleanup() {
  // Cleanup tasks to be run at the END of the mainloop

  // Check for ACK at end of instruction.
  if (ACK) {
    Serial.print("ok"); // Send ACK.
    ACK = false; // Reset ACK flag.
  }
}


void serialEvent() {
  // Serial event is called when the serial buffer has an instruction.
  noInterrupts(); // Do not be interrupted

  // As long as serial data is available
  while (Serial.available()) {
    // Switch on serial.read single instruction.
    switch (Serial.read()) {
      case 0x56: // Instruction v
        Serial.println(VERSION); // Print Version
        break;
      
      default:
        // Bad or unknown instruction
        Serial.println("?");
        break;
    }

    ACK = true; // Raise ACK flag.
  }

  interrupts(); // Resume being interrupted.
}