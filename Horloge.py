import time
import tkinter as tk
from tkinter import ttk

format_temps = "24"

'''def updateHeure ():
    global h_actuel_sys
    h_actuel_sys = time.localtime ()
    time.localtime ( h = {'%H'} ) ( m = {'%M'} ) ( s = {'%S'} ).format ( h_actuel_sys.temps_h,h_actuel_sys.temps_min,
                                                                         h_actuel_sys.temps_sec )
    print ( h_actuel_sys )


def recupheure ():
    time_str = '12::00::00'
    time_object = time.localtime ( time_str,'%H::%M::%S' )

    print ( '%H| %M |%S' )
    print ( time_object )'''

'''frame [ 'padding' ] = (6,10,6,10)'''

def tick():
    label.config(text=time.strftime("%H:%M:%S"))
    label.after(1000, tick)

root = tk.Tk ()

root.geometry ( '400x400' )
root.title ( "Horloge Digital" )
root.resizable ( 0,0 )

label = tk.Label (
    root, text = 'Heure française' )
label.pack ()


# Style pour affichage des heures & des minutes
label_heure = tk.Label (root,text = "16",font = ("Arial",50),fg = "#11ff22",bg = "blue" )

label = tk.Label(root, font=("times", 50, "bold"), bg="white")
label.pack(fill="both", expand=True)
tick()


label_heure.place(x = 400, y = 300)

root.mainloop ()




'''time_label_min = Label ( root,text = "",font = ("Arial",50),fg = "orange" )
time_label_min = Label ( x = 600,y = 450,width = 214,height = 146 )

time_label_seconde = Label ( rootoot,text = "43",font = ("Arial",50),fg = "orange" )
time_label_seconde.place ( x = 1100,y = 450,width = 200,height = 30 )'''


