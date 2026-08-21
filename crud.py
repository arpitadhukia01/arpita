import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3


# ---------------------------------------------------------
# DATABASE CONNECTION
# ---------------------------------------------------------
def connect_db():
    """
    Connect to SQLite database.
    If dept.db does not exist, SQLite creates it automatically.
    """
    return sqlite3.connect("payroll.db")


# ---------------------------------------------------------
# CREATE TABLE
# ---------------------------------------------------------
def create_table():
    """
    Create tbldept table if it does not already exist.
    """
    con = connect_db()
    cur = con.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS tbldept
        (
            dno INTEGER PRIMARY KEY,
            dname TEXT NOT NULL,
            loc TEXT NOT NULL
        )
    """)

    con.commit()
    con.close()


# ---------------------------------------------------------
# CLEAR FORM
# ---------------------------------------------------------
def clear_form():
    """
    Clear all text boxes.
    """

    txt_dno.delete(0, tk.END)
    txt_dname.delete(0, tk.END)
    txt_loc.delete(0, tk.END)

    txt_dno.focus()


# ---------------------------------------------------------
# READ / SHOW DATA
# ---------------------------------------------------------
def fetch_data():
    """
    Read all records from tbldept
    and display them in the grid.
    """

    try:
        con = connect_db()
        cur = con.cursor()

        cur.execute("SELECT dno, dname, loc FROM tbldept")
        rows = cur.fetchall()

        con.close()

        # Clear old grid rows
        for item in grid.get_children():
            grid.delete(item)

        # Add database rows to grid
        for row in rows:
            grid.insert("", tk.END, values=row)

    except sqlite3.Error as e:
        messagebox.showerror("Database Error", str(e))


# ---------------------------------------------------------
# CREATE / INSERT
# ---------------------------------------------------------
def insert_data():
    """
    Insert a new department into tbldept.
    """

    dno = txt_dno.get().strip()
    dname = txt_dname.get().strip()
    loc = txt_loc.get().strip()

    # Check empty fields
    if dno == "" or dname == "" or loc == "":
        messagebox.showwarning(
            "Missing Data",
            "Please enter all fields."
        )
        return

    # Department number should be numeric
    if not dno.isdigit():
        messagebox.showwarning(
            "Invalid Data",
            "Department number must be numeric."
        )
        return

    try:
        con = connect_db()
        cur = con.cursor()

        # ? is used for parameters in SQLite
        sql = """
            INSERT INTO tbldept (dno, dname, loc)
            VALUES (?, ?, ?)
        """

        cur.execute(sql, (dno, dname, loc))

        con.commit()
        con.close()

        messagebox.showinfo(
            "Success",
            "Department added successfully."
        )

        fetch_data()
        clear_form()

    except sqlite3.IntegrityError:
        messagebox.showerror(
            "Error",
            "Department number already exists."
        )

    except sqlite3.Error as e:
        messagebox.showerror(
            "Database Error",
            str(e)
        )


# ---------------------------------------------------------
# UPDATE
# ---------------------------------------------------------
def update_data():
    """
    Update department name and location
    using department number.
    """

    dno = txt_dno.get().strip()
    dname = txt_dname.get().strip()
    loc = txt_loc.get().strip()

    if dno == "":
        messagebox.showwarning(
            "Select Record",
            "Please select a record to update."
        )
        return

    if dname == "" or loc == "":
        messagebox.showwarning(
            "Missing Data",
            "Please enter department name and location."
        )
        return

    try:
        con = connect_db()
        cur = con.cursor()

        sql = """
            UPDATE tbldept
            SET dname = ?, loc = ?
            WHERE dno = ?
        """

        cur.execute(
            sql,
            (dname, loc, dno)
        )

        con.commit()
        con.close()

        messagebox.showinfo(
            "Success",
            "Department updated successfully."
        )

        fetch_data()
        clear_form()

    except sqlite3.Error as e:
        messagebox.showerror(
            "Database Error",
            str(e)
        )


# ---------------------------------------------------------
# DELETE
# ---------------------------------------------------------
def delete_data():
    """
    Delete a department using department number.
    """

    dno = txt_dno.get().strip()

    if dno == "":
        messagebox.showwarning(
            "Select Record",
            "Please select a record to delete."
        )
        return

    answer = messagebox.askyesno(
        "Confirm Delete",
        "Are you sure you want to delete this department?"
    )

    if answer == False:
        return

    try:
        con = connect_db()
        cur = con.cursor()

        cur.execute(
            "DELETE FROM tbldept WHERE dno = ?",
            (dno,)
        )

        con.commit()
        con.close()

        messagebox.showinfo(
            "Success",
            "Department deleted successfully."
        )

        fetch_data()
        clear_form()

    except sqlite3.Error as e:
        messagebox.showerror(
            "Database Error",
            str(e)
        )


# ---------------------------------------------------------
# GRID ROW SELECTION
# ---------------------------------------------------------
def select_row(event):
    """
    When a row is selected in the grid,
    show that row's values in the text boxes.
    """

    selected_item = grid.focus()

    if selected_item == "":
        return

    row = grid.item(selected_item)

    values = row["values"]

    if not values:
        return

    # Clear text boxes
    txt_dno.delete(0, tk.END)
    txt_dname.delete(0, tk.END)
    txt_loc.delete(0, tk.END)

    # Put grid values into text boxes
    txt_dno.insert(0, values[0])
    txt_dname.insert(0, values[1])
    txt_loc.insert(0, values[2])


# =========================================================
# CREATE MAIN WINDOW
# =========================================================

root = tk.Tk()

root.title("Department CRUD - SQLite")
root.geometry("700x500")


# =========================================================
# TITLE
# =========================================================

lbl_title = tk.Label(
    root,
    text="Department Management",
    font=("Arial", 20, "bold")
)

lbl_title.pack(pady=10)


# =========================================================
# FORM
# =========================================================

form_frame = tk.Frame(root)
form_frame.pack(pady=10)


# Department Number
tk.Label(
    form_frame,
    text="Department No:",
    font=("Arial", 12)
).grid(
    row=0,
    column=0,
    padx=10,
    pady=8,
    sticky="w"
)

txt_dno = tk.Entry(
    form_frame,
    font=("Arial", 12),
    width=30
)

txt_dno.grid(
    row=0,
    column=1,
    padx=10,
    pady=8
)


# Department Name
tk.Label(
    form_frame,
    text="Department Name:",
    font=("Arial", 12)
).grid(
    row=1,
    column=0,
    padx=10,
    pady=8,
    sticky="w"
)

txt_dname = tk.Entry(
    form_frame,
    font=("Arial", 12),
    width=30
)

txt_dname.grid(
    row=1,
    column=1,
    padx=10,
    pady=8
)


# Location
tk.Label(
    form_frame,
    text="Location:",
    font=("Arial", 12)
).grid(
    row=2,
    column=0,
    padx=10,
    pady=8,
    sticky="w"
)

txt_loc = tk.Entry(
    form_frame,
    font=("Arial", 12),
    width=30
)

txt_loc.grid(
    row=2,
    column=1,
    padx=10,
    pady=8
)


# =========================================================
# BUTTONS
# =========================================================

button_frame = tk.Frame(root)
button_frame.pack(pady=10)


tk.Button(
    button_frame,
    text="Add",
    width=10,
    command=insert_data
).grid(
    row=0,
    column=0,
    padx=5
)


tk.Button(
    button_frame,
    text="Update",
    width=10,
    command=update_data
).grid(
    row=0,
    column=1,
    padx=5
)


tk.Button(
    button_frame,
    text="Delete",
    width=10,
    command=delete_data
).grid(
    row=0,
    column=2,
    padx=5
)


tk.Button(
    button_frame,
    text="Clear",
    width=10,
    command=clear_form
).grid(
    row=0,
    column=3,
    padx=5
)


tk.Button(
    button_frame,
    text="Refresh",
    width=10,
    command=fetch_data
).grid(
    row=0,
    column=4,
    padx=5
)


# =========================================================
# GRID / TREEVIEW
# =========================================================

grid_frame = tk.Frame(root)

grid_frame.pack(
    fill="both",
    expand=True,
    padx=20,
    pady=10
)


grid = ttk.Treeview(
    grid_frame,
    columns=("dno", "dname", "loc"),
    show="headings"
)


# Grid headings
grid.heading(
    "dno",
    text="Department No"
)

grid.heading(
    "dname",
    text="Department Name"
)

grid.heading(
    "loc",
    text="Location"
)


# Grid column sizes
grid.column(
    "dno",
    width=130,
    anchor="center"
)

grid.column(
    "dname",
    width=220
)

grid.column(
    "loc",
    width=180
)


# Scrollbar
scrollbar = ttk.Scrollbar(
    grid_frame,
    orient="vertical",
    command=grid.yview
)

grid.configure(
    yscrollcommand=scrollbar.set
)


grid.pack(
    side="left",
    fill="both",
    expand=True
)

scrollbar.pack(
    side="right",
    fill="y"
)


# When user selects a row
grid.bind(
    "<<TreeviewSelect>>",
    select_row
)


# =========================================================
# START PROGRAM
# =========================================================

# Create database table
create_table()

# Show existing data
fetch_data()

# Cursor starts at department number
txt_dno.focus()

# Start Tkinter
root.mainloop()
