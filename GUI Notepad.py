# Importing modules.....
from tkinter import *
import tkinter.messagebox as tmsg
from tkinter.filedialog import askopenfilename, asksaveasfilename
from datetime import datetime
import os 

# Creating GUI window.... 
window = Tk()
window.geometry("700x450")
window.resizable(False, False)
window.title("Notepad - Created By Mohd.Tahil")
window.wm_iconbitmap("arc.ico.ico")

# Creating Satus bar......
status = StringVar()
status.set("Untitled - Notepad")
l0 = Label(window, textvariable=status, font="lucida 15 bold", relief=SUNKEN, anchor=NW)
l0.pack(side=BOTTOM, fill=X)

# Creating textarea and other logics....
file = None 

# Creating scroll  bar logic....
scroll = Scrollbar(window)
scroll.pack(fill=Y, side=RIGHT)
text_area = Text(window, font="lucida 20 bold", yscrollcommand=scroll.set)
text_area.pack() 
scroll.config(command=text_area.yview)

#Creating functions for notepad......
def new_file():
    global file
    text_area.delete(1.0, END)
    window.title(str(file) + " Untitled - Notepad")

def open_file():
    global file 

    file = askopenfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
    
    if file=="":
        file = None

    else:
        window.title(os.path.basename(file) + " - Notepad")
        text_area.delete(1.0, END)
        f = open(file, "r")
        text_area.insert(1.0, f.read())
        f.close()

def save_file():
    global file 
    
    if file==None:
        file = asksaveasfilename(initialfile="Untitled.txt", defaultextension=".txt", filetypes=[("All files", "*.*"), ("Text Documents", "*.txt")])

        if file=="":
            file = None 

        else:
            window.title(os.path.basename(file)+" - Notepad")
            f = open(file, "w")
            f.write(text_area.get(1.0, END))
            f.close()
    
    else:
        window.title(os.path.basename(file)+" - Notepad")
        f = open(file, "w")
        f.write(text_area.get())
        f.close()

def back():
    window.destroy()

def cut_txt():
    text_area.event_generate(("<<Cut>>"))

def copy_txt():
    text_area.event_generate(("<<Copy>>"))

def pst_txt():
    text_area.event_generate(("<<Paste>>"))

def dt():
    global status
    status.set(f"Date_Time - {datetime.now()}")

def rate():
    value = tmsg.askquestion("Rate us", "How is your Experinace, was your Experinace good..")

    if value=="yes":
        tmsg.showinfo("Good Experiance", "Please Ratu us on Google Play Store")

    else:
        tmsg.showinfo("Bad Expeiance", "Please Send us your Feedback About this platform our community will Solve your Problem Soon....")

def feed():
    text_area.delete(1.0, END)
    text_area.insert(INSERT, "Explain Briefly Whats Wrong With you..._: ")
    tmsg.showinfo("Note", "Please Post Your Problem in This File on our official Website(WWW.MTN.COM)")

# Creating the Main Menus.....
menu0 = Menu(window, font="lucida 20 bold")

# Creating the file menu.....
m0 = Menu(menu0, tearoff=0)
m0.add_command(label="New", command=new_file)
m0.add_command(label="Open", command=open_file)
m0.add_command(label="Save", command=save_file)
m0.add_separator()
m0.add_command(label="Exit", command=back)
menu0.add_cascade(label="File", menu=m0)

# Creating the Edit menu.......
m1 = Menu(menu0, tearoff=0)
m1.add_command(label="Cut", command=cut_txt)
m1.add_command(label="Copy", command=copy_txt)
m1.add_command(label="Paste", command=pst_txt)
m1.add_separator()
m1.add_command(label="Time/Date", command=dt)

menu0.add_cascade(label="Edit", menu=m1)

about_mn = Menu(menu0, tearoff=0)
about_mn.add_command(label="Rate us", command=rate)
about_mn.add_command(label="Feedback", command=feed)

menu0.add_cascade(label="About", menu=about_mn)
menu0.add_command(label="Exit", command=back)

window.config(menu=menu0)
# Closing the Window....
window.mainloop()