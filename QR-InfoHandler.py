from tkinter import *
import pyqrcode
from pyzbar.pyzbar import decode
from PIL import Image
import os
import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar
scr=Tk()
scr.configure(bg="#BCC6CC")
scr.title("QR Handler")
canvas = Canvas(width=2000,height=2000)
canvas.pack()
photo = PhotoImage(file='C:\\Users\\hp\\Desktop\\Python Projects\\tkinter projects\\Logo2.png')
canvas.create_image(620,350,image=photo ,anchor=NW)
logo="Airports" + "\n" + "Authority" + "\n" + "of India"
      
l=Label(scr,text="CREATE QR-CODE",bg="Red",fg="black",font=('time','40','bold'))
l.place(x=70,y=20)
l1=Label(scr,text="Enter S/N",bg="blue",fg="black",font=('time','20','bold'))
l1.place(x=5,y=150)
l2=Label(scr,text="Enter Details",bg="blue",fg="black",font=('time','20','bold'))
l2.place(x=5,y=280)
e=Entry(scr,bg="white",fg="black",font=('Time','20','bold'))
e.place(x=250,y=150)
text=Text(scr,width=20,height=8,wrap=WORD,font=('Time','20','bold'),selectbackground="grey")
text.place(x=250,y=280)
b=Button(scr,text="CreateQR",bg="red",fg="black",font=('Time','20','bold'),command=lambda:createqr())
b.place(x=150,y=600)
l3=Label(scr,text="READ QR-CODE",bg="Red",fg="black",font=('time','40','bold'))
l3.place(x=900,y=20)
l4=Label(scr,text="Enter S/N",bg="blue",fg="black",font=('time','20','bold'))
l4.place(x=900,y=150)
e1=Entry(scr,bg="white",fg="black",font=('Time','20','bold'))
e1.place(x=1100,y=150)
b2=Button(scr,text="ReadQR",bg="green",fg="black",font=('Time','20','bold'),command=lambda:readqr())
b2.place(x=1050,y=250)
l5=Label(scr,text="UPDATE QR-CODE",bg="Red",fg="black",font=('time','40','bold'))
l5.place(x=900,y=400)
l6=Label(scr,text="Enter S/N",bg="blue",fg="black",font=('time','20','bold'))
l6.place(x=900,y=550)
l7=Label(scr,text="Add Details",bg="blue",fg="black",font=('time','20','bold'))
l7.place(x=900,y=650)
e2=Entry(scr,bg="white",fg="black",font=('Time','20','bold'))
e2.place(x=1100,y=550)
text1=Text(scr,width=20,height=4,wrap=WORD,font=('Time','20','bold'),selectbackground="grey")
text1.place(x=1100,y=620)
b3=Button(scr,text="Update",bg="yellow",fg="black",font=('Time','20','bold'),command=lambda:update())
b3.place(x=1408,y=695)
ls=Label(scr,text=logo,bg="green",fg="black",font=('time','40','bold'))
ls.place(x=600,y=20)
def createqr():
    a=e.get()
    b=a+".png"
    c=text.get(0.0,"end")
    d=a+"\n"+c
    qr=pyqrcode.create(d)
    qr.png(b,scale=8)


def readqr():
    a=e1.get()
    b=a+".png"
    d=decode(Image.open(b))
    c=d[0].data.decode('ascii')
    l=Label(scr,text=c,bg="white",fg="black",font=('time','15','bold'))
    l.place(x=1220,y=200)        
def update():
    a=e2.get()
    b=a+".png"
    d=decode(Image.open(b))
    c=d[0].data.decode('ascii')
    e=text1.get(0.0,"end")
    update=c+e
    os.remove(b)
    qr=pyqrcode.create(update)
    qr.png(b,scale=8)
