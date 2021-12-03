// Team Gold
// EG-207, SNHU

// Public libraries
#include "Arduino.h"


class WaterLevelSensor {
    private:
        unsigned int pin;           // What pin the sensor is on
        unsigned int enable_pin;    // What pin enables the sensor
        signed int value;           // The current value of the sensor
    public:
        WaterLevelSensor(unsigned int _pin, unsigned int _enable_pin) {
            pin = _pin; // Update pins
            enable_pin = _enable_pin;

            pinMode(enable_pin, OUTPUT);
            //pinMode(pin, INPUT);
        };

        signed int getRawValue() {
            digitalWrite(enable_pin, LOW); // Turn on the sensor.
            delay(100);                      // Wait for ms for value to stab.
            value = analogRead(pin);        // Read the current sensor value.
            digitalWrite(enable_pin, HIGH);  // Disable the sensor when done.
            return value;
        };
};
