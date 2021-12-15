# from adafruit_servokit import ServoKit
# myKit = ServoKit(channels=16)
# myKit.servo[1].angle=20

import board
import math
import time
i2c = board.I2C()
deice_address = i2c
print(i2c, deice_address)