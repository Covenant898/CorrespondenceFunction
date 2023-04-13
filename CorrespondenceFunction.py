import math
import tkinter

ventana = tkinter.Tk()
ventana.title("Funcion de Correspondencia")
ventana.geometry("650x500") #anchoXaltura

etique = tkinter.Label(ventana, text="Ingrese Datos")
etique.grid(row = 0, column = 2)
lbl_mP = tkinter.Label(ventana, text="Memoria Principal")
lbl_mC = tkinter.Label(ventana, text="Memoria Cache")

########################################################## Funciones

def tms():
    varN.set( 2 ** float(varLam.get()) )
    varB.set( float(varN.get()) / float(varb.get()) )
    mP.set(      ((16*float(varN.get()))/8)/1024     )
    mC.set( float(varL.get()) *  float(varb.get()) )
    mK.set( ((16*float(mC.get()))/8)/1024   )

def log():
    a1.set(math.log2(float(varB.get())))
    a2.set(math.log2(float(varLam.get())))

    lbl_a1 = tkinter.Label(ventana, text=format(float(a1.get())),fg='blue' )
    lbl_a1.grid(row=10, column=2)
    lbl_a2 = tkinter.Label(ventana, text=format(float(a2.get())),fg='blue' )
    lbl_a2.grid(row=10, column=3)
    directa()

def directa():
    dP.set(math.log2(float(varb.get())))
    dL.set(math.log2(float(varL.get())))
    divE.set( float(varB.get()) / float(varL.get()) )
    dE.set(math.log2(float(divE.get())))

    lbl_d1 = tkinter.Label(ventana, text=format(float(dE.get())),fg='green' )
    lbl_d1.grid(row=15, column=2)
    lbl_d2 = tkinter.Label(ventana, text=format(float(dL.get())),fg='green' )
    lbl_d2.grid(row=15, column=3)
    lbl_d3 = tkinter.Label(ventana, text=format(float(dP.get())),fg='green' )
    lbl_d3.grid(row=15, column=4)
    conjuntos()

def conjuntos():
    cP.set(math.log2(float(varb.get())))
    Cv.set( float(varL.get()) / float(varJ.get()) )
    cC.set(math.log2(float(Cv.get())))
    cE1.set( float(varB.get()) / float(Cv.get()) )
    cE2.set(math.log2(float(cE1.get())))

    lbl_c1 = tkinter.Label(ventana, text=format(float(cP.get())),fg='brown' )
    lbl_c1.grid(row=20, column=4)
    lbl_c2 = tkinter.Label(ventana, text=format(float(cC.get())),fg='brown' )
    lbl_c2.grid(row=20, column=3)
    lbl_c3 = tkinter.Label(ventana, text=format(float(cE2.get())),fg='brown' )
    lbl_c3.grid(row=20, column=2)


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
varJ = tkinter.StringVar()

#loga = tkinter.StringVar()
msj = "bits"
a1 = tkinter.StringVar() 
a2 = tkinter.StringVar()

dP = tkinter.StringVar()
dL = tkinter.StringVar()
dE = tkinter.StringVar()
divE = tkinter.StringVar()

Cv = tkinter.StringVar()
cP = tkinter.StringVar()
cC = tkinter.StringVar()
cE1 = tkinter.StringVar()
cE2 = tkinter.StringVar()

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
caj_j = tkinter.Entry(ventana, textvariable=varJ)

lbl_mC.grid(row = 1, column = 3)
lbl_Lb.grid(row = 2, column = 3)
caj_Lb.grid(row = 2, column = 4)
lbl_j.grid(row = 3, column = 3)
caj_j.grid(row = 3, column = 4)


########################################################## Tamanos

space = tkinter.Label(ventana,text="")
space.grid(row = 5, column = 0)
space1 = tkinter.Label(ventana,text="")
space1.grid(row = 6, column = 0)

tama = tkinter.Label(ventana, text=" Tamaños ")
tama.grid(row = 7, column = 0)

