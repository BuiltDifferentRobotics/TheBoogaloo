import serial

ser = serial.Serial(115200)


def post_serial(id, value):
    return id + value + ","


def send_serial(message):
    ser.write(message)


def read_serial(message_to_read):
    print(message_to_read)


while True:
    string1 = "id";
    string2 = "value"
    while ser.in_waiting > 0:
        read_serial(ser.read())
    post_serial(string1, string2)
    send_serial(post_serial())
