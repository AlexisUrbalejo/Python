from tkinter import *
from tkinter import ttk
import math

def ingval(tecla):
    if tecla >='0' and tecla<='9' or tecla =='(' or tecla == ')' or tecla =='.' :
        entrada2.set(entrada2.get() + tecla)
    if tecla == '*' or tecla == '/' or tecla == '+' or tecla=='-':
        if tecla == '*':
            entrada1.set(entrada2.get() + '*')
        elif tecla == '/':
            entrada1.set(entrada2.get() + '/')
        elif tecla == '+':
            entrada1.set(entrada2.get() + '+')
        elif tecla == '-':
            entrada1.set(entrada2.get() + '-')
        entrada2.set('')
    if tecla == '=':
        entrada1.set(entrada1.get() + entrada2.get())    
        resultado= eval(entrada1.get())
        entrada2.set(resultado)
def raiz():
    entrada1.set('')
    resultado = math.sqrt(float(entrada2.get()))
    entrada2.set(resultado)
    
def borrar(*args):
    inicio = 0
    final = len(entrada2.get())

    entrada2.set(entrada2.get()[inicio:final-1])


def borrar_todo():

    entrada1.set('')
    entrada2.set('')

def ingtec(event):
    tecla = event.char
    if tecla >='0' and tecla<='9' or tecla =='(' or tecla == ')' or tecla =='.' :
        entrada2.set(entrada2.get() + tecla)
    if tecla == '*' or tecla == '/' or tecla == '+' or tecla=='-':
        if tecla == '*':
            entrada1.set(entrada2.get() + '*')
        elif tecla == '/':
            entrada1.set(entrada2.get() + '/')
        elif tecla == '+':
            entrada1.set(entrada2.get() + '+')
        elif tecla == '-':
            entrada1.set(entrada2.get() + '-')
        entrada2.set('')
    if tecla == '=':
        entrada1.set(entrada1.get() + entrada2.get())    
        resultado= eval(entrada1.get())
        entrada2.set(resultado)


root = Tk()
root.title("Calculadora avanzada")
root.geometry("+500+80")
root.columnconfigure(0,weight=1)
root.rowconfigure(0,weight=1)

estilo = ttk.Style()
estilo.configure('mainframe.TFrame',background="#DBDBDB")

mainframe = ttk.Frame(root,style="mainframe.TFrame")
mainframe.grid(column=0,row=0,sticky=(W,N,E,S))
mainframe.columnconfigure(0,weight=1)
mainframe.columnconfigure(1,weight=1)
mainframe.columnconfigure(2,weight=1)
mainframe.columnconfigure(3,weight=1)


estilo_label1 = ttk.Style()
estilo_label1.configure('Label1.TLabel',font="arial 15",anchor="E")

mainframe = ttk.Frame(root)
mainframe.grid(column=0,row=0)



entrada1= StringVar()
label_entrada1 = ttk.Label(mainframe,textvariable=entrada1,style="Label1.TLabel")
label_entrada1.grid(column=0,row=0,columnspan=4,sticky=(W,E))

entrada2 = StringVar()
label_entrada2 = ttk.Label(mainframe,textvariable=entrada2)
label_entrada2.grid(column=0,row=1,columnspan=4,sticky=(W,E))

boton0 = ttk.Button(mainframe,text="0",command=lambda: ingval('0'))
boton1 = ttk.Button(mainframe,text="1",command=lambda: ingval('1'))
boton2 = ttk.Button(mainframe,text="2",command=lambda: ingval('2'))
boton3 = ttk.Button(mainframe,text="3",command=lambda: ingval('3'))
boton4 = ttk.Button(mainframe,text="4",command=lambda: ingval('4'))
boton5 = ttk.Button(mainframe,text="5",command=lambda: ingval('5'))
boton6 = ttk.Button(mainframe,text="6",command=lambda: ingval('6'))
boton7 = ttk.Button(mainframe,text="7",command=lambda: ingval('7'))
boton8 = ttk.Button(mainframe,text="8",command=lambda: ingval('8'))
boton9 = ttk.Button(mainframe,text="9",command=lambda: ingval('9'))

boton_borrar = ttk.Button(mainframe,text=chr(9003),command=lambda: borrar())
boton_par1 = ttk.Button(mainframe,text="(",command=lambda: ingval('('))
boton_par2 = ttk.Button(mainframe,text=")",command=lambda: ingval(')'))
boton_borrart = ttk.Button(mainframe,text="c",command=lambda: borrar_todo())
boton_punto = ttk.Button(mainframe,text=".",command=lambda: ingval('.'))

boton_divi = ttk.Button(mainframe,text=chr(247),command=lambda: ingval('/'))
boton_multi = ttk.Button(mainframe,text="*",command=lambda: ingval('*'))
boton_suma = ttk.Button(mainframe,text="+",command=lambda: ingval('+'))
boton_resta = ttk.Button(mainframe,text="-",command=lambda: ingval('-'))

boton_igual = ttk.Button(mainframe,text="=",command=lambda: ingval('='))
boton_raiz = ttk.Button(mainframe,text="√",command=lambda: raiz())

boton_par1.grid(column=0,row=2)
boton_par2.grid(column=1,row=2)
boton_borrart.grid(column=2,row=2)
boton_borrar.grid(column=3,row=2)

boton7.grid(column=0,row=3)
boton8.grid(column=1,row=3)
boton9.grid(column=2,row=3)
boton_divi.grid(column=3,row=3)

boton4.grid(column=0,row=4)
boton5.grid(column=1,row=4)
boton6.grid(column=2,row=4)
boton_multi.grid(column=3,row=4)

boton1.grid(column=0,row=5)
boton2.grid(column=1,row=5)
boton3.grid(column=2,row=5)
boton_suma.grid(column=3,row=5)

boton0.grid(column=0,row=6,columnspan=2,sticky=(W,E))
boton_punto.grid(column=2,row=6)
boton_resta.grid(column=3,row=6)

boton_igual.grid(column=0,row=7,columnspan=3,sticky=(W,E))
boton_raiz.grid(column=3,row=7)



root.bind('<Key>',ingtec)
root.bind('<KeyPress-b>',borrar)



root.mainloop()

