// Team Gold
// EG-207, SNHU


/* A single packet with
 * only one data value
 */
class DataPacket{
    private:
        char name; // The name this packet will use
        float value = 15.000; // The currently set value
    public:
        DataPacket(char _name) {
            name = _name; // Set the name for this packet
        };

        String getPacket() {
            String packetstring = String(name); // Set to string name, ie: "T"

            if (packetstring.concat(value)) {
                return packetstring; // Only return if concat works.
            }
        };
};
