import tkinter as tk
root = tk.Tk()

def button_clear1():
    value = textfield.get()[:-1]
    textfield.delete(0, tk.END)
    textfield.insert(tk.END, value)

def compute():
    try:
        value = eval(textfield.get())
        textfield.delete(0, tk.END)
        textfield.insert(tk.END, value)
    except:
        textfield.delete(0, tk.END)
        textfield.insert(tk.END,"Enter the correct calculation")

def button_neg():
    value = textfield.get()
    textfield.delete(0, tk.END)
    textfield.insert(tk.END, "-(" + value + ")")   

label1 = tk.Label(root, text="CALCULATOR", font=("arial", "18", "bold"))
label1.grid(row=0, column=4, columnspan=4, padx=10, pady=10)

label2 = tk.Label(root, text="Value and Result:", font=("arial", "12", "bold"))
label2.grid(row=1, column=4, columnspan=4, padx=0, pady=5)

textfield = tk.Entry(root, width=55)
textfield.grid(row=2, column=4, columnspan=4, padx=20, pady=20)

button_frame = tk.Frame(root)
button_frame.grid(row=3, column=5, columnspan=14,pady=15)


button_cle = tk.Button(button_frame, text="AC", command=lambda: textfield.delete(0, tk.END), height=2, width=10)
button_cle.grid(row=0, column=0, padx=8, pady=5)

button_cle1 = tk.Button(button_frame, text="Clear", command=button_clear1, height=2, width=10)
button_cle1.grid(row=0, column=1, padx=8, pady=5)

button_neg = tk.Button(button_frame, text="+/-", command=button_neg, height=2, width=10)
button_neg.grid(row=0, column=2, padx=8, pady=5)

button_div = tk.Button(button_frame, text="/", command=lambda: textfield.insert(tk.END, "/"), height=2, width=10)
button_div.grid(row=0, column=3, padx=8, pady=5)


button7 = tk.Button(button_frame, text="7", command=lambda: textfield.insert(tk.END, "7"), height=2, width=10)
button7.grid(row=1, column=0, padx=8, pady=5)

button8 = tk.Button(button_frame, text="8", command=lambda: textfield.insert(tk.END, "8"), height=2, width=10)
button8.grid(row=1, column=1, padx=8, pady=5)

button9 = tk.Button(button_frame, text="9", command=lambda: textfield.insert(tk.END, "9"), height=2, width=10)
button9.grid(row=1, column=2, padx=8, pady=5)

button_mul = tk.Button(button_frame, text="*", command=lambda: textfield.insert(tk.END, "*"), height=2, width=10)
button_mul.grid(row=1, column=3, padx=8, pady=5)


button4 = tk.Button(button_frame, text="4", command=lambda: textfield.insert(tk.END, "4"), height=2, width=10)
button4.grid(row=2, column=0, padx=8, pady=5)

button5 = tk.Button(button_frame, text="5", command=lambda: textfield.insert(tk.END, "5"), height=2, width=10)
button5.grid(row=2, column=1, padx=8, pady=5)

button6 = tk.Button(button_frame, text="6", command=lambda: textfield.insert(tk.END, "6"), height=2, width=10)
button6.grid(row=2, column=2, padx=8, pady=5)

button_sub = tk.Button(button_frame, text="-", command=lambda: textfield.insert(tk.END, "-"), height=2, width=10)
button_sub.grid(row=2, column=3, padx=8, pady=5)


button1 = tk.Button(button_frame, text="1", command=lambda: textfield.insert(tk.END, "1"), height=2, width=10)
button1.grid(row=3, column=0, padx=8, pady=5)

button2 = tk.Button(button_frame, text="2", command=lambda: textfield.insert(tk.END, "2"), height=2, width=10)
button2.grid(row=3, column=1, padx=8, pady=5)

button3 = tk.Button(button_frame, text="3", command=lambda: textfield.insert(tk.END, "3"), height=2, width=10)
button3.grid(row=3, column=2, padx=8, pady=5)

button_add = tk.Button(button_frame, text="+", command=lambda: textfield.insert(tk.END, "+"), height=2, width=10)
button_add.grid(row=3, column=3, padx=8, pady=5)


button_mod = tk.Button(button_frame, text="%", command=lambda: textfield.insert(tk.END, "%"), height=2, width=10)
button_mod.grid(row=4, column=0, padx=8, pady=5)

button0 = tk.Button(button_frame, text="0", command=lambda: textfield.insert(tk.END, "0"), height=2, width=10)
button0.grid(row=4, column=1, padx=8, pady=5)

button_dec = tk.Button(button_frame, text=".", command=lambda: textfield.insert(tk.END, "."), height=2, width=10)
button_dec.grid(row=4, column=2, padx=8, pady=5)

button_equ = tk.Button(button_frame, text="=", command=compute, height=2, width=10)
button_equ.grid(row=4, column=3, padx=8, pady=5)

root.title("Calculator")
root.configure(bg="#F0F8FF")

root.mainloop()
