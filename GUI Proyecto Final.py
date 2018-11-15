from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import serial
import time
import sys

recibido = 0
modo = 0

def serial (*args):
    if modo == 0:
        REC.state(['!disabled'])  
        PLY.state(['!disabled'])
        PS.state(['disabled'])
    elif modo == 1:
        REC.state(['!disabled'])
        PLY.state(['disabled'])
        PS.state(['!disabled'])
    elif modo == 2:
        REC.state(['disabled'])
        PLY.state(['disabled'])
        PS.state(['!disabled'])
    print(modo)
    root.after(50, serial)
    pass
        
def grabar():
    global modo
    modo = 1

def reproducir():
    global modo
    modo = 2

def pausar():
    global modo
    modo = 0

size = 40

root = Tk()
root.title('Proyecto Final')

image1 = Image.open("play.jpg")
play = ImageTk.PhotoImage(image1.resize((size,size)))

image2 = Image.open("record.png")
record = ImageTk.PhotoImage(image2.resize((size, size)))

image3 = Image.open("pause.png")
pause = ImageTk.PhotoImage(image3.resize((size, size)))

mensaje = StringVar()
mensaje.set('testing')

mainframe = ttk.Frame(root, padding='10 10 20 20')
mainframe.grid(column = 0, row = 0, sticky = (N, S, E, W))
root.columnconfigure(0, weight = 1)
root.rowconfigure(0, weight = 1)

num_rutina = IntVar()
num_rutina.set(1)

ttk.Radiobutton(mainframe, text = 'Rutina 1', variable = num_rutina, value = 1).grid(column = 1, row = 1, sticky = (W, E))
ttk.Radiobutton(mainframe, text = 'Rutina 2', variable = num_rutina, value = 2).grid(column = 2, row = 1, sticky = (W, E))
ttk.Radiobutton(mainframe, text = 'Rutina 3', variable = num_rutina, value = 3).grid(column = 3, row = 1, sticky = (W, E))

REC = ttk.Button(mainframe, image = record, command = grabar)
REC.grid(column = 2, row = 2, sticky = (N, S, W, E))
PLY = ttk.Button(mainframe, image = play, command = reproducir)
PLY.grid(column = 1, row = 2, sticky = (N, S, W, E))
PS = ttk.Button(mainframe, image = pause, command = pausar)
PS.grid(column = 3, row = 2, sticky = (N, S, W, E))

ttk.Label(mainframe, textvariable = mensaje, anchor = CENTER).grid(column = 1, columnspan = 3, row = 4, sticky = (W, E))

for child in mainframe.winfo_children():
    child.grid_configure(padx = 10, pady = 10)

root.after(0, serial)
root.mainloop()
