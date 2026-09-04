# from tkinter import*

# window = Tk()
# window.title("Event handler")
# window.geometry("100x100")

# def handle_keypress(event):
#     """Print the character associated to the key pressed """
#     print(event.char)

# window.bind("<Key>", handle_keypress)

# def handle_click(event):
#     print("\n The button was clicked")

# Button = Button(text="click me!")
# Button.pack()

# Button.bind("<Button-1>", handle_click)

# window.mainloop()




from tkinter import*
from tkinter import messagebox

root = Tk()
root.geometry("200x200")

def msg():
    #messagebox.showwarning("Alert","Stop! Virus found.")
    messagebox.askquestion("save","you want to save this file ")

Button = Button(root, text="Scan for Virus", command=msg)
Button.place(x=40 , y=80)

root.mainloop()