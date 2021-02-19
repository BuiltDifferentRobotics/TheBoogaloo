import serial

ser = serial.Serial('/dev/ttyUSB0', 115200)

# Make a map to store <id, value>
# Function that gets a value for given id
# Function that asks for value from arduino??
# Split encoded serial by comma

def encode_serial(id, value):
    return id + value + ","

def decode_serial(serialMessage):
    id = serialMessage[0:2]
    value = serialMessage[2:5]

def send_serial(message):
    ser.write(message)


def read_serial():
    if ser.in_waiting() > 0:
        print(ser.read())

while True:
    read_serial()
    send_serial(input("Input:"))
