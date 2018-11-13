from tkinter import *
from tkinter import ttk
import serial
import time
import sys

ser = serial.Serial(port='COM12',baudrate=9600, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS, timeout=0)
grados = 0
servo1_rutina = []
servo2_rutina = []
servo3_rutina = []
servo4_rutina = []

for x in range(50):
    ser.reset_input_buffer()
    ser.reset_output_buffer()
    time.sleep(.2)
    recibido1 = ser.read()
    recibido2 = ser.read()
    recibido3 = ser.read()
    recibido4 = ser.read()
    recibido5 = ser.read()
    print(recibido1, recibido2, recibido3, recibido4, recibido5)
    if (recibido5 == (13).to_bytes(1, byteorder = 'big')):
        servo1_rutina.append(recibido1)
        servo2_rutina.append(recibido2)
        servo3_rutina.append(recibido3)
        servo4_rutina.append(recibido4)
    else:
        servo1_rutina.append(servo1_rutina[len(servo1_rutina)-1])
        servo2_rutina.append(servo2_rutina[len(servo2_rutina)-1])
        servo3_rutina.append(servo3_rutina[len(servo3_rutina)-1])
        servo4_rutina.append(servo4_rutina[len(servo4_rutina)-1])

for y in range(len(servo1_rutina)):
    print(servo1_rutina[y], servo2_rutina[y], servo3_rutina[y], servo4_rutina[y])
