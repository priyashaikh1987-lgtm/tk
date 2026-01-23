import tkinter as tk
from tkinter import messagebox
from datetime import date

def calculate_age():
    try:
        day = int(day_entry.get())
        month = int(month_entry.get())
        year = int(year_entry.get())

        birthday = date(year, month, day)
        today = date.today()

        age = today.year - birthday.year

        
        if (today.month, today.day) < (birthday.month, birthday.day):
            age -= 1

        messagebox.showinfo("Age Result", f"The person is {age} years old.")

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers for day, month, and year.")


root = tk.Tk()
root.title("Age Calculator")

tk.Label(root, text="Day:").grid(row=0, column=0)
tk.Label(root, text="Month:").grid(row=1, column=0)
tk.Label(root, text="Year:").grid(row=2, column=0)

day_entry = tk.Entry(root)
month_entry = tk.Entry(root)
year_entry = tk.Entry(root)

day_entry.grid(row=0, column=1)
month_entry.grid(row=1, column=1)
year_entry.grid(row=2, column=1)

calc_button = tk.Button(root, text="Calculate Age", command=calculate_age)
calc_button.grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()