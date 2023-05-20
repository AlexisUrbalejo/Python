from tkinter import *

def suma():
    n1=int(num1.get())
    n2=int(num2.get())
    res.set(n1+n2)
    signo.set("+")
    
def resta():
    n1=int(num1.get())
    n2=int(num2.get())
    res.set(n1-n2)
    signo.set("-")
    
def multi():
    n1=int(num1.get())
    n2=int(num2.get())
    res.set(n1*n2)
    signo.set("*")

def div():
    n1=int(num1.get())
    n2=int(num2.get())
    res.set(n1/n2)
    signo.set("/")
    
    
ventana = Tk()
ventana.title("Calculadora  de operaciones basicas ")
ventana.geometry("450x275")

num1=StringVar()
num1.set("0")

num2=StringVar()
num2.set("0")

signo=StringVar()
signo.set(" ")

res=StringVar()
res.set("0")

cuadro1=LabelFrame(text='Operacion',fg="royalblue1",font=("Arial black", 10),relief="groove",bd=3,width=400,height=(72)).place(x=25,y=40)
tit1=Label(cuadro1,fg="royalblue1", text="Numero 1",font=("arial black",8)).place(x=57, y=59)
op=Label(cuadro1,font=("Arial", 22),textvariable=signo).place(x=144, y=67)
tit2=Label(cuadro1,fg="royalblue1", text="Numero 2:",font=("arial black",8)).place(x=197, y=59)
Label(cuadro1, text="=",font=("Arial", 22)).place(x=284, y=67)
tit3=Label(cuadro1,fg="royalblue1", text="Resultado:",font=("arial black",8)).place(x=335, y=59)

cuadro2=LabelFrame(text='Operadores Arimeticos',fg="royalblue1",font=("Arial black", 10),relief="groove",bd=3,width=400,height=(72)).place(x=25,y=151)
bsuma=Button(cuadro2,text='+',fg="navy",font=("Arial black", 10), width=8, command=suma).place(x=50,y=174)
bresta=Button(cuadro2,text='-',fg="navy",font=("Arial black", 10), width=8,command=resta).place(x=144,y=174)
bmulti=Button(cuadro2,text='*',fg="navy",font=("Arial black", 10), width=8,command=multi).place(x=236,y=174)
bdivi=Button(cuadro2,text='/',fg="navy",font=("Arial black", 10), width=8,command=div).place(x=330,y=174)

n1=Entry(cuadro1, width=15,textvariable=num1).place(x=41, y=75)
n2=Entry(cuadro1, width=15,textvariable=num2).place( x=181, y=75)
resul=Entry(cuadro1, width=15,textvariable=res).place( x=321, y=75)

Label(ventana, text="Alexis Urbalejo",fg="red4",font=("Arial", 8)).place(x=337, y=240)


ventana.mainloop()
