from tkinter import *
from datetime import date

window = Tk()
window.title('password')
window.geometry('400x400')

frame = Frame(master=window, height=200, width=360, bg="#d0efff")

lbl1 = Label(frame, text = "FULL NAME", bg="black", fg="white", width=12)

lbl2 = Label(frame, text = "EMAIL ID", bg="white", fg="black", width=12)

lbl3 = Label(frame, text = "ENTER PASSWORD", bg="black", fg="white", width=12)

name_entry = Entry(frame)
email_entry = Entry(frame)
pass_entry = Entry(frame, show="*")

def display():
    name = name_entry.get()

    greet = "HELLO " + name
    Message= "\nCONGRATULATIONS FOR YOUR NEW ACCOUNT :)"
    textbox.insert(END, greet)
    textbox.insert(END, Message)

textbox = Text(bg= "#6B0E0E",fg="white" )

btn = Button(text= "CREATE", command = display, bg="black", fg="white")

frame.place(x=20,y=0)
lbl1.place(x=20,y=20)
name_entry.place(x=150,y=20)
lbl2.place(x=20,y=80)
email_entry.place(x=150,y=80)
lbl3.place(x=20,y=140)
pass_entry.place(x=150,y=140)
btn.place(x=130,y=210)
textbox.place(y=250)

window.mainloop()
