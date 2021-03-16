
#include <SerialPort.h>

SerialPort::SerialPort(int baudrate)
{
    Serial.begin(baudrate);
}

bool SerialPort::messageToRead(void) // Wrapper function; RUN BEFORE DECODING NEXT MESSAGE
{
    return Serial.available(); // check if there's a message
}

void SerialPort::decodeNextMessage(uint8_t* deviceID, int* value) // take in a pointer to store the result of the next message
{
    
}

std::string SerialPort::encodePacket(int deviceID, int value)
{
    char temp[2];
    sprintf(temp, "%02X", deviceID);
    std::string id = temp;

    char temp2[3];
    std::string val;

    val = value < 0 ? "F" : "0"; // if value < 0, val = "F", else val = "0";
    value = value < 0 ? 256 + value : value; // swaps -1 -> 255 if value is negative to convert to two's complement

    sprintf(temp2, "%02X", value);
    std::string temp3 = temp2;

    return id + val + temp3 + ",";
}

std::string SerialPort::sendMessage(std::string packets[]) // packets -> [id1, val1, id2, val2, id3, val3]
{
    return "";
}