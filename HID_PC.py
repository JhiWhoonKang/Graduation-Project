import hid
import time

VID = 0x16C0
PID = 0x0486

try:
    device = hid.device()
    device.open(VID, PID)

    send_data = [0] * 64
    #send_data[0] = 5
    send_data[1] = 1
    send_data[2] = 0xF3
    send_data[3] = 0xF3
    send_data[4] = 0xF3
    send_data[5] = 0xF3
    send_data[6] = 0xF3
    send_data[7] = 0xF3
    send_data[2] = 0xF3
    send_data[63] = 3
    #send_data[64]=2

    device.write(send_data)

    while True:
        data = device.read(64)
        if data:
            print("Received:", data)
            break

    device.close()

except IOError as e:
    print(e)
    print("Teensy 꽂으셈")