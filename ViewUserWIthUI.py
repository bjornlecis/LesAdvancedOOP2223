import mysql.connector
import tkinter as tk
from tkinter import ttk

# Connect to the MySQL database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="login_example"
)

# Define a function to view all users in the database
def view_users():
    # Create a new tkinter window
    view_window = tk.Toplevel()
    view_window.title("View Users")

    # Create a treeview to display the user data
    tree = ttk.Treeview(view_window)
    tree.pack()

    # Define the columns for the treeview
    tree["columns"] = ("user_id", "user_name", "password")
    tree.column("#0", width=0, stretch=tk.NO)
    tree.column("user_id", width=50, anchor=tk.CENTER)
    tree.column("user_name", width=100, anchor=tk.CENTER)
    tree.column("password", width=100, anchor=tk.CENTER)

    # Add headers for the columns
    tree.heading("#0", text="")
    tree.heading("user_id", text="ID", anchor=tk.CENTER)
    tree.heading("user_name", text="Username", anchor=tk.CENTER)
    tree.heading("password", text="Password", anchor=tk.CENTER)

    # Create a cursor object and execute the SQL query to get all users
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM users")

    # Loop through the query results and add them to the treeview
    for row in mycursor.fetchall():
        tree.insert("", tk.END, values=row)

# Define a function to insert the user and password into the database
def insert_user():
    # Get the values from the entry boxes
    user_name = name_entry.get()
    password = password_entry.get()

    # Create a cursor object
    mycursor = mydb.cursor()

    # Execute the SQL query to insert the new user into the database
    sql = "INSERT INTO users (user_name, password) VALUES (%s, %s)"
    val = (user_name, password)
    mycursor.execute(sql, val)

    # Commit the changes to the database
    mydb.commit()

    # Clear the entry boxes
    name_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)

# Create a tkinter window
window = tk.Tk()
window.title("Insert New User")

# Create a label and entry box for the username
name_label = tk.Label(window, text="Username:")
name_label.pack()
name_entry = tk.Entry(window)
name_entry.pack()

# Create a label and entry box for the password
password_label = tk.Label(window, text="Password:")
password_label.pack()
password_entry = tk.Entry(window, show="*")
password_entry.pack()

# Create a button to insert the new user into the database
insert_button = tk.Button(window, text="Insert User", command=insert_user)
insert_button.pack()

# Create a button to view all users in the database
view_button = tk.Button(window, text="View Users", command=view_users)
view_button.pack()

# Start the tkinter main loop
window.mainloop()
