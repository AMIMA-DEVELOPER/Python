from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('DEMONINATION COUNTER')
root.configure(bg= 'dark blue')
root.geometry('650x400')


label1 = Label(root,
               text="HEY USER! WELCOME TP THE COUNTER APP",
               bg='Light blue')
label1.place(relx=0.5, y=340, anchor=CENTER)

def msg():
    MsgBox = messagebox.showinfo(
        "ALERT", "DO U WANT TO CALCULATE THE COUNT")
    if MsgBox == 'ok':
        topwin()

btn1 = Button(root,text="LET'S GO", command=msg,bg='violet',fg='white')
btn1.place(x=260, y=360)

def topwin():
    top = Toplevel()
    top.title("demoniation calculator")
    top.configure(bg='black')
    top.geometry("600x350+50+50")

    label = Label(top,text="ENTER THE AMOUNT", bg='violet')
    entry = Entry(top)
    lbl = Label(top,text="HERE ARE THE NO.S FOR EACH DENOMINATION", bg='violet')

    l1 = Label(top,text="500", bg='light blue')
    l2 = Label(top,text="200", bg='light blue')
    l3 = Label(top,text="100", bg='light blue')
    l4 = Label(top,text="50", bg='light blue')

    t1 = Entry(top)
    t2 = Entry(top)
    t3 = Entry(top)
    t4 = Entry(top)

    def calculator():
        try:
            global amount
            amount = int(entry.get())
            note500 = amount // 500
            amount %= 500
            note200 = amount // 200
            amount %= 200
            note100 = amount // 100
            amount %= 100
            note50 = amount // 50
            amount %= 50


            t1.delete(0,END)
            t2.delete(0,END)
            t3.delete(0,END)
            t4.delete(0,END)

            t1.insert(END, str(note500))
            t2.insert(END, str(note200))
            t3.insert(END, str(note100))
            t4.insert(END, str(note50))
        except ValueError:
            messagebox.showerror("ERROR","PLEASE ENTER A NUMBER")

    btn = Button(top, text='CALCULATE', command=
                 calculator, bg='grey', fg='white')

    label.place(x=230, y=50)
    entry.place(x=200, y=80)
    btn.place(x=240, y=120)
    lbl.place(x=140, y=170)
    

    l1.place(x=180, y=200)
    l2.place(x=180, y=230)
    l3.place(x=180, y=260)
    l4.place(x=180, y=290)


    t1.place(x=270, y=200)
    t2.place(x=270, y=230)
    t3.place(x=270, y=260)
    t4.place(x=270, y=290)
    top.mainloop()
root.mainloop()