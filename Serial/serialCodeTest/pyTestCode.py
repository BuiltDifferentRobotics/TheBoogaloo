import serial

ser = serial.Serial('/dev/ttyUSB0', 115200)

# Make a map to store <id, value>
# Function that gets a value for given id
# Function that asks for value from arduino??
# Split encoded serial by comma

d = {1: 000, 2: 000, 3: 000}


def get_value_from_id(ID):
    return d.get(ID)


def encode_serial(ID, value):
    return ID + value + ","


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
