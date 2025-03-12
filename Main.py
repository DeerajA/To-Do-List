import tkinter as tk

root = tk.Tk()
root.title("To Do List")
root.geometry("400x700")
root.config(cursor="hand2")

entry = tk.Entry(root)
entry.pack()
entry.config(font=("Ariel", 14, "bold"), borderwidth=2, relief="raised")
def clearPlaceholder():
    if entry.get() == "Enter task":
        entry.delete(0, tk.END)
entry.insert(0, "Enter task")
entry.bind("<FocusIn>", clearPlaceholder)




print(root.tk.splitlist(root.tk.call("tk", "cursors")))

def addButton():
    label = tk.Label(root, text=entry.get())
    label.pack()
    label.bind("<ButtonRelease-1>", lambda e: label.destroy())
    entry.delete(0, tk.END)

button = tk.Button(root, text="Add", command=addButton)
button.pack()
button.bind("<Return>",lambda e: addButton)

root.mainloop()

#enter triggers the add button
#dont allow empty tasks
