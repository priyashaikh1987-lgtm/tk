import tkinter as dk
def intcm():
    try:
        inches = float(entry_in.get())
        cm = inches * 2.54
        rl.config(text=f"{cm:.2f} cm")
    except ValueError:
        rl.config(text="Please enter a valid number.")
window = dk.Tk()
window.title("length converter app")
window.geometry("400x400")
entry_in = dk.Entry(window,width = 40)
entry_in.grid(row=0,column=1,padx=10,pady=10)
dk.Label(window,text="inches").grid(row=0,column=0)
cb = dk.Button(window,text="convert to cm",command=intcm)
cb.grid(row=1,column=0,padx=2,pady=10)
rl = dk.Label(window,text="")
rl.grid(row=2,column=0,columnspan=2)
window.mainloop()