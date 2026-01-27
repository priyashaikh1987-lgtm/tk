from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
window = Tk()
window.title("codingal text editor") 
window.geometry("600x500")
window.rowconfigure(0,minsize=800,weight=1)
window.columnconfigure(1,minsize=800,weight=1)
def openfile():
    file_path = askopenfilename(filetypes=[("text files","*.txt"),("all files","*.*")])
    if not file_path:
        return 
    text_edit.delete(1.0,END)
    with open(file_path,"r")as inputfile:
        text = inputfile.read()
        text_edit.insert(END,text)
        inputfile.close()
    window.title(f"codingal text editor {file_path}")
def savefile():
    file_path = asksaveasfilename(defaultextension="txt",filetypes=[("text files","*.txt"),("all files","*.*")])
    if not file_path:
        return
    with open(file_path,"w")as outputfile:
        text = text_edit.get(1.0,END)
        outputfile.write(text)
        window.title(f"codingal text editor {file_path}")
text_edit = Text(window)
button1 = Frame(window,relief=RAISED,bd=2)
buttonopen = Button(button1,text="open",command=openfile)
buttonsave = Button(button1,text="save as",command=savefile)
buttonopen.grid(row=0,column=0,sticky="ew",padx=5,pady=5)
buttonsave.grid(row=1,column=0,sticky="ew",padx=5)
button1.grid(row=0,column=0,sticky="ns")
text_edit.grid(row=0,column=1,sticky="nsew")
window.mainloop()