import tkinter as tk

root = tk.Tk()
root.title("To Do List")
root.geometry("400x700")
root.grid_rowconfigure(0,minsize=50)
root.config(background="#4c4c4c")
rows = 1 # For spacing purposes with list of labels

# Saves Tasks in a file named Tasks.txt
def saveTask(task):
    with open("Tasks.txt", 'a') as file:
        file.write(task + "\n")

# Deletes the task from Tasks.txt
def deleteSavedTask(task):
    with open("Tasks.txt", 'r') as file:
        tasks = file.readlines()
    with open("Tasks.txt", 'w') as file:
        for taskz in tasks:
            if taskz.strip() != task:
                file.write(taskz)

# Loads all tasks in new window
def loadTask():
    with open("Tasks.txt", 'r') as file:
        tasks = file.readlines()
    for task in tasks:
        addLabel(task.strip())

# Clears the 'Enter Task' in the entry feild
def clearPlaceholder(event):
    if entry.get() == "Enter Task":
        entry.delete(0, tk.END)

# Capitalizes the first letter
def capWord(event):
    text = entry.get()
    if text:
        entry.delete(0,tk.END)
        entry.insert(0,text[:1].upper() + text[1:]) 

# Adds text to the window as a label
def addLabel(text):
    global rows
    label = tk.Label(root, text=text)
    label.grid(row=rows,column=0,pady=5,padx=20,sticky="w")
    rows+=1
    label.config(font=("Garamond", 17), 
                 fg="White", 
                 bg="#4c4c4c")

    label.bind("<Enter>", lambda e: label.config(font=("Garamond", 17, "overstrike"), fg="red")) # Hovering of mouse causes red overstrike font
    label.bind("<Leave>", lambda e: label.config(font=("Garamond", 17), fg = "white")) # Returns to normal after mouse leaves label

    label.bind("<ButtonRelease-1>", lambda e: (deleteSavedTask(label.cget("text")), label.destroy())) # Release of left-click deletes task
    
    entry.delete(0, tk.END)

# Command for the button, runs saveTask
def addButton(event=None):
    global rows
    task = entry.get().strip()
    if entry.get() == "" or entry.get() == "Enter Task":
        return
    saveTask(task)
    addLabel(task)
    entry.delete(0, tk.END)

# To adjust the entry bar across window
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
entry.bind("<KeyRelease>", capWord)
entry.place(x=20,y=10)

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
