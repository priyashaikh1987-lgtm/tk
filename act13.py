import tkinter as tk
from tkinter import messagebox

def calculate_interest():
    try:
        principal = float(principal_entry.get())
        rate = float(rate_entry.get())
        time = float(time_entry.get())

        # Simple Interest
        simple_interest = (principal * rate * time) / 100

        # Compound Interest
        compound_amount = principal * (1 + rate/100) ** time
        compound_interest = compound_amount - principal

        # Display results
        si_result_label.config(text=f"Simple Interest: {simple_interest:.2f}")
        ci_result_label.config(text=f"Compound Interest: {compound_interest:.2f}")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values.")

# Main window
root = tk.Tk()
root.title("Interest Calculator")
root.geometry("350x300")

# Labels and input fields
tk.Label(root, text="Principal Amount:").pack()
principal_entry = tk.Entry(root)
principal_entry.pack()

tk.Label(root, text="Rate of Interest (%):").pack()
rate_entry = tk.Entry(root)
rate_entry.pack()

tk.Label(root, text="Time Period (years):").pack()
time_entry = tk.Entry(root)
time_entry.pack()

# Calculate button
tk.Button(root, text="Calculate", command=calculate_interest).pack(pady=10)

# Result labels
si_result_label = tk.Label(root, text="Simple Interest: ")
si_result_label.pack()

ci_result_label = tk.Label(root, text="Compound Interest: ")
ci_result_label.pack()

root.mainloop()