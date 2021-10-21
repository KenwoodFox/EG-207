// Team Gold
// EG-207, SNHU

/* === Warning! ===
 * this code needs a re-write!
 * do not use! Experimental!
 */

#define GOLD_PACKET_VERSION "AAAAA"


/* A single packet with
 * only one data value
 */
class DataPacket {
    private:
        static char name; // The name this packet will use
        static float value; // The currently set value
    public:
        DataPacket(char _name='X') {
            name = _name; // Set the name for this packet
        };

        String getPacket() {
            String packetstring = String(name); // Set to string name, ie: "T"

            if (packetstring.concat(value)) {
                return packetstring; // Only return if concat works.
            }
        };
};


/* A full data frame,
 * made from many smaller
 * data packets.
 */
class DataFrame {
    private:
        DataPacket sensors[2] = { DataPacket('V'), DataPacket('U') };
    public:
        DataFrame() {
            ;
        };

        // Send a regular frame to the host PC
        bool sendRegularFrame() {
            for (byte i = 0; i<sizeof sensors/sizeof sensors[0]; i++) {
                Serial.println(sensors[i].getPacket);
            }
        };
};
