import tkinter as tk

root = tk.Tk()
root.title("To Do List")
root.geometry("400x700")
root.grid_rowconfigure(0,minsize=50)

entry = tk.Entry(root)
entry.config(font=("Garamond", 18, "bold"), 
             highlightbackground="grey", 
             relief="raised", 
             borderwidth=.1,
             width=31)
def clearPlaceholder(event):
    if entry.get() == "Enter Task":
        entry.delete(0, tk.END)
entry.insert(0, "Enter Task")
entry.bind("<FocusIn>", clearPlaceholder)
entry.place(x=20,y=10)

rows = 1
def addButton(event=None):
    global rows
    if entry.get() == "" or entry.get() == "Enter Task":
        return
    label = tk.Label(root, text=entry.get())

    label.grid(row=rows,column=0,pady=5,padx=20,sticky="w")
    rows+=1

    label.config(font=("Garamond", 17), 
                 fg="White", 
                 bg="black")

    label.bind("<Enter>", lambda e: label.config(font=("Garamond", 17, "overstrike"), fg="red"))
    label.bind("<Leave>", lambda e: label.config(font=("Garamond", 17), fg = "white"))
    label.bind("<ButtonRelease-1>", lambda e: label.destroy())
    
    entry.delete(0, tk.END)

button = tk.Button(root, text="Add", command=addButton)
button.config(font=("Garamond", 17, "bold"), 
              highlightbackground="grey", 
              relief="raised", 
              borderwidth=1,
              fg= "black")
button.place(x=320,y=10)
root.bind("<Return>", addButton)
root.mainloop()
