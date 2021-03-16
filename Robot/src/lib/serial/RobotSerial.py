import serial

ser = serial.Serial('/dev/ttyUSB0', 115200)

# Make a map to store <id, value>
# Function that gets a value for given id
# Function that asks for value from arduino??
# Split encoded serial by comma

d = {1: 000, 2: 000, 3: 000}


def get_value_from_id(ID):
    return d.get(ID)


def convert_to_hex(val, is_value):
    prefix = ""
    if is_value:
        prefix = "F" if val < 0 else "0"
        val = val + 256
    return prefix + "{:02X}".format(val)


def encode_serial(ID, value):
    return convert_to_hex(ID, False) + convert_to_hex(value, True) + ","


def decode_serial(serial_message):
    id_decimal = int(serial_message[0:2], 16)
    multiplier = 1 if serial_message[2] == "0" else -1
    value_decimal = int(serial_message[3:5], 16)
    return [id_decimal, multiplier*value_decimal]


def send_serial(message):
    ser.write(message)


def read_serial():
    if ser.in_waiting() > 0:
        print(ser.read())

def run_serial():
    while True:
        read_serial()
        send_serial(input("Input:"))