// Team Gold
// EG-207, SNHU

#include "DHT.h"
#include "Arduino.h"
#include "TimerOne.h"

// Build information
#include "version.h"

// DHT pin definition
#define DHTPIN 2

// DHT type
#define DHTTYPE DHT11

// Create DHT object (requires DHT.h)
DHT dht(DHTPIN, DHTTYPE);

// Sensor variables
float dhtHumidity = 0;
float dhtTemperature = 0;

// Misc persistant data
float sum = 0;

// Flags
bool checkdht = false;


void setup() {
  // Start serial comms and make serial buffer
  Serial.begin(115200);

  // Delay while host device establishes a link (Mostly for LabView being weird)
  delay(1000);

  // Begin DHT listener
  dht.begin();

  // Initalize hardware inturrupts.
  Timer1.initialize(50000); // Every 50 ms

  // Attach raiseDHTFlag to hw inturrupt
  Timer1.attachInterrupt(raiseDHTFlag);

  // Spit out MOTD
  // print out some information about the software we're running.
  Serial.print("Starting Team Gold LAB1 software. Using version "); Serial.println(VERSION);
  Serial.print("This software compiled on "); Serial.println(COMPILED_ON); Serial.println();

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
}


void loop() {
  // Slow loop
  delay(50);

  // If its time to check the DHT sesor
  if (checkdht) {
    // Read in dht data
    float _h = dht.readHumidity();
    float _t = dht.readTemperature();

    // If either number is NAN, the frame is invalid!
    if (isnan(_h) || isnan(_t)) {
      //Serial.println("Got invalid frame."); // Debug!
    } else {
      //Serial.println("Got valid frame."); // Debug!
      // Valid frame data is coppied.
      dhtHumidity = _h;
      dhtTemperature = _t;
    }
  }

  // Check if data changed (TODO: Replace with actual data checksum)
  if (dhtHumidity + dhtTemperature != sum) {
    // Send large serial frame
    Serial.print("H"); Serial.print(dhtHumidity);Serial.print(',');
    Serial.print("T"); Serial.print(dhtTemperature);
    Serial.print("\n");

    sum = dhtHumidity + dhtTemperature;
  } else { 
    //Serial.println("Nothing to send."); // Debug!
  }
}
