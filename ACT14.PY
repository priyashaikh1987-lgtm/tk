import tkinter as tk
from tkinter import messagebox
def password_check():
    password = password_entry.get()
    letter = 0
    digit = 0
    special = 0
    for char in password:
        if char.isalpha():
            letter += 1
        elif char.isdigit():
            digit += 1
        else:
            special += 1
    total = letter + digit + special
    if total <= 5:
        messagebox.showinfo("Password Strength", "Weak Password")
        cube.config(bg="red")
    elif total >=6 and total <= 8:
        messagebox.showinfo("Password Strength", "Moderate Password")
        cube.config(bg="yellow")
    elif total > 8 and total < 12:
        messagebox.showinfo("Password Strength", "Strong Password")
        cube.config(bg="light green")
    else:
        messagebox.showinfo("Password Strength", "Very Strong Password")
        cube.config(bg="green")
window = tk.Tk()
window.title("Password Strength Checker")
window.geometry("400x400")
password_entry = tk.Entry(window, show="*")
password_entry.pack(pady=10)
tk.Button(window,text="Check Password Strength",command=password_check).pack(pady=20)
cube = tk.Frame(window,width=20,height=20,bg="white")
cube.pack(padx=10,pady=10)
window.mainloop()