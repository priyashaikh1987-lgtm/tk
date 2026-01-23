from tkinter import *
import tkinter as tk
def multply_num():
    try:
        num1 = float(enter1.get())
        num2 = float(enter2.get())
        result = num1 * num2
        result_label.config(text=f"result: {result}")
    except ValueError:
        result_label.config(text="Please enter valid numbers")
window = Tk()
window.title("getting started with widgets")
window.geometry("400x300")
tk.Label(window, text="enter first number").pack()
enter1 = tk.Entry(window)
enter1.pack()
tk.Label(window, text="enter second number").pack()
enter2 = tk.Entry(window)
enter2.pack()
tk.Button(window, text="multply", command=multply_num).pack(pady=10)
result_label = tk.Label(window, text="result: ")
result_label.pack()
window.mainloop()