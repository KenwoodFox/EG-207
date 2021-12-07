// Team Gold
// EG-207, SNHU


class UVSensor {
    private:
        unsigned int pin; // What pin the sensor is on
        signed int value; // The current value of the sensor
    public:
        UVSensor(unsigned int _pin) {
            pin = _pin; // Update pin
        };

        unsigned int getRawValue() {
            value = analogRead(pin);
            return value;
        };
};
