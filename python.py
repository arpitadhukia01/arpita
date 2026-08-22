import tkinter as tk
from tkinter import ttk

root = tk.Tk()

entry = ttk.Entry(root, width=30)
entry.pack(padx=20, pady=20)

placeholder = "Enter your name"

entry.insert(0, placeholder)

def on_focus_in(event):
    if entry.get() == placeholder:
        entry.delete(0, tk.END)

def on_focus_out(event):
    if not entry.get():
        entry.insert(0, placeholder)

entry.bind("<FocusIn>", on_focus_in)
entry.bind("<FocusOut>", on_focus_out)

root.mainloop()