from tkinter import *
from datetime import date

window = Tk()

window.title('demo window')
window.geometry('400x300')

lb = Label(text="HEY THERE", fg ="Black", bg="#FFFFFF", height=1, width= 300)

name_lb = Label(text="full name", bg="#DC143C")
name_entry = Entry()

def display():
    name = name_entry.get()
    global Message
    Message = "WELSOME TO THE APPLICATION! \n Today's date is:  "
    greet = "hello  "   +name+ "\n"

    text_box.insert(END, greet)
    text_box.insert(END, Message)
    text_box.insert(END, date.today())

text_box = Text(height=3)

btn = Button(text="start", command=display, height=1, bg="#2C0886", fg="crimson")

lb.pack()
name_lb.pack()
name_entry.pack()
btn.pack()
text_box.pack()

window.mainloop()