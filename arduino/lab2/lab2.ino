// Team Gold
// EG-207, SNHU
// Lab 2

// Public libraries
#include "Arduino.h"
#include "TimerOne.h"

// Team Gold libraries
#include "CDS55.h"
#include "UVSensor.h"

// Auto-generated defs
#include "version.h"
#include "eeprom_settings.h"

// Sensor pin defs
#define CDSPIN 2
#define UVSENSORPIN 4

// Create sensor objects
CDS55 my_photoresistor = CDS55(CDSPIN);
UVSensor my_uvsensor = UVSensor(UVSENSORPIN);

// Sensor variables
float photoresistorLux = 0;
float UVIndex = 0;

// Misc persistant data
float sum = 0;
int stimulate = 0; // counts up

// Flags
bool checkdht = false;


void setup() {
  // Start serial comms and make serial buffer
  Serial.begin(115200);

  // Delay while host device establishes a link (Mostly for LabView being weird)
  delay(1000);

  // Initalize hardware inturrupts.
  Timer1.initialize(500000); // Every 50 ms

  // Attach raiseDHTFlag to hw inturrupt
  Timer1.attachInterrupt(raiseDHTFlag);

  // Spit out MOTD
  // print out some information about the software we're running.
  Serial.print("Starting Team Gold LAB2 software. Using version "); Serial.println(VERSION);
  Serial.print("This software compiled on "); Serial.println(COMPILED_ON); Serial.println(); // Could use __DATE__ and __TIME__ instead

  // Delay before starting tasks.
  delay(200);

  // Start all tasks.
  // Start raiseDHTFlag.
  Timer1.start();
}


/* Listen for inturrupts and change a volitalie
 * array of data with new values when appropriate
 */
void raiseDHTFlag(void) {
  checkdht = true;
  stimulate++;
}


void loop() {
  // Slow loop
  delay(100);

  // If its time to check the DHT sesor
  if (checkdht) {
    // Read in sensor data
    int _l = my_photoresistor.getLuxValue(); // Int because values are sometimes invalid
    int _u = my_uvsensor.getRawValue();

    // If either number is NAN, the frame is invalid!
    if (isnan(_l) || isnan(_u)) {
      //Serial.println("Got invalid frame."); // Debug!
    } else {
      //Serial.println("Got valid frame."); // Debug!
      // Valid frame data is coppied.
      photoresistorLux = _l;
      UVIndex = _u;
    }
  }

  // Check if data changed (TODO: Replace with actual data checksum)
  if (photoresistorLux + UVIndex != sum || stimulate > 8) {
    // Send large serial frame
    Serial.print("H"); Serial.print(1.00);Serial.print(',');
    Serial.print("T"); Serial.print(1.00);Serial.print(',');
    Serial.print("L"); Serial.print(photoresistorLux);Serial.print(',');
    Serial.print("U"); Serial.print(UVIndex);
    Serial.print("\n\r");

    sum = photoresistorLux + UVIndex;

    stimulate = 0;
  } else { 
    //Serial.println("Nothing to send."); // Debug!
  }
}
