from tkinter import *
class Opciones(Toplevel):
    def __init__(self,master=None):
        super().__init__(master=master)
        self.title("Opciones")
        self.geometry("300x300")
        label = Label(self,text="No implementado")
        label.pack()
        self.grab_set()
class Ruleta(Toplevel):
    def __init__(self,master=None):
        super().__init__(master=master)
        self.title("Ruleta")
        self.geometry("500x600")
        label_ruleta=Label(self,text="No implementado")
        label_ruleta.pack()
        self.grab_set()
menu = Tk()
menu.geometry('800x533')
menu.title('Menu principal')
menu.resizable(width=False, height=False)
bg = PhotoImage(file="images/fondo.png")
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
