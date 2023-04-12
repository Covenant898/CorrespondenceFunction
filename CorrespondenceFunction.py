
import tkinter

ventana = tkinter.Tk()
ventana.title("Funcion de Correspondencia")
ventana.geometry("600x400") #anchoXaltura

etique = tkinter.Label(ventana, text="Ingrese Datos")
etique.grid(row = 0, column = 2)
lbl_mP = tkinter.Label(ventana, text="Memoria Principal")
lbl_mC = tkinter.Label(ventana, text="Memoria Cache")

########################################################## Funciones

def tms():
    varN.set( float(varn.get()) ** float(varLam.get()) )
    varB.set( float(varN.get()) / float(varb.get()) )
    mP.set(      ((16*float(varN.get()))/8)/1024     )
    mC.set( float(varL.get()) *  float(varb.get()) )
    mK.set( ((16*float(mC.get()))/8)/1024   )

########################################################## Variables

varn = tkinter.StringVar()
varLam = tkinter.StringVar() #Variable de direccion LAMBDA de bits
varN = tkinter.StringVar()

varb = tkinter.StringVar()
varB = tkinter.StringVar()

mP = tkinter.StringVar()
mC = tkinter.StringVar()
mK = tkinter.StringVar()
varL = tkinter.StringVar()


########################################################## Memoria Principal

lbl_n = tkinter.Label(ventana, text="Celdas n-bits")
caj_n = tkinter.Entry(ventana, textvariable=varn)

lbl_L = tkinter.Label(ventana, text="Direcciones λ-bits")
caj_L = tkinter.Entry(ventana , textvariable=varLam) #textvariable = "Nombre de la variable"

lbl_b = tkinter.Label(ventana, text="Bloques b-celdas")
caj_b = tkinter.Entry(ventana, textvariable=varb)


lbl_mP.grid(row = 1, column = 0)
lbl_n.grid(row = 2, column = 0)
caj_n.grid(row = 2, column = 1)
lbl_L.grid(row = 3, column = 0)
caj_L.grid(row = 3, column = 1)
lbl_b.grid(row = 4, column = 0)
caj_b.grid(row = 4, column = 1)


########################################################## Memoria Cache

lbl_Lb = tkinter.Label(ventana, text="Lineas b-celdas")
caj_Lb = tkinter.Entry(ventana, textvariable=varL)

lbl_j = tkinter.Label(ventana, text="conjuntos j-vias")
caj_j = tkinter.Entry(ventana)

lbl_mC.grid(row = 1, column = 3)
lbl_Lb.grid(row = 2, column = 3)
caj_Lb.grid(row = 2, column = 4)
lbl_j.grid(row = 3, column = 3)
caj_j.grid(row = 3, column = 4)


########################################################## Tamanos

tama = tkinter.Label(ventana, text=" Tamaños ")
tama.grid(row = 5, column = 2)

lbl_N = tkinter.Label(ventana, text=" N : ")
caj_N = tkinter.Entry(ventana, justify="center" ,textvariable=varN)
lbl_N.grid(row = 6, column = 2)
caj_N.grid(row = 7, column = 2)

lbl_B = tkinter.Label(ventana, text=" B : ")
caj_B = tkinter.Entry(ventana, justify="center" ,textvariable=varB)
lbl_B.grid(row = 8, column = 2)
caj_B.grid(row = 9, column = 2)

lbl_MP = tkinter.Label(ventana, text=" MP : ")
caj_MP = tkinter.Entry(ventana, justify="center" ,textvariable=mP)
lbl_MP.grid(row = 10, column = 2)
caj_MP.grid(row = 11, column = 2)

lbl_MC = tkinter.Label(ventana, text=" MC : ")
caj_MC = tkinter.Entry(ventana, justify="center" ,textvariable=mC)
lbl_MC.grid(row = 12, column = 2)
caj_MC.grid(row = 13, column = 2)

lbl_MK = tkinter.Label(ventana, text=" MK : ")
caj_MK = tkinter.Entry(ventana, justify="center" ,textvariable=mK)
lbl_MK.grid(row = 14, column = 2)
caj_MK.grid(row = 15, column = 2)

btn_S = tkinter.Button(ventana, text="Tamaños", command=tms)
btn_S.grid(row=14, column=3)





ventana.mainloop()