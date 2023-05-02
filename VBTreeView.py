import mysql.connector
from tkinter import ttk
import tkinter as tk

class MainScreen:
    def __init__(self):
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="root",
            database="dbauto"
        )

        self.my_w = tk.Tk()
        self.my_w.geometry("400x280")
        self.my_w.title("Treeview auto")

        self.create_menu()

        self.trv = ttk.Treeview(self.my_w, selectmode='browse')
        self.trv.grid(row=1, column=1, padx=20, pady=20)
        self.trv["columns"] = ("1", "2", "3", "4", "5")
        self.trv['show'] = 'headings'
        self.trv.column("1", width=30, anchor='c')
        self.trv.column("2", width=80, anchor='c')
        self.trv.column("3", width=80, anchor='c')
        self.trv.column("4", width=50, anchor='c')
        self.trv.column("5", width=80, anchor='c')
        self.trv.heading("1", text="id")
        self.trv.heading("2", text="Merk")
        self.trv.heading("3", text="Model")
        self.trv.heading("4", text="Bouwjaar")
        self.trv.heading("5", text="Brandstof")

        # create delete button
        delete_button = tk.Button(self.my_w, text="Delete", command=self.delete_car)
        delete_button.grid(row=2, column=1)

        self.fill_table()

    def create_menu(self):
        menu_bar = tk.Menu(self.my_w)

        # create a pulldown menu, and add it to the menu bar
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Voeg auto toe", command=self.add_car)
        file_menu.add_command(label="Wijzig auto", command=self.edit_car)
        file_menu.add_command(label="Quit", command=self.quit)
        menu_bar.add_cascade(label="Menu", menu=file_menu)

        # display the menu
        self.my_w.config(menu=menu_bar)

    def add_car(self):
        # TODO: implement add car functionality
        pass

    def edit_car(self):
        # TODO: implement edit car functionality
        pass

    def fill_table(self):
        cur = self.db.cursor()
        cur.execute('''SELECT * from auto''')
        for dt in cur:
            self.trv.insert("", 'end', iid=dt[0], text=dt[0],
                            values=(dt[0], dt[1], dt[2], dt[3], dt[4]))

    def delete_car(self):
        # get selected row id
        selected_row = self.trv.focus()
        if selected_row:
            selected_id = self.trv.item(selected_row)['values'][0]

            # delete from Treeview
            self.trv.delete(selected_row)

            # delete from database
            cur = self.db.cursor()
            cur.execute(f"DELETE FROM auto WHERE idauto={selected_id}")
            self.db.commit()

    def quit(self):
        self.my_w.quit()

    def run(self):
        self.my_w.mainloop()
if __name__ == "__main__":
    app = MainScreen()
    app.run()
