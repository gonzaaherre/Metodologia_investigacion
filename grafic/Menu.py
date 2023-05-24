from tkinter import *

menu = Tk()
menu.geometry('800x533')
menu.title('Menu principal')
menu.resizable(width=False, height=False)
bg = PhotoImage(file="fondo.png")
label1 = Label(menu, image=bg)
label1.pack()
titulo = Label(menu, text='Bienvenido al Casino')
titulo.pack(side=TOP, pady=10)

def start():
    pass


def load():
    pass


def options():



def salida():
    pass


boton_comenzar = Button(menu, text='Comenzar', command=start)
boton_comenzar.place(x=200, y=70)
boton_cargar = Button(menu, text='Cargar', command=load)
boton_cargar.place(x=210, y=100)
boton_opciones = Button(menu, text='Opciones', command=options)
boton_opciones.place(x=205, y=130)
boton_salir = Button(menu, text='Salir', command=salida)
boton_salir.place(x=220, y=160)
menu.mainloop()
