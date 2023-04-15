def memory(ventana, titulo, r, c, n_objetos, *text):
    import tkinter
    
    lbl = tkinter.Label(ventana, text=titulo)
    lbl.grid(row = r, column = c)
    for i in range(n_objetos):
        r = r+1
        lab_txtbox_n(ventana,text[i], r, c)


# def main_memory(ventana):
#     import tkinter

#     lbl_mP = tkinter.Label(ventana, text="Memoria Principal")
#     lbl_mP.grid(row = 1, column = 0)

#     lab_txtbox_n(ventana,"Celdas n-bits", 2, 0)
#     lab_txtbox_n(ventana,"Direcciones lambda-bits", 3, 0)
#     lab_txtbox_n(ventana,"Bloques b-celda", 4, 0)

def lab_txtbox_n(ventana, txt_lbl, r, c):
    import tkinter
    #Creación del label con el texto de argumento y textBox
    lbl = tkinter.Label(ventana, text=txt_lbl)
    caja = tkinter.Entry(ventana)
    #Ubicaciones con argumentos un lado al otro
    lbl.grid(row=r, column=c)
    caja.grid(row=r, column=c+1)


