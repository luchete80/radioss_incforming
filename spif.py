#https://www.tutorialsteacher.com/python/create-ui-using-tkinter-in-python
from math import *


from tkinter import *
from tkinter.ttk import Combobox
window=Tk()
linea_g=10

#INPUT VARS
r     = 0.0325
dr    = 5.0e-4
t_end = 4.0e-2
dt    = 1.0e-5
t_ang = 1.0e-3 #Periodo angular
z_0   = 5.0e-4

filelbl = Label(window, text="Archivo", width=15,justify=LEFT)
filelbl.grid(column=1, row=0)	
textField = Entry(window, width=15)
textField.grid(column=2, row=0)
textField.insert(0,"test.txt")

def save(lin):
# f= open(textField.get(),"w+")
# X DIRECTION
  fx = open("movx.csv","w+")
  fy = open("movy.csv","w+")
  fz = open("movz.csv","w+")
  
  t = 0.0
  while (t < t_end):
    x = r - dr * t/t_ang *cos(2.0*pi*t/t_ang)
    y = r - dr * t/t_ang *sin(2.0*pi*t/t_ang)
    z = z_0 - t * dr/t_ang
    fx.write("%.6e, %.6e\n" % (t,x))
    fy.write("%.6e, %.6e\n" % (t,y))
    fz.write("%.6e, %.6e\n" % (t,z))
    t += dt
  fx.close
  fy.close
  fz.close

#Si no se coloca lambda no funciona
b = Button(window, text="Generar", width=10, command=lambda:save(linea_g))
b.grid(column=3, row=10)
#b.pack()

window.title('Generador Codigo G')
window.geometry("400x200+10+10")
window.mainloop()