import tkinter as tk
from tkinter import ttk
op="" # op contains the operator
n1=0
n2=0
r=0

def btndigit_click(digit):
    current = txtnum.get()
    txtnum.delete(0, tk.END)
    txtnum.insert(0, current + str(digit))
def op_click(operator):
    global op, n1
    op = operator
    n1 = float(txtnum.get())
    txtnum.delete(0, tk.END)
def equal_click():
    global op, n1, n2, r
    n2 = float(txtnum.get())
    if op == "+":
        r = n1 + n2
    elif op == "-":
        r = n1 - n2
    elif op == "*":
        r = n1 * n2
    elif op == "/":
        if n2 != 0:
            r = n1 / n2
        else:
            txtnum.delete(0, tk.END)
            txtnum.insert(0, "Error: Division by zero")
            return
    txtnum.delete(0, tk.END)
    txtnum.insert(0, str(r))   
# Initialize window
window = tk.Tk()
window.title("My Calculator")
window.geometry("400x400")
window.resizable(False, False)

# Cleaned loop to configure all 6 columns and 6 rows with equal weight uniformly
for col in range(6):
    window.columnconfigure(col, weight=1)
for row in range(1, 6):
    window.rowconfigure(row, weight=1)

# Display entry box - Spans the entire window width
txtnum = ttk.Entry(window, width=32, font=("Arial", 16), justify="right")
txtnum.grid(row=0, column=0, columnspan=6, pady=10, padx=10, sticky="ew")

# --- ROW 1 BUTTONS ---
lblmem = ttk.Label(window, text="M", font=("Arial", 12), background="lightgrey", width=3, anchor="center") 
lblmem.grid(row=1, column=0, pady=5, padx=2, sticky="nsew") # Changed sticky to nsew

btnbackspace = ttk.Button(window, text="⌫", width=5)
btnbackspace.grid(row=1, column=1, pady=5, padx=2, sticky="nsew")

btnce = ttk.Button(window, text="CE", width=5)
btnce.grid(row=1, column=2, pady=5, padx=2, sticky="nsew")

btnc = ttk.Button(window, text="C", width=5)
btnc.grid(row=1, column=3, pady=5, padx=2, sticky="nsew")


# --- ROW 2 BUTTONS ---
btnmc = ttk.Button(window, text="MC", width=3)
btnmc.grid(row=2, column=0, pady=5, padx=2, sticky="nsew")

btn7 = ttk.Button(window, text="7", width=3, command=lambda: btndigit_click(7))
btn7.grid(row=2, column=1, pady=5, padx=2, sticky="nsew")

btn8 = ttk.Button(window, text="8", width=3, command=lambda: btndigit_click(8))
btn8.grid(row=2, column=2, pady=5, padx=2, sticky="nsew")

btn9 = ttk.Button(window, text="9", width=3, command=lambda: btndigit_click(9))
btn9.grid(row=2, column=3, pady=5, padx=2, sticky="nsew")

btndivide = ttk.Button(window, text="/", width=3, command=lambda: op_click("/"))
btndivide.grid(row=2, column=4, pady=5, padx=2, sticky="nsew")

btnsqrt = ttk.Button(window, text="√", width=3)
btnsqrt.grid(row=2, column=5, pady=5, padx=2, sticky="nsew")


# --- ROW 3 BUTTONS ---
btnmr = ttk.Button(window, text="MR", width=3)
btnmr.grid(row=3, column=0, pady=5, padx=2, sticky="nsew")

btn4 = ttk.Button(window, text="4", width=3, command=lambda: btndigit_click(4))
btn4.grid(row=3, column=1, pady=5, padx=2, sticky="nsew")

btn5 = ttk.Button(window, text="5", width=3, command=lambda: btndigit_click(5))
btn5.grid(row=3, column=2, pady=5, padx=2, sticky="nsew")

btn6 = ttk.Button(window, text="6", width=3, command=lambda: btndigit_click(6))
btn6.grid(row=3, column=3, pady=5, padx=2, sticky="nsew")

btnmultiply = ttk.Button(window, text="*", width=3, command=lambda: op_click("*"))
btnmultiply.grid(row=3, column=4, pady=5, padx=2, sticky="nsew")

btnpercent = ttk.Button(window, text="%", width=3)
btnpercent.grid(row=3, column=5, pady=5, padx=2, sticky="nsew")


# --- ROW 4 BUTTONS ---
btnms = ttk.Button(window, text="MS", width=3)
btnms.grid(row=4, column=0, pady=5, padx=2, sticky="nsew")

btn1 = ttk.Button(window, text="1", width=3, command=lambda: btndigit_click(1))
btn1.grid(row=4, column=1, pady=5, padx=2, sticky="nsew")

btn2 = ttk.Button(window, text="2", width=3, command=lambda: btndigit_click(2))
btn2.grid(row=4, column=2, pady=5, padx=2, sticky="nsew")

btn3 = ttk.Button(window, text="3", width=3, command=lambda: btndigit_click(3))
btn3.grid(row=4, column=3, pady=5, padx=2, sticky="nsew")

btnminus = ttk.Button(window, text="-", width=3, command=lambda: op_click("-"))
btnminus.grid(row=4, column=4, pady=5, padx=2, sticky="nsew")

btnfraction = ttk.Button(window, text="1/x", width=3)
btnfraction.grid(row=4, column=5, pady=5, padx=2, sticky="nsew")


# --- ROW 5 BUTTONS ---
btnmplus = ttk.Button(window, text="M+", width=3)
btnmplus.grid(row=5, column=0, pady=5, padx=2, sticky="nsew")

btn0 = ttk.Button(window, text="0", width=3, command=lambda: btndigit_click(0))
btn0.grid(row=5, column=1, pady=5, padx=2, sticky="nsew")

btndot = ttk.Button(window, text=".", width=3)
btndot.grid(row=5, column=2, pady=5, padx=2, sticky="nsew")

btnpm = ttk.Button(window, text="±", width=3)
btnpm.grid(row=5, column=3, pady=5, padx=2, sticky="nsew")

btnplus = ttk.Button(window, text="+", width=3, command=lambda: op_click("+"))
btnplus.grid(row=5, column=4, pady=5, padx=2, sticky="nsew")

btnequal = ttk.Button(window, text="=", width=3, command=equal_click)
btnequal.grid(row=5, column=5, pady=5, padx=2, sticky="nsew")

# Start application
window.mainloop()
