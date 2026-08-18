import tkinter as tk
from tkinter import ttk


def greet():
    if enabled.get():
        print("We are happy to update you.")
    else:
        print("May you miss the chances of offers.")
root = tk.Tk()
root.title("Checkbutton Example")
root.geometry("420x260")
enabled = tk.BooleanVar(value=True)

ttk.Checkbutton(root, text="Enable notifications", variable=enabled).pack(pady=20)
ttk.Button(root, text="Print", command=lambda: greet()).pack()

root.mainloop()

# label frame - title - Select your Hobbies
# create 2 checkboxes inside label frame Studying, Playing
# Submit Button - lambda : submit_hobby()
# make 2 variables chkstudy, chkplaying bind with variable property of checkboxes 
# print message - both checkbox checked - excelent , if study - very good, if playing - good 