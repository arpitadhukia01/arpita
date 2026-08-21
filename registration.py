import tkinter as tk
from tkinter import ttk

def greet():
    if enabled.get():
        print("We are happy to update you.")
    else:
        print("May you miss the chances of offers.")

# New function for the hobbies section
def submit_hobby():
    if chkstudy.get() and chkplaying.get():
        print("excellent")
    elif chkstudy.get():
        print("very good")
    elif chkplaying.get():
        print("good")

root = tk.Tk()
root.title("Checkbutton Example")
root.geometry("420x350")  # Increased height slightly to fit the new elements nicely

# --- Upper Code Elements ---
enabled = tk.BooleanVar(value=True)

ttk.Checkbutton(root, text="Enable notifications", variable=enabled).pack(pady=20)
ttk.Button(root, text="Print", command=lambda: greet()).pack(pady=10)

# --- New Code Elements (From Comments) ---
# 1. Label Frame with title "Select your Hobbies"
lf = ttk.LabelFrame(root, text="Select your Hobbies")
lf.pack(pady=20, padx=20, fill="both", expand=True)

# 4. Create 2 variables for the checkboxes
chkstudy = tk.BooleanVar()
chkplaying = tk.BooleanVar()

# 2. Create 2 checkboxes inside the Label Frame bound to the variables
ttk.Checkbutton(lf, text="Studying", variable=chkstudy).pack(anchor="w", padx=10, pady=5)
ttk.Checkbutton(lf, text="Playing", variable=chkplaying).pack(anchor="w", padx=10, pady=5)

# 3. Submit Button
ttk.Button(root, text="Submit Hobbies", command=lambda: submit_hobby()).pack(pady=10)

root.mainloop()
