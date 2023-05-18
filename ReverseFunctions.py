import tkinter as tk
import math
import Results as rs
import CorrespondenceFunction as cf

wdReverse = tk.Tk()
wdReverse.title("Funciones de Correspondencia")
wdReverse.geometry("650x500") #anchoXaltura

########################################################## Funciones
def first():
    varnnn.set( (float(varMP.get()) * 1024 * 8)/float(varbits.get()))
    varl.set(math.log2(float(varnnn.get())))
    varB.set(float(varnnn.get())/float(varblo.get()))
    rs.things(wdReverse, 5, 0, 7, "n:", "l:", "B:", "b:", "L:", "j:", "c:")
    second()

def second():
    principal = tk.StringVar()
    varc = tk.StringVar()

    if float(varMC.get()) > 100:
        principal.set( (float(varMC.get()) * 8)/float(varbits.get()))
        varLL.set(float(principal.get())/float(varblo.get()))
        varc.set(float(varLL.get())/float(varCon.get()))
    else:
        principal.set( (float(varMC.get()) * 1024 * 8)/float(varbits.get()))
        varLL.set(float(principal.get())/float(varblo.get()))
        varc.set(float(varLL.get())/float(varCon.get()))

    rs.thingsResu(wdReverse,6,0,7, varbits, varl, varB, varblo, varLL, varCon, varc)
    asociativa()

def asociativa():
    a1 = tk.StringVar()
    a2 = tk.StringVar()

    a1.set(math.log2(float(varB.get())))
    a2.set(math.log2(float(varblo.get())))
    
    rs.space(wdReverse,4,3)
    rs.createA(wdReverse,5,3,"Asociativa", varl, 2, a1, a2)
    directa()

def directa():
    dP = tk.StringVar()
    dL = tk.StringVar()
    divE = tk.StringVar()
    dE = tk.StringVar()

    dP.set(math.log2(float(varblo.get())))
    dL.set(math.log2(float(varLL.get())))
    divE.set( float(varB.get()) / float(varLL.get()) )
    dE.set(math.log2(float(divE.get())))
    
    rs.space(wdReverse,9,3)
    rs.createDC(wdReverse,10,3,"Directa", varl, 3, dE, dL, dP)
    conjuntos()

def conjuntos():
    cP = tk.StringVar()
    Cv = tk.StringVar()
    cC = tk.StringVar()
    cE1 = tk.StringVar()
    cE2 = tk.StringVar()

    cP.set(math.log2(float(varblo.get())))
    Cv.set( float(varLL.get()) / float(varCon.get()) )
    cC.set(math.log2(float(Cv.get())))
    cE1.set( float(varB.get()) / float(Cv.get()) )
    cE2.set(math.log2(float(cE1.get())))

    rs.space(wdReverse,14,3)
    rs.createDC(wdReverse,15,3,"Conjuntos", varl, 3, cE2, cC, cP)

########################################################## Variables
varbits = tk.StringVar()
varMP = tk.StringVar()
varblo = tk.StringVar()
varMC = tk.StringVar()
varCon = tk.StringVar()

#Variables para las funciones
varnnn = tk.StringVar()
varl = tk.StringVar()
varB = tk.StringVar()
varLL = tk.StringVar()

########################################################## Memoria Principal

lbl_title = tk.Label(wdReverse, text="Memoria Principal")
lbl_n = tk.Label(wdReverse, text="Celdas n-bits")
caj_n = tk.Entry(wdReverse, textvariable=varbits)

lbl_L = tk.Label(wdReverse, text="MP en KB")
caj_L = tk.Entry(wdReverse , textvariable=varMP) 

lbl_b = tk.Label(wdReverse, text="Bloques n-palabras")
caj_b = tk.Entry(wdReverse, textvariable=varblo)#textvariable = "Nombre de la variable"


lbl_title.grid(row = 0, column = 0)
lbl_n.grid(row = 1, column = 0)
caj_n.grid(row = 1, column = 1)
lbl_L.grid(row = 2, column = 0)
caj_L.grid(row = 2, column = 1)
lbl_b.grid(row = 3, column = 0)
caj_b.grid(row = 3, column = 1)

########################################################## Memoria Cache
lb_title2 = tk.Label(wdReverse, text="Memoria Cache")

lb_MC = tk.Label(wdReverse, text="MC en KB")
caj_MC = tk.Entry(wdReverse, textvariable=varMC)
lb_Conj = tk.Label(wdReverse, text="Conjuntos j-vias")
caj_Conj = tk.Entry(wdReverse, textvariable=varCon)

lb_title2.grid(row = 0, column = 3)
lb_MC.grid(row = 1, column = 3)
caj_MC.grid(row = 1, column = 4)
lb_Conj.grid(row = 2, column = 3)
caj_Conj.grid(row = 2, column = 4)

########################################################## Botones

btn_S = tk.Button(wdReverse, text="Tamaños", command=first)
btn_S.grid(row=3, column=5)

wdReverse.mainloop()