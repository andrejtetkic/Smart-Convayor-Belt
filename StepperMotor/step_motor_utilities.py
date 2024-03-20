# # import RPi.GPIO as GPIO
# # import time

# # GPIO.setmode(GPIO.BOARD)

# # ControlPin = [7,11,13,15]

# # for pin in ControlPin:
# #     GPIO.setup(pin,GPIO.OUT)
# #     GPIO.output(pin,0)

# # seq = [[1,0,0,0],
# #        [1,1,0,0],
# #        [0,1,0,0],
# #        [0,1,1,0],
# #        [0,0,1,0],
# #        [0,0,1,1],
# #        [0,0,0,1],
# #        [1,0,0,1]]

# # for i in range(512):
# #     for halfstep in range(8):
# #         for pin in range(4):
# #             GPIO.output(ControlPin[pin], seq[halfstep][pin])
# #         time.sleep(0.001)


# # GPIO.cleanup(0)


# import RPi.GPIO as GPIO
# import time
 
# GPIO.setmode(GPIO.BCM)
# GPIO.setwarnings(False)
# coil_A_1_pin = 4 # pink
# coil_A_2_pin = 17 # orange
# coil_B_1_pin = 23 # blue
# coil_B_2_pin = 24 # yellow
 
# # adjust if different
# StepCount = 8
# Seq = range(0, StepCount)
# Seq[0] = [1,0,0,0]
# Seq[1] = [1,1,0,0]
# Seq[2] = [0,1,0,0]
# Seq[3] = [0,1,1,0]
# Seq[4] = [0,0,1,0]
# Seq[5] = [0,0,1,1]
# Seq[6] = [0,0,0,1]
# Seq[7] = [1,0,0,1]
 

# enable_pin = 18
# GPIO.setup(enable_pin, GPIO.OUT)
# GPIO.setup(coil_A_1_pin, GPIO.OUT)
# GPIO.setup(coil_A_2_pin, GPIO.OUT)
# GPIO.setup(coil_B_1_pin, GPIO.OUT)
# GPIO.setup(coil_B_2_pin, GPIO.OUT)
 
# GPIO.output(enable_pin, 1)
 
# def setStep(w1, w2, w3, w4):
#     GPIO.output(coil_A_1_pin, w1)
#     GPIO.output(coil_A_2_pin, w2)
#     GPIO.output(coil_B_1_pin, w3)
#     GPIO.output(coil_B_2_pin, w4)
 
# def forward(delay, steps):
#     for i in range(steps):
#         for j in range(StepCount):
#             setStep(Seq[j][0], Seq[j][1], Seq[j][2], Seq[j][3])
#             time.sleep(delay)
 
# def backwards(delay, steps):
#     for i in range(steps):
#         for j in reversed(range(StepCount)):
#             setStep(Seq[j][0], Seq[j][1], Seq[j][2], Seq[j][3])
#             time.sleep(delay)
 
# if __name__ == '__main__':
#     while True:
#         delay = raw_input("Time Delay (ms)?")
#         steps = raw_input("How many steps forward? ")
#         forward(int(delay) / 1000.0, int(steps))
#         steps = raw_input("How many steps backwards? ")
#         backwards(int(delay) / 1000.0, int(steps))
 



# SPDX-FileCopyrightText: 2019 Mikey Sklar for Adafruit Industries
#
# SPDX-License-Identifier: MIT

import time
import board
import digitalio

enable_pin = digitalio.DigitalInOut(board.D18)
coil_A_1_pin = digitalio.DigitalInOut(board.D4)
coil_A_2_pin = digitalio.DigitalInOut(board.D17)
coil_B_1_pin = digitalio.DigitalInOut(board.D23)
coil_B_2_pin = digitalio.DigitalInOut(board.D24)

enable_pin.direction = digitalio.Direction.OUTPUT
coil_A_1_pin.direction = digitalio.Direction.OUTPUT
coil_A_2_pin.direction = digitalio.Direction.OUTPUT
coil_B_1_pin.direction = digitalio.Direction.OUTPUT
coil_B_2_pin.direction = digitalio.Direction.OUTPUT

enable_pin.value = True

def forward(delay, steps):
    i = 0
    while i in range(0, steps):
        setStep(1, 0, 1, 0)
        time.sleep(delay)
        setStep(0, 1, 1, 0)
        time.sleep(delay)
        setStep(0, 1, 0, 1)
        time.sleep(delay)
        setStep(1, 0, 0, 1)
        time.sleep(delay)
        i += 1

def backwards(delay, steps):
    i = 0
    while i in range(0, steps):
        setStep(1, 0, 0, 1)
        time.sleep(delay)
        setStep(0, 1, 0, 1)
        time.sleep(delay)
        setStep(0, 1, 1, 0)
        time.sleep(delay)
        setStep(1, 0, 1, 0)
        time.sleep(delay)
        i += 1

def setStep(w1, w2, w3, w4):
    coil_A_1_pin.value = w1
    coil_A_2_pin.value = w2
    coil_B_1_pin.value = w3
    coil_B_2_pin.value = w4

while True:
    user_delay = input("Delay between steps (milliseconds)?")
    user_steps = input("How many steps forward? ")
    forward(int(user_delay) / 1000.0, int(user_steps))
    user_steps = input("How many steps backwards? ")
    backwards(int(user_delay) / 1000.0, int(user_steps))
