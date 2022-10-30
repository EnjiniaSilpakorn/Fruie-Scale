
from tkinter import *
from tkinter import ttk,messagebox

GUI=Tk()
GUI.title('Program fruit price calculator')
GUI.geometry('700x500')

bg=PhotoImage(file='Fruit.png')
BG=Label(GUI,image=bg)
BG.pack()

L0=Label(GUI,text='กรุณาใส่หมายเลขเลือกชนิดผลไม้',font=(None,15))
L1=Label(GUI,text='1            Mango',font=(None,8))
L2=Label(GUI,text='2   Mangosteen',font=(None,8))
L3=Label(GUI,text='3           Banana',font=(None,8))
L4=Label(GUI,text='4           Orenge',font=(None,8))
L5=Label(GUI,text='5             Apple',font=(None,8))
L6=Label(GUI,text='6             Grape',font=(None,8))
L7=Label(GUI,text='7       Pineapple',font=(None,8))
L8=Label(GUI,text='8     Persimmon',font=(None,8))
L9=Label(GUI,text='9          Papaya',font=(None,8))
L0.pack()
L1.pack()
L2.pack()
L3.pack()
L4.pack()
L5.pack()
L6.pack()
L7.pack()
L8.pack()
L9.pack()

Typefruit={'1':'Mango','2':'Mangosteen','3':'Banana','4':'Orenge','5':'Apple','6':'Grape','7':'Pineapple','8':'Persimmon','9':'Papaya'}

A=StringVar()
E0=ttk.Entry(GUI,textvariable=A,font=(None,15))
E0.pack()

L10=Label(GUI,text='กรุณาใส่น้ำหนักผลไม้',font=(None,15))
L10.pack()

v_quantity=StringVar()
E1=ttk.Entry(GUI,textvariable=v_quantity,font=(None,15))
E1.pack()

def Cal():
    F=float(A.get())
    if (F==1):
        price = 45   
    elif (F==2):
        price = 35  
    elif (F==3):
        price = 60 
    elif (F==4):
        price = 55 
    elif (F==5):
        price = 99  
    elif (F==6):
        price = 100  
    elif (F==7):
        price = 33
    elif (F==8):
        price = 120
    elif (F==9):
        price = 15
    else:
        price = 0

    try:
        quan=float(v_quantity.get())
        calc=quan*price
        messagebox.showinfo('ราคาทั้งหมด','Sale Price {} Bath'.format(calc))
        
        v_quantity.set('')
        E1.focus()

    except:
        messagebox.showwarning('กรอกผิด','กรอกเฉพาะตัวเลข')
        v_quantity.set('')
        E1.focus()
B=ttk.Button(GUI,text='คำนวณ',command=Cal)
B.pack(ipadx=20,ipady=15)







GUI.mainloop()
