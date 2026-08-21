import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3


# ---------------------------------------------------------
# DATABASE CONNECTION
# ---------------------------------------------------------
def connect_db():
    """
    Connect to SQLite database.
    If payroll.db does not exist, SQLite creates it automatically.
    """
    return sqlite3.connect("payroll.db")


# ---------------------------------------------------------
# CREATE TABLE
# ---------------------------------------------------------
def create_table():
    """
    Create tblCountry table if it does not already exist.
    """
    con = connect_db()
    cur = con.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS tblCountry
        (
            CID INTEGER PRIMARY KEY,
            CName TEXT NOT NULL,
            CCode TEXT NOT NULL
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

    txt_CID.delete(0, tk.END)
    txt_CName.delete(0, tk.END)
    txt_CCode.delete(0, tk.END)

    txt_CID.focus()


# ---------------------------------------------------------
# READ / SHOW DATA
# ---------------------------------------------------------
def fetch_data():
    """
    Read all records from tblCountry
    and display them in the grid.
    """

    try:
        con = connect_db()
        cur = con.cursor()

        cur.execute("SELECT CID, CName, CCode FROM tblCountry")
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
    Insert a new country into tblCountry.
    """

    CID = txt_CID.get().strip()
    CName = txt_CName.get().strip()
    CCode = txt_CCode.get().strip()

    # Check empty fields
    if CID == "" or CName == "" or CCode == "":
        messagebox.showwarning(
            "Missing Data",
            "Please enter all fields."
        )
        return

    # Country ID should be numeric
    if not CID.isdigit():
        messagebox.showwarning(
            "Invalid Data",
            "Country ID must be numeric."
        )
        return

    try:
        con = connect_db()
        cur = con.cursor()

        # ? is used for parameters in SQLite
        sql = """
            INSERT INTO tblCountry (CID, CName, CCode)
            VALUES (?, ?, ?)
        """

        cur.execute(sql, (CID, CName, CCode))

        con.commit()
        con.close()

        messagebox.showinfo(
            "Success",
            "Country added successfully."
        )

        fetch_data()
        clear_form()

    except sqlite3.IntegrityError:
        messagebox.showerror(
            "Error",
            "Country ID already exists."
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
    Update country name and country code
    using Country ID.
    """

    CID = txt_CID.get().strip()
    CName = txt_CName.get().strip()
    CCode = txt_CCode.get().strip()

    if CID == "":
        messagebox.showwarning(
            "Select Record",
            "Please select a record to update."
        )
        return

    if CName == "" or CCode == "":
        messagebox.showwarning(
            "Missing Data",
            "Please enter country name and country code."
        )
        return

    try:
        con = connect_db()
        cur = con.cursor()

        sql = """
            UPDATE tblCountry
            SET CName = ?, CCode = ?
            WHERE CID = ?
        """

        cur.execute(
            sql,
            (CName, CCode, CID)
        )

        con.commit()
        con.close()

        messagebox.showinfo(
            "Success",
            "Country updated successfully."
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
    Delete a country using Country ID.
    """

    CID = txt_CID.get().strip()

    if CID == "":
        messagebox.showwarning(
            "Select Record",
            "Please select a record to delete."
        )
        return

    answer = messagebox.askyesno(
        "Confirm Delete",
        "Are you sure you want to delete this country?"
    )

    if answer == False:
        return

    try:
        con = connect_db()
        cur = con.cursor()

        cur.execute(
            "DELETE FROM tblCountry WHERE CID = ?",
            (CID,)
        )

        con.commit()
        con.close()

        messagebox.showinfo(
            "Success",
            "Country deleted successfully."
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
    txt_CID.delete(0, tk.END)
    txt_CName.delete(0, tk.END)
    txt_CCode.delete(0, tk.END)

    # Put grid values into text boxes
    txt_CID.insert(0, values[0])
    txt_CName.insert(0, values[1])
    txt_CCode.insert(0, values[2])


# =========================================================
# CREATE MAIN WINDOW
# =========================================================

root = tk.Tk()

root.title("Country CRUD - SQLite")
root.geometry("700x500")


# =========================================================
# TITLE
# =========================================================

lbl_title = tk.Label(
    root,
    text="Country Management",
    font=("Arial", 20, "bold")
)

lbl_title.pack(pady=10)


# =========================================================
# FORM
# =========================================================

form_frame = tk.Frame(root)
form_frame.pack(pady=10)


# Country ID
tk.Label(
    form_frame,
    text="Country ID:",
    font=("Arial", 12)
).grid(
    row=0,
    column=0,
    padx=10,
    pady=8,
    sticky="w"
)

txt_CID = tk.Entry(
    form_frame,
    font=("Arial", 12),
    width=30
)

txt_CID.grid(
    row=0,
    column=1,
    padx=10,
    pady=8
)


# Country Name
tk.Label(
    form_frame,
    text="Country Name:",
    font=("Arial", 12)
).grid(
    row=1,
    column=0,
    padx=10,
    pady=8,
    sticky="w"
)

txt_CName = tk.Entry(
    form_frame,
    font=("Arial", 12),
    width=30
)

txt_CName.grid(
    row=1,
    column=1,
    padx=10,
    pady=8
)


# Country Code
tk.Label(
    form_frame,
    text="Country Code:",
    font=("Arial", 12)
).grid(
    row=2,
    column=0,
    padx=10,
    pady=8,
    sticky="w"
)

txt_CCode = tk.Entry(
    form_frame,
    font=("Arial", 12),
    width=30
)

txt_CCode.grid(
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
    columns=("CID", "CName", "CCode"),
    show="headings"
)


# Grid headings
grid.heading(
    "CID",
    text="Country ID"
)

grid.heading(
    "CName",
    text="Country Name"
)

grid.heading(
    "CCode",
    text="Country Code"
)


# Grid column sizes
grid.column(
    "CID",
    width=130,
    anchor="center"
)

grid.column(
    "CName",
    width=220
)

grid.column(
    "CCode",
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

# Cursor starts at Country ID
txt_CID.focus()

# Start Tkinter
root.mainloop()