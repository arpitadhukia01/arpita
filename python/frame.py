import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Frame Example")
root.geometry("420x260")

top = ttk.Frame(root, padding=12)
top.pack(fill="x")
ttk.Label(top, text="Header inside a frame").pack(anchor="w")

content = ttk.Frame(root, padding=12)
content.pack(fill="both", expand=True)
ttk.Button(content, text="Action").pack()

root.mainloop()
