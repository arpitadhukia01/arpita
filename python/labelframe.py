import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("LabelFrame Example")
root.geometry("420x260")

group = ttk.LabelFrame(root, text="Account", padding=12)
group.pack(fill="x", padx=20, pady=20)
ttk.Label(group, text="Username").pack(anchor="w")
ttk.Entry(group).pack(fill="x")

root.mainloop()
