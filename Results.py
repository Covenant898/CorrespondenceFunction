def things(ventana, r, c, n, *text):
    import tkinter as tk

    #creacion de n labels
    for i in range (n):
        r = r+2
        lb_th = tk.Label(ventana, text=text[i])
        lb_th.grid(row=r, column=c)

def space(ventana,r,c):
    import tkinter as tk
    lb_rr = tk.Label(ventana, text="")
    lb_rr.grid(row=r,column=c)

def thingsResu(ventana,r,c,n,*text):
    import tkinter as tk
    for i in range(n):
        r=r+2
        lb_rr = tk.Label(ventana, text=format(float(text[i].get())), fg='red' )
        lb_rr.grid(row=r,column=c)

def createDC(ventana,r,c,titulo,variable,n,*text):
    import tkinter as tk
    lb_titulo = tk.Label(ventana, text=titulo, fg='brown')
    lb_titulo.grid(row=r,column=c)
    lb_bits1 = tk.Label(ventana, text=format(float(variable.get())))
    lb_bits1.grid(row=r+1,column=c)
    lb_bits = tk.Label(ventana, text="bits")
    lb_bits.grid(row=r+1,column=c+1)
    lb_bits = tk.Label(ventana, text="Etiqueta")
    lb_bits.grid(row=r+2,column=c)
    lb_bits = tk.Label(ventana, text="Linea")
    lb_bits.grid(row=r+2,column=c+1)
    lb_bits = tk.Label(ventana, text="Palabra")
    lb_bits.grid(row=r+2,column=c+2)
    r = r + 3
    for i in range(n):
        lb_rr = tk.Label(ventana, text=format(float(text[i].get())), fg='blue' )
        lb_rr.grid(row=r,column=c)
        c = c + 1

def createA(ventana,r,c,titulo,variable,n,*text):
    import tkinter as tk
    lb_titulo = tk.Label(ventana, text=titulo, fg='brown')
    lb_titulo.grid(row=r,column=c)
    lb_bits1 = tk.Label(ventana, text=format(float(variable.get())))
    lb_bits1.grid(row=r+1,column=c)
    lb_bits = tk.Label(ventana, text="bits")
    lb_bits.grid(row=r+1,column=c+1)
    lb_bits = tk.Label(ventana, text="Etiqueta")
    lb_bits.grid(row=r+2,column=c)
    lb_bits = tk.Label(ventana, text="Palabra")
    lb_bits.grid(row=r+2,column=c+1)
    r = r + 3
    for i in range(n):
        lb_rr = tk.Label(ventana, text=format(float(text[i].get())), fg='blue' )
        lb_rr.grid(row=r,column=c)
        c = c + 1