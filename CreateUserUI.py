import mysql.connector
import tkinter as tk

# Connect to the MySQL database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="login_example"
)

# Create a tkinter window
window = tk.Tk()
window.title("Insert New User")

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

# Start the tkinter main loop
window.mainloop()
