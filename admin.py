import tkinter as tk
from tkinter import messagebox

def login():
    username = entry_user.get()

    password = entry_pass.get()

    if username == "" or password == "":
        messagebox.showwarning("warning","Fields cannot be empty")

    elif username == "happy" and password == "123":
        messagebox.showinfo("success", "Login successful!")

    else:
        retry = messagebox.askretrycancel("ERROR!", "WRONG USERNAME OR PASSWORD. Retry?")
        if not retry:
            root.destroy()

root= tk.Tk()
root.title("Login System")

tk.Label(root, text="Username: ").pack()
entry_user = tk.Entry(root)
entry_user.pack()

tk.Label(root, text="Password: ").pack()
entry_pass = tk.Entry(root, show=".")
entry_pass.pack()

tk.Button(root, text="LOGIN", command=login).pack()

root.mainloop()