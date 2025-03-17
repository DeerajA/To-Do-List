import tkinter as tk

root = tk.Tk()
root.title("To Do List")
root.geometry("400x700")
root.grid_rowconfigure(0,minsize=50)
root.config(background="#4c4c4c")
rows = 1

def saveTask(task):
    with open("Tasks.txt", 'a') as file:
        file.write(task + "\n")

def deleteSavedTask(task):
    with open("Tasks.txt", 'r') as file:
        tasks = file.readlines()
    with open("Tasks.txt", 'w') as file:
        for taskz in tasks:
            if taskz.strip() != task:
                file.write(taskz)

def loadTask():
    with open("Tasks.txt", 'r') as file:
        tasks = file.readlines()
    for task in tasks:
        addLabel(task.strip())

def clearPlaceholder(event):
    if entry.get() == "Enter Task":
        entry.delete(0, tk.END)

def capWord(event):
    text = entry.get()
    if text:
        entry.delete(0,tk.END)
        entry.insert(0,text[:1].upper() + text[1:]) 

def addLabel(text):
    global rows
    label = tk.Label(root, text=text)
    label.grid(row=rows,column=0,pady=5,padx=20,sticky="w")
    rows+=1
    label.config(font=("Garamond", 17), 
                 fg="White", 
                 bg="#4c4c4c")

    label.bind("<Enter>", lambda e: label.config(font=("Garamond", 17, "overstrike"), fg="red"))
    label.bind("<Leave>", lambda e: label.config(font=("Garamond", 17), fg = "white"))
    label.bind("<ButtonRelease-1>", lambda e: (deleteSavedTask(label.cget("text")), label.destroy()))
    
    entry.delete(0, tk.END)

def addButton(event=None):
    global rows
    task = entry.get().strip()
    if entry.get() == "" or entry.get() == "Enter Task":
        return
    saveTask(task)
    addLabel(task)
    entry.delete(0, tk.END)

def change(event):
    root.update_idletasks()
    button.place(x=root.winfo_width()-80)
    entry.config(width=int((root.winfo_width()-110)/10))


entry = tk.Entry(root)
entry.config(font=("Garamond", 18, "bold"), 
             highlightbackground="White", 
             relief="raised", 
             borderwidth=.1,
             width=31)
entry.insert(0, "Enter Task")
entry.bind("<FocusIn>", clearPlaceholder)
entry.place(x=20,y=10)
entry.bind("<KeyRelease>", capWord)

root.bind("<Configure>", change)
root.bind("<Return>", addButton)

button = tk.Button(root, text="Add", command=addButton)
button.config(font=("Garamond", 17, "bold"), 
              highlightbackground="White", 
              relief="raised", 
              borderwidth=1,
              fg= "black")
root.update_idletasks()
button.place(x=320,y=10)

loadTask()
root.mainloop()