lbl_N = tkinter.Label(ventana, text=" N : ")
caj_N = tkinter.Entry(ventana, justify="center" ,textvariable=varN)
lbl_N.grid(row = 8, column = 0)
caj_N.grid(row = 9, column = 0)

lbl_B = tkinter.Label(ventana, text=" B : ")
caj_B = tkinter.Entry(ventana, justify="center" ,textvariable=varB)
lbl_B.grid(row = 10, column = 0)
caj_B.grid(row = 11, column = 0)

lbl_MP = tkinter.Label(ventana, text=" MP : ")
caj_MP = tkinter.Entry(ventana, justify="center" ,textvariable=mP)
lbl_MP.grid(row = 12, column = 0)
caj_MP.grid(row = 13, column = 0)

lbl_MC = tkinter.Label(ventana, text=" MC : ")
caj_MC = tkinter.Entry(ventana, justify="center" ,textvariable=mC)
lbl_MC.grid(row = 14, column = 0)
caj_MC.grid(row = 15, column = 0)

lbl_MK = tkinter.Label(ventana, text=" MK : ")
caj_MK = tkinter.Entry(ventana, justify="center" ,textvariable=mK)
lbl_MK.grid(row = 16, column = 0)
caj_MK.grid(row = 17, column = 0)


########################################################## Asociativa

lbl_aso = tkinter.Label(ventana, text="Asociativa" ,fg="red")
lbl_aso.grid(row=7, column=2)
lbl_16 = tkinter.Label(ventana, text="16" )#format(float(varn.get()))
lbl_16.grid(row=8, column=2)
lbl_bts = tkinter.Label(ventana, text=msj )
lbl_bts.grid(row=8, column=3)
lbl_etique = tkinter.Label(ventana, text="Etiqueta" )
lbl_etique.grid(row=9, column=2)
lbl_word = tkinter.Label(ventana, text="Palabra" )
lbl_word.grid(row=9, column=3)

########################################################## Directa

space2 = tkinter.Label(ventana,text="")
space2.grid(row = 11, column = 2)

lbl_aso = tkinter.Label(ventana, text="Directa" ,fg="red")
lbl_aso.grid(row=12, column=2)
lbl_16 = tkinter.Label(ventana, text="16" )#format(float(varn.get()))
lbl_16.grid(row=13, column=2)
lbl_bts = tkinter.Label(ventana, text=msj )
lbl_bts.grid(row=13, column=3)
lbl_etique = tkinter.Label(ventana, text="Etiqueta" )
lbl_etique.grid(row=14, column=2)
lbl_word = tkinter.Label(ventana, text="Linea" )
lbl_word.grid(row=14, column=3)
lbl_word = tkinter.Label(ventana, text="Palabra" )
lbl_word.grid(row=14, column=4)

########################################################## Conjuntos

space3 = tkinter.Label(ventana,text="")
space3.grid(row = 16, column = 2)
lbl_aso = tkinter.Label(ventana, text="Conjuntos" ,fg="red")
lbl_aso.grid(row=17, column=2)

lbl_16 = tkinter.Label(ventana, text="16" )#format(float(varn.get()))
lbl_16.grid(row=18, column=2)
lbl_bts = tkinter.Label(ventana, text=msj )
lbl_bts.grid(row=18, column=3)
lbl_etique = tkinter.Label(ventana, text="Etiqueta" )
lbl_etique.grid(row=19, column=2)
lbl_word = tkinter.Label(ventana, text="Linea" )
lbl_word.grid(row=19, column=3)
lbl_word = tkinter.Label(ventana, text="Palabra" )
lbl_word.grid(row=19, column=4)

########################################################## Botones

btn_S = tkinter.Button(ventana, text="Tamaños", command=tms)
btn_S.grid(row=14, column=5)

btn_Log = tkinter.Button(ventana, text="Empezar", command=log)
btn_Log.grid(row=16, column=5)


ventana.mainloop()