
import tkinter as tk

def popupmsg(title,msg):
    root = tk.Tk()
    root.title(title)

    label = tk.Label(root, text=msg,width=30, height=10)
    label.pack(side="top", fill="x", pady=10)
    B1 = tk.Button(root, text="Okay", command = root.destroy)
    B1.pack()
    root.mainloop()

