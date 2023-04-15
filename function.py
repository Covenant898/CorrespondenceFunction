import tkinter
import example_modulo as ex_md

ventana = tkinter.Tk()
ventana.title("Funcion de Correspondencia")
ventana.geometry("650x500") #anchoXaltura

etique = tkinter.Label(ventana, text="Ingrese Datos")
etique.grid(row = 0, column = 2)

ex_md.memory(ventana, "Memoria Principal", 1, 0, 3, "Celdas n-bits", "Direcciones lambda-bits", "Bloques b-celda")
ex_md.memory(ventana, "Memoria Cache", 1, 3, 2, "Lineas b-celdas", "Conjuntos j-vias")

ventana.mainloop()

