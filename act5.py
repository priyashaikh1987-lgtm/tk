from tkinter import *
window = Tk()
window.title("event handler")
window.geometry("500x500")
def handle_keypress(event):
    print(event.char)
window.bind("<Key>",handle_keypress)
def handle_click(event):
    print("\nthe button was clicked")
button = Button(text = "click me")
button.pack()
button.bind("<Button-1>",handle_click)
window.mainloop()