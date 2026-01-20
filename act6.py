from tkinter import * 
from tkinter import messagebox
window = Tk()
window.geometry("5000x5000")
window.title("message box")
def waring_message():
    messagebox.showwarning("alert","stop virus found")
button = Button(window,text="Scan For Virus",command=waring_message)
button.place(x=40,y=80)
window.mainloop()