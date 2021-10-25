// Team Gold
// EG-207, SNHU


class CDS55 {
    private:
        unsigned int pin; // What pin the sensor is on
        signed int value; // The current value of the sensor
    public:
        CDS55(unsigned int _pin) {
            pin = _pin; // Update pin
        };

        signed int getRawValue() {
            value = analogRead(pin);
            return value;
        };

        int getLuxValue() {
            getRawValue(); // Populate value

            // Magic 4th order polynomial (Sucks a lot)
            // Based purely on provided lab data.
            int luxvalue = 1020.881 - (19.60206 * value) + (0.1080073 * pow(value, 2)) - (0.0001971755 * pow(value, 3)) + (1.218544e-7* pow(value, 4));

            if (luxvalue > 0) {
                return luxvalue; // Only return valid outputs 
            } else {
                return sqrt(-1); // NaN any other time.
            }

        };
};
