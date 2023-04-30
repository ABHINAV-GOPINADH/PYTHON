from tkinter import *
import random

ro=0
pa=1
sc=2
d="DRAW"
l="LOOSE"
w="WIN"
def r():
    n=random.randint(0,3)
    if(n==ro):
        print("DRAW")
    elif(n==pa):
        print("LOOSE")
    else:
        print("WIN")
rps=Tk()
rps.geometry("340x400")
comp=Label(rps,text="COMPUTER :").place(x=20,y=20)
you=Label(rps,text="YOU        :").place(x=200,y=20)
e1=Entry(rps,width=10).place(x=100,y=20,)
e2=Entry(rps,width=10).place(x=240,y=20)
b1=Button(rps,text="ROCK",command=r,width=10,height=3).place(x=21,y=60)
b2=Button(rps,text="PAPER",width=10,height=3).place(x=121,y=60)
b3=Button(rps,text="SCISSOR",width=10,height=3).place(x=221,y=60)
e3=Entry(rps,width=10).place(x=120,y=150)
rps.mainloop()