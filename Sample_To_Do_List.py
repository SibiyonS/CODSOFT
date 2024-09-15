""" TO_DO LIST """
import tkinter as tk
root=tk.Tk()
global tasks
tasks={}

def add_task():
    textarea.delete(1.0,tk.END)
    task_name =entry1.get()
    task_description =entry2.get()
    if(task_name and task_description!=""):
        tasks[task_name] = task_description
        textarea.insert(tk.END,"Task get inserted\n")
        entry1.delete(0,tk.END)
        entry2.delete(0,tk.END)
    else:
        textarea.insert(tk.END,"Enter the name and destination\n")

def delete_task():
    textarea.delete(1.0,tk.END)
    task_name =entry1.get()
    if(task_name!=""):
        if task_name not in tasks:
            textarea.insert(tk.END,"Name not found\n")
        else:
            textarea.insert(tk.END,"Task get deleted")
        if task_name in tasks:
            del tasks[task_name]
        entry1.delete(0,tk.END)
        entry2.delete(0,tk.END)
    else:
        textarea.insert(tk.END,"Enter the task name(optional destination name)\n")

def view_task():
    textarea.delete(1.0,tk.END)
    if(tasks=={}):
           textarea.insert(tk.END,"No task was stored\n")  
    else:
        for task, description in tasks.items():
                textarea.insert(tk.END,"Task:"+task+"\tDescription:"+description+"\n")
def update_task():
    textarea.delete(1.0,tk.END)
    task_name=entry1.get()
    task_description=entry2.get()
    if(task_name and task_description!=""):
        if task_name in tasks:
            tasks[task_name]=task_description
        if task_name not in tasks:
            textarea.insert(tk.END,"Name not found\n")
        else:
            textarea.insert(tk.END,"task get updated")
        entry1.delete(0,tk.END)
        entry2.delete(0,tk.END)
    else:
        textarea.insert(tk.END,"Enter the name and updated destination\n")

label0 = tk.Label(root, text="TO-DO LIST", font=("Arial", 14, "bold"))
label0.grid(row=0, column=0, columnspan=10, pady=2)

label1 = tk.Label(root, text="Enter task name")
label1.grid(row=1, column=0, padx=2, pady=15)

label2 = tk.Label(root, text="Enter task description")
label2.grid(row=2, column=0, padx=2, pady=15)

entry1 = tk.Entry(root)
entry1.grid(row=1, column=1, padx=2, pady=10)

entry2 = tk.Entry(root)
entry2.grid(row=2, column=1, padx=20, pady=10)

button1 = tk.Button(root, text="Add Task", command=add_task)
button1.grid(row=3, column=0, padx=30, pady=10)

button2 = tk.Button(root, text="Delete Task", command=delete_task)
button2.grid(row=3, column=1, padx=30, pady=10)

button3 = tk.Button(root, text="View Tasks", command=view_task)
button3.grid(row=4, column=0, padx=30, pady=10)

button4 = tk.Button(root, text="Update Task", command=update_task)
button4.grid(row=4, column=1, padx=30, pady=10)

textarea = tk.Text(root, height=15, width=50, font=("Arial", 12, "bold"))
textarea.grid(row=5, column=0, columnspan=2, padx=50, pady=80)

root.configure(bg="#F0F8FF")
root.title("TO-DO LIST")

root.mainloop()
