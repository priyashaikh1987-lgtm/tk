from tkinter import *
window = Tk()
window.title("gettng started with widgets")
window.geometry("4000x3000")
lable1 = Label(text="Hey There",fg="white",bg="green",height=1,width=300)
lable2 = Label(text="full name",bg="orange")
nameentery = Entry()
def display():
    name = nameentery.get()
    global Message 
    Message = "WELCOME TO THE APCACTION"
    greet = "hello"
    textbox.insert(END,greet)
    textbox.insert(END,Message)
textbox = Text(height = 3)
button1 = Button(text="BEGIN",command=display,height=1,bg="purple",fg="white")
lable1.pack()
lable2.pack()
nameentery.pack()
button1.pack()
textbox.pack()
window.mainloop()