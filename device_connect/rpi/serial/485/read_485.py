import serial


dev = "/dev/ttyAMA2"
boudrace = 9600

with serial.Serial(dev, boudrace) as ser:
    print(ser.is_open)
    print(ser.name)
    ser.read()
