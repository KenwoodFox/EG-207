#include "DHT.h"
#include "Arduino.h"
#include "TimerOne.h"

// DHT pin definition
#define DHTPIN 2

// DHT type
#define DHTTYPE DHT11

// Create DHT object (requires DHT.h)
DHT dht(DHTPIN, DHTTYPE);

// Sensor variables
volatile float dhtHumidity;
volatile float dhtTemperature;

// Misc persistant data
float sum = 0;


void setup() {
  // Start serial comms and make serial buffer
  Serial.begin(115200);

  // Begin DHT listener
  dht.begin();

  // Initalize hardware inturrupts.
  Timer1.initialize(200000);

  // Attach updateDHT to hw inturrupt
  Timer1.attachInterrupt(updateDHT);
}

/* Listen for inturrupts and change a volitalie
 * array of data with new values when appropriate
 */
void updateDHT(void) {
  // Read in dht data
  float h = dht.readHumidity();
  float t = dht.readTemperature();

  // If either number is NAN, the frame is invalid!
  if (isnan(h) || isnan(t)) {
    ;
  } else {
    // Valid frame data si not coppied
    dhtHumidity = h;
    dhtHumidity = t;
  }
}


void loop() {
  // Check if data changed (TODO: Replace with actual data checksum)
  if (dhtHumidity + dhtTemperature != sum) {
    // Send large serial frame
    Serial.print("H"); Serial.print(dhtHumidity); Serial.print(",");
    Serial.print("T"); Serial.print(dhtTemperature); Serial.print(",\n");

    sum = dhtHumidity + dhtTemperature;
  }
}
