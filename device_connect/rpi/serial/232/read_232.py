import serial


dev = "/dev/ttyAMA1"
boudrace = 9600

with serial.Serial(dev, boudrace) as ser:
    print(ser.is_open)
    print(ser.name)
    ser.read()
