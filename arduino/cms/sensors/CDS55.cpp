// Team Gold
// EG-207, SNHU

// Public Libs
#include <EEPROM.h>


class CDS55 {
    private:
        unsigned int pin; // What pin the sensor is on
        signed int value; // The current value of the sensor
    public:
        CDS55(unsigned int _pin) {
            pin = _pin; // Update pin
        };

        int getRawValue() {
            value = analogRead(pin);
            return value;
        };

        float getLuxValue() {
            float f_value = getRawValue(); // Populate value

            // Polynomial conversion
            float coefA;
            float coefB;
            float coefC;

            EEPROM.get(COEF_PHOTO_A, coefA);
            EEPROM.get(COEF_PHOTO_B, coefB);
            EEPROM.get(COEF_PHOTO_C, coefC);

            float luxvalue = (coefA * pow(f_value, 2)) - (coefB * f_value) + coefC;

            if (luxvalue > 0) {
                return luxvalue; // Only return valid outputs 
            } else {
                return sqrt(-1); // NaN any other time.
            }

        };
};
