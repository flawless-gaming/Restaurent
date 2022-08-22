from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
from time import strftime


root=Tk()
root.title('BARATIE')
# root.iconbitmap('baratielogo2.ico')
root.geometry('250x250')


def select1():
    selected=clicked.get()
    lb=Label(root,text=selected).grid(row=0,column=2,columnspan=2)
    if selected == 'Lunch & Dinner':
        root.geometry('600x250')
#         img_1=ImageTk.PhotoImage(Image.open('Food_1'))
#         l1=Label(Image=img_1).grid(row=0,column=0)
        b1=Button(orderbox1,text='Blessing of East Blue').grid(row=1,column=2)
#         img_2=ImageTk.PhotoImage(Image.open('Food_2'))
#         l2=Label(Image=img_2).grid(row=0,column=0)
        b2=Button(orderbox1,text='The vow with Shanks').grid(row=1,column=3)
#         img_3=ImageTk.PhotoImage(Image.open('Food_3'))
#         l3=Label(Image=img_3).grid(row=0,column=0)
        b3=Button(orderbox1,text='Absolute Justice').grid(row=2,column=2)
#         img_4=ImageTk.PhotoImage(Image.open('Food_4'))
#         l4=Label(Image=img_4).grid(row=0,column=0)
        b4=Button(orderbox1,text='Kids Food').grid(row=2,column=3)
#         img_5=ImageTk.PhotoImage(Image.open('Food_5'))
#         l5=Label(Image=img_5).grid(row=0,column=0)
        b5=Button(orderbox1,text='Honorable Liar').grid(row=3,column=2)
#         img_6=ImageTk.PhotoImage(Image.open('Food_6'))
#         l6=Label(Image=img_6).grid(row=0,column=0)
        b6=Button(orderbox1,text='The Fighting Cook').grid(row=3,column=3)
#         img_7=ImageTk.PhotoImage(Image.open('Food_7'))
#         l7=Label(Image=img_7).grid(row=0,column=0)
        b7=Button(orderbox1,text='Strong Man').grid(row=4,column=2)
#         img_8=ImageTk.PhotoImage(Image.open('Food_8'))
#         l8=Label(Image=img_8).grid(row=0,column=0)
        b8=Button(orderbox1,text='Courage to Conviction').grid(row=4,column=3)
#         img_9=ImageTk.PhotoImage(Image.open('Food_9'))
#         l9=Label(Image=img_9).grid(row=0,column=0)
        b9=Button(orderbox1,text='Freedom from Control').grid(row=5,column=2,columnspan=2)
        
    if selected == 'Dessert':
#         img_10=ImageTk.PhotoImage(Image.open('Red Nose Great Adventure'))
#         l10=Label(Image=img_10).grid(row=0,column=0)
        b10=Button(root,text="Red Nose's Great Adventure").grid(row=0,column=0)
#         img_11=ImageTk.PhotoImage(Image.open('Beautiful Lady'))
#         l11=Label(Image=img_11).grid(row=0,column=0)
        b11=Button(root,text='Beautiful Lady').grid(row=0,column=0)
#         img_12=ImageTk.PhotoImage(Image.open("A Gentleman's Taste"))
#         l12=Label(Image=img_12).grid(row=0,column=0)
        b12=Button(root,text="A Gentleman's Taste").grid(row=0,column=0)
#         img_13=ImageTk.PhotoImage(Image.open("Spark's Fall"))
#         l13=Label(Image=img_13).grid(row=0,column=0)
        b13=Button(root,text="Spark's Fall").grid(row=0,column=0)
#         img_14=ImageTk.PhotoImage(Image.open("Nami's Orange Jelly"))
#         l14=Label(Image=img_14).grid(row=0,column=0)
        b14=Button(root,text="Nami's Orange Jelly").grid(row=0,column=0) 
    if selected == 'Drinks':
#         img_15=ImageTk.PhotoImage(Image.open("Berry Berry Squash"))
#         l15=Label(Image=img_15).grid(row=0,column=0)
        b15=Button(root,text='Berry Berry Squash').grid(row=0,column=0)
#         img_16=ImageTk.PhotoImage(Image.open('Kiwi Lassi'))
#         l16=Label(Image=img_16).grid(row=0,column=0)
        b16=Button(root,text='Kiwi Lassi').grid(row=0,column=0)
#         img_17=ImageTk.PhotoImage(Image.open('Blue Ocean'))
#         l17=Label(Image=img_17).grid(row=0,column=0)
        b17=Button(root,text='Blue Ocean').grid(row=0,column=0)
#         img_18=ImageTk.PhotoImage(Image.open("Bellemere's Orange Juice"))
#         l18=Label(Image=img_18).grid(row=0,column=0)
        b18=Button(root,text="Bellemere's Orange Juice").grid(row=0,column=0)
#         img_19=ImageTk.PhotoImage(Image.open('Lime Juice'))
#         l19=Label(Image=img_19).grid(row=0,column=0)
        b19=Button(root,text='Lime Juice').grid(row=0,column=0)
    if selected == 'Alcoholic Drinks':
        
#         img_20=ImageTk.PhotoImage(Image.open('Going Merry'))
#         l20=Label(Image=img_20).grid(row=0,column=0)
        b20=Button(orderbox2,text="Going Merry").grid(row=0,column=0)
#         img_21=ImageTk.PhotoImage(Image.open('Red Eye'))
#         l21=Label(Image=img_21).grid(row=0,column=0)
        b21=Button(orderbox2,text="Red Eye").grid(row=0,column=1)
    elif selected=='0':
        error=messagebox.showerror('BARATIE','Selection Error')
#order
def order():
    global clicked
    options=[
        'Lunch & Dinner',
        'Dessert',
        'Drinks',
        'Alcoholic Drinks'
        ]
    clicked=StringVar()
    clicked.set('0')
    
    select=OptionMenu(root,clicked,*options)
    select.grid(row=0,column=1)
    
    btn=Button(root,text='Select',command=select1).grid(row=1,column=1)
    
#cancel
def pop():
    Label(root,text='boom!').grid(row=0,column=1)

frame1=LabelFrame(root,bg='#CDCD81',padx=30,pady=10)
frame1.grid(row=0,column=0)

frame2=LabelFrame(root,bg='#CDCD81',padx=25,pady=10)
frame2.grid(row=2,column=0)

frame3=LabelFrame(root,bg='#CDCD81',padx=33,pady=10)
frame3.grid(row=3,column=0)

frame4=LabelFrame(root,bg='#CDCD81',padx=37,pady=10)
frame4.grid(row=4,column=0)

frame5=LabelFrame(root,bg='#CDCD81',padx=31,pady=10)
frame5.grid(row=1,column=0)

orderbox1=LabelFrame(root,bg='#CDCD81',padx=31,pady=10)
orderbox1.grid(row=1,column=2,rowspan=4)

orderbox2=LabelFrame(root,bg='#CDCD81',padx=31,pady=10)
orderbox2.grid(row=1,column=2,rowspan=4)

Button(frame1,text='ORDER',command=order).pack()
Button(frame2,text='CANCEL',command=pop).pack()
Button(frame3,text='CART',command=pop).pack()
Button(frame4,text='EXIT',command=lambda:root.destroy()).pack()
Button(frame5,text='MENU',command=pop).pack()


root.mainloop()
