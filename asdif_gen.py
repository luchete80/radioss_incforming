#https://www.tutorialsteacher.com/python/create-ui-using-tkinter-in-python
from math import *
import mesher as msh
import numpy as np

from tkinter import *
from tkinter.ttk import Combobox
window=Tk()
linea_g=10

#IMPORTANTE - ACA ESTA DEFINIDO TOOL SPEED
#INPUT VARS
#VER COMO ACOMODAR CON ALFA Y BETA ANGULOS
r_i         = 0.01
r_o         = 0.0325    #NO CONFUNDI CON HERRAMENTAS IN Y OOUT
r           = 0.0325
dr          = 5.0e-4    #DESAPARECE DE ACUERDO A LA GEOMETRIA
t_end       = 1.0e-1
dt          = 1.0e-5
#t_ang       = 1.0e-3    #Periodo angular, ANTES ERA CONSTANTE
p_D         = 2.5e-3     #ASDIF RADIAL DISTANCE BETWEEN TOOLS
p_S         = 4.3e-4     #ASDIF HEIGHT DISTANCE BETWEEN TOOLS
tool_speed  = 0.6 / 60.0 * 5000 #600mm/min according to Valoppi
t_ind       = 1.0e-3
thck        = 5.0e-4

filelbl = Label(window, text="Archivo", width=15,justify=LEFT)
filelbl.grid(column=1, row=0)	
textField = Entry(window, width=15)
textField.grid(column=2, row=0)
textField.insert(0,"test.txt")

test = [(1,1),(2,2)]
test.append((3,4))
print (test)
print (test[2][0])
#############################################################################################################################################
largo = 0.3
delta = 0.01
# shell_nodos = [(0,0,0)]
shell_elnod = [(1,2,3,4)]

shell_mesh = msh.Plane_Mesh(largo,delta)

shell_mesh.printRadioss("radioss.rad")

#IMPORTANTE: LA VELOCIDAD SE ASUME PARA RADIO CONSTANTE EN CADA VUELTAS
#CON LO CUAL EN LA REALIDAD DISMINUYE UN POCO
def save(lin):
# f= open(textField.get(),"w+")
  # LA HERRAMIENTA INTERNA ESTA EN EL TOP, LA EXTERNA EN EL BOTTOM
  # PERO TOP Y BOTTOM CONFUNDE POR LAS INDENTACIONES
  fi_x = open("movi_x.csv","w")
  fi_y = open("movi_y.csv","w")
  fi_z = open("movi_z.csv","w")
  fo_x = open("movo_x.csv","w")
  fo_y = open("movo_y.csv","w")
  fo_z = open("movo_z.csv","w")
  
  t = 0.0
  r = r_i
  turn = 1
  
  z  = 0.0 
  zo = -thck #ESTA HERRAMIENTA NO DESCIENDE (PARA EVITAR DEFORMACIONES IRREGULARES)
  zi =  thck 
  vz = (thck + p_S) / t_ind # EN PRINCIPIO S EDESPLAZA SOLO LA INTERIOR 
  
  #####################INDENTACION ######################### 
  xi = r - p_D/2.0
  xo = r + p_D/2.0
  
  while (t < t_ind):    
    zi -= vz * dt
    #HAY QUE VER SI ES NECESARIO ESCRIBIR X E Y PARA TODOS LOS TIEMPOS
    fi_x.write("%.6e, %.6e\n" % (t,xi))
    fi_y.write("%.6e, %.6e\n" % (t,0.0))
    fi_z.write("%.6e, %.6e\n" % (t,zi))

    fo_x.write("%.6e, %.6e\n" % (t,xo))
    fo_y.write("%.6e, %.6e\n" % (t,0.0))
    fo_z.write("%.6e, %.6e\n" % (t,zo))  
    t +=dt 
 
  print("Final zi %.3e , zo %.3e \n" %(zi,zo))
  
  ######################## VUELTAS ##############################
  while (t < t_end):
    t_ang = 2.0 * pi * r / tool_speed #Tiempo (incremento) de cada vuelta (ASUMIENDO RADIO CONSTANTE)
    print("Turn %d Turn Time %.3e Time %.3e Radius %.3e\n" %(turn, t_ang,t,r))
    t_vuelta = t + t_ang  #Tiempo de final de vuelta (TOTAL)
    t_0 = t               #Tiempo de comienzo de vuelta
    t_inc = 0.0           # t - t_0
    dz = dr               #CAMBIAR SEGUN GEOMETRIA
    vz = dz / t_ang
    while (t < t_vuelta): #VUELTAS  
      # print ("t_inc %.3e t_ang %.3e"%(t_inc,t_ang))
      xi = (r - p_D/2.0 + dr * t_inc/t_ang) *cos(2.0*pi*t_inc/t_ang)
      yi = (r - p_D/2.0 + dr * t_inc/t_ang) *sin(2.0*pi*t_inc/t_ang)
      zi -= vz * dt

      xo = (r + p_D/2.0 + dr * t_inc/t_ang) *cos(2.0*pi*t_inc/t_ang)
      yo = (r + p_D/2.0 + dr * t_inc/t_ang) *sin(2.0*pi*t_inc/t_ang)      
      zo -= vz * dt #CAMBIAR A DZ
      
      # print("zi %.3e , zo %.3e \n" %(zi,zo))
      # z -= t_inc/t_ang * dr # CAMBIAR A dz
      
      fi_x.write("%.6e, %.6e\n" % (t,xi))
      fi_y.write("%.6e, %.6e\n" % (t,yi))
      fi_z.write("%.6e, %.6e\n" % (t,zi))

      fo_x.write("%.6e, %.6e\n" % (t,xo))
      fo_y.write("%.6e, %.6e\n" % (t,yo))
      fo_z.write("%.6e, %.6e\n" % (t,zo))
      
      t_inc +=dt
      t += dt
      
    r +=dr
    turn += 1    

  #SPRINGBACK
  fi_x.close;fi_y.close;fi_z.close
  fo_x.close;fo_y.close;fo_z.close

  print("End zi %.3e, zo %.3e" % (zi,zo))


#Si no se coloca lambda no funciona
b = Button(window, text="Generar", width=10, command=lambda:save(linea_g))
b.grid(column=3, row=10)
#b.pack()

window.title('Incremental Forming PATH Script')
window.geometry("400x200+10+10")
window.mainloop()