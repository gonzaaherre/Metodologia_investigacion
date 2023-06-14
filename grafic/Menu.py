import tkinter as tk
from tkinter import *
from math import *

import random
class Opciones(Toplevel):
    def __init__(self,master=None):
        super().__init__(master=master)
        self.title("Opciones")
        self.geometry("300x300")
        label = Label(self,text="")
        label.pack()
        self.grab_set()
class Ruleta(Toplevel):
    def __init__(self, master=None):
        super().__init__(master=master)
        self.title("Ruleta")
        self.geometry("500x600")
        canvas = Canvas(self, width=400, height=400)
        canvas.pack()
        self.dibujar_ruleta(canvas)
        self.grab_set()

    def dibujar_ruleta(self, canvas):
        # Configuración de colores
        color_fondo = "#FFFFFF"  # Color de fondo de la ruleta
        color_lineas = "#000000"  # Color de las líneas
        color_numeros = "#FF0000"  # Color de los números

        # Dibujar fondo de la ruleta
        # canvas.create_oval(50, 50, 350, 350, fill=color_fondo, outline=color_lineas, width=2)

        # Dibujar líneas
        for i in range(0, 360, 18):
            angulo = i * 3.14159 / 180.0
            x1 = 200 + 140 * sin(angulo)
            y1 = 200 - 140 * cos(angulo)
            x2 = 200 + 160 * sin(angulo)
            y2 = 200 - 160 * cos(angulo)
            canvas.create_line(x1, y1, x2, y2, fill=color_lineas, width=2)

        # Dibujar números
        for i in range(0, 360, 18):
            angulo = i * 3.14159 / 180.0
            x = 200 + 130 * sin(angulo)
            y = 200 - 130 * cos(angulo)
            canvas.create_text(x, y, text=str(i), fill=color_numeros, font=("Arial", 12), anchor=NW)


menu = Tk()
menu.geometry('800x533')
menu.title('Menu principal')
menu.resizable(width=False, height=False)

# Configuración de la imagen de fondo
bg_image = PhotoImage(file="")  # Reemplaza "ruta_de_la_imagen.png" con la ruta real de tu imagen
label1 = Label(menu, image=bg_image)
label1.place(x=0, y=0)

titulo = Label(menu, text='Bienvenido al Casino')
titulo.pack(pady=10)
        
menu = Tk()
menu.geometry('800x533')
menu.title('Menu principal')
menu.resizable(width=False, height=False)
bg = PhotoImage(file="")
label1 = Label(menu, image=bg)
label1.place(x=0,y=0)
titulo = Label(menu, text='Bienvenido al Casino')
titulo.pack(pady=10)

def start():
    pass


def load():
    pass


def options():
    pass
def salida():
    menu.destroy()


boton_comenzar = Button(menu, text='Ruleta')
boton_comenzar.bind("<Button>",lambda e: Ruleta(menu))
boton_comenzar.pack(pady=10)
boton_cargar = Button(menu, text='Cargar', command=load)
boton_cargar.pack(pady=3)
boton_opciones = Button(menu, text='Opciones')
boton_opciones.bind("<Button>", lambda e: Opciones(menu))
boton_opciones.pack(pady=3)
boton_salir = Button(menu, text='Salir', command=salida)
boton_salir.pack(pady=3)
menu.mainloop()
