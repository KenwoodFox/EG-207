// Team Gold
// EG-207, SNHU

// y = 3664347000 + (238.5626 - 3664347000)/(1 + (x/19246.87)^4.36837)

class CDS55 {
    private:
        unsigned int pin; // What pin the sensor is on
        signed int value; // The current value of the sensor
    public:
        CDS55(unsigned int _pin) {
            pin = _pin; // Update pin
        };

        signed int getRawValue() {
            //value = analogRead(pin);
            value = 251;
            return value;
        };

        double getLuxValue() {
            getRawValue(); // Populate value

            // Magic 4th order polynomial (Sucks a lot)
            double luxvalue = -525.0179 + (8.14062 * value) - (0.02335421* pow(value, 2)) + (0.00002457257 * pow(value, 3));
            return luxvalue;
        };
};
