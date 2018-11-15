from tkinter import *
from tkinter import ttk
import serial
import time
import sys

ser = serial.Serial(port='COM12',baudrate=9600, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS, timeout=0)
grados = 0
servo1_rutina = [(0).to_bytes(1, byteorder = 'big')]
servo2_rutina = [(0).to_bytes(1, byteorder = 'big')]
servo3_rutina = [(0).to_bytes(1, byteorder = 'big')]
servo4_rutina = [(0).to_bytes(1, byteorder = 'big')]

for x in range(20):
    ser.reset_input_buffer()
    ser.reset_output_buffer()
    time.sleep(.2)
    recibido1 = ser.read()
    recibido2 = ser.read()
    recibido3 = ser.read()
    recibido4 = ser.read()
    recibido5 = ser.read()
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

for y in range(1,len(servo1_rutina)):
    ser.reset_input_buffer()
    ser.reset_output_buffer()
    time.sleep(.2)
    ser.write(servo1_rutina[y])
    ser.write(servo2_rutina[y])
    ser.write(servo3_rutina[y])
    ser.write(servo4_rutina[y])
    print(servo1_rutina[y], servo2_rutina[y], servo3_rutina[y], servo4_rutina[y])
