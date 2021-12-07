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


void setup() {
  // Init serial
  Serial.begin(115200);

  // Setup Status LEDs
  pinMode(STATUS_LED, OUTPUT);
}


void loop() {
  // Blink Status LED with loop counter
  if (LC > 127){digitalWrite(STATUS_LED, LOW);}else{digitalWrite(STATUS_LED, HIGH);}

  // Cleanup mainloop.
  cleanup();

  // This is one of the few holding commands in our program, it scales excecution speed.
  delay(4);
}


void cleanup() {
  // Cleanup tasks to be run at the END of the mainloop

  // Check for ACK at end of instruction.
  if (ACK) {
    Serial.println("ok"); // Send ACK.
    ACK = false; // Reset ACK flag.
  }

  // Increment LC
  LC++;
}


void serialEvent() {
  // Serial event is called when the serial buffer has an instruction.
  noInterrupts(); // Do not be interrupted

  // As long as serial data is available
  while (Serial.available()) {
    // Switch on serial.read single instruction.
    int instruct = Serial.read();

    switch (instruct) {
      case 0x76: // Instruction v
        Serial.println(VERSION); // Print Version
        break;
      
      case 0x65: // Instruction E
        Serial.println("No Errors in EEPROM.");
        break;
      
      default:
        // Bad or unknown instruction
        Serial.print("?");Serial.println(instruct, HEX);
        break;
    }

    ACK = true; // Raise ACK flag.
  }

  interrupts(); // Resume being interrupted.
}
