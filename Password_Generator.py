import tkinter as tk
from tkinter import messagebox
import random
import string
root=tk.Tk()

def generate_password():
    textfield2.delete(0,tk.END)
    if(textfield1.get()==''):
         messagebox.showinfo("Info","Enter the length of password")
    else:
        length=int(textfield1.get())
        complexity=variable.get()
        character=string.ascii_lowercase
        if(complexity=='low'):
            character+=string.ascii_uppercase
        elif(complexity=='medium'):
            character=string.digits+string.ascii_letters
        else:
            character+=string.punctuation+string.digits+string.ascii_letters
        if(length<12 or length>128):
            value=messagebox.askquestion("question","Minimum length of password is 12.\nMaximum length of password is 128\nDo you want to continue with this length")
            if(value=="yes"):
                for i in range(length):
                    textfield2.insert(tk.END,random.choice(character))
            else:
                textfield1.delete(0,tk.END)
                textfield2.delete(0,tk.END)
        else:
            for i in range(length):
                    textfield2.insert(tk.END,random.choice(character))

def clipboard():
    if(textfield2.get()==''):
        messagebox.showinfo("Info","No generated value")
    else:
        root.clipboard_clear()
        root.clipboard_append(textfield2.get())
        messagebox.showinfo("Info","The password is copied to clipboard")
        textfield1.delete(0,tk.END)
        textfield2.delete(0,tk.END)
            

label0=tk.Label(root,text="PASSWORD GENERATOR",font=("arial",15,"bold"))
label0.grid(row=0,column=3,padx=5,pady=5)

label1=tk.Label(root,text="Enter the length of the password")
label1.grid(row=1,column=2,padx=5,pady=15)

textfield1=tk.Entry(root,font=("arial",15))
textfield1.grid(row=1,column=3,padx=5,pady=15)

label1=tk.Label(root,text="Select the complexity")
label1.grid(row=2,column=2,padx=5,pady=15)

variable=tk.StringVar()
variable.set('low')

option_menu=tk.OptionMenu(root,variable,'low','medium','high')
option_menu.grid(row=2,column=3,padx=5,pady=15)

label2=tk.Label(root,text="The generated password ")
label2.grid(row=3,column=2,padx=5,pady=15)

textfield2=tk.Entry(root,font=("arial",15))
textfield2.grid(row=3,column=3,padx=5,pady=15)

button1=tk.Button(root,text="Generate password",width=20,command=generate_password)
button1.grid(row=4,column=2,padx=0,pady=25)

button2=tk.Button(root,text="Copy to clipboard",width=20,command=clipboard)
button2.grid(row=4,column=4,padx=0,pady=25)

root.title("Password Generator")
root.configure(bg="#F0F8FF")

root.mainloop()