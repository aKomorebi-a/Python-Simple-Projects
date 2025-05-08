import tkinter as tk
from tkinter import ttk
from tkinter import *
import pyperclip as paper
'''Ejemplo tkinter'''

# def actualizar_texto():
#     etiqueta.config(text="HOla mundo")


# # ventana principal
# ventana = tk.Tk()
# ventana.title("Ejemplo Tkinter")

# # widgets
# etiqueta = tk.Label(ventana, text="texto inicial")
# boton = tk.Button(ventana, text="haz clic", command=actualizar_texto)

# # Diseño
# etiqueta.pack(pady=50)
# boton.pack(pady=30)

# ventana.mainloop()

class ConvertMayus:
    def __init__(self, main):
        main.title("Convertir a mayuscula")

        mainframe = ttk.Frame(main, padding="20 20 20 40")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        main.columnconfigure(0, weight=1)
        main.rowconfigure(0, weight=1)

        self.mayus = StringVar()

        ttk.Label(mainframe, text="Introduce la Palabra: ").grid(
            column=0, row=1, sticky=(W, E))

        mayus_entry = ttk.Entry(
            mainframe, justify="left", width=50, textvariable=self.mayus)
        mayus_entry.grid(column=1, row=1, sticky=(W, E))

        self.result_mayus = StringVar()

        ttk.Label(mainframe, textvariable=self.result_mayus).grid(
            column=1, row=2, sticky=(W, E))

        ttk.Button(mainframe, text="Convertir", command=self.convertir_mayuscula).grid(
            column=1, row=3, sticky=(W, E))

        ttk.Label(mainframe, text="En mayusculas es: ").grid(
            column=0, row=2, sticky=E)

        for child in mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)

        mayus_entry.focus()
        main.bind("<Return>", self.convertir_mayuscula)

    def convertir_mayuscula(self, *args) -> str:
        try:
            palabra = self.mayus.get()
            x = palabra.upper()
            self.result_mayus.set(x)
            paper.copy(x)
        except:
            print("error")


main = Tk()
ConvertMayus(main)
main.mainloop()
