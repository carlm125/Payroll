from tkinter import *
from tkinter import ttk
import sqlite3
from tkinter import messagebox
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.pagesizes import LEGAL

import csv
from datetime import date,time,datetime
today = date.today()


# database connector
conn = sqlite3.connect("Employee_Hours.db")
c = conn.cursor()


def MainScreen():


    root = Tk()
    root.title('Employee Details')

    root.geometry("1920x1080")


    # Add Some Style
    style = ttk.Style()

    # Pick A Theme
    style.theme_use('default')

    # Configure the Treeview Colors
    style.configure("Treeview",
                    background="#1a1919",
                    foreground="black",
                    rowheight=25,
                    fieldbackground="#1a1919")

    # Change Selected Color
    style.map('Treeview',
              background=[('selected', "#2f5f6e")])

    # Create a Treeview Frame
    tree_frame = Frame(root)
    tree_frame.pack(pady=10)

    # Create a Treeview Scrollbar
    treeview_scrollbar = Scrollbar(tree_frame)
    treeview_scrollbar.pack(side=RIGHT, fill=Y)

    # Create The Treeview
    my_tree = ttk.Treeview(tree_frame, yscrollcommand=treeview_scrollbar.set, selectmode="extended")
    my_tree.pack()

    # Configure the Scrollbar
    treeview_scrollbar.config(command=my_tree.yview)

    # Define Our Columns
    my_tree['columns'] = ("ID","First Name", "Last Name",  "PPS", "Role", "Pay","Emp_Id","Hours Worked")

    # Format Our Columns
    my_tree.column("#0", width=0, stretch=NO)
    my_tree.column("ID", anchor=CENTER, width=100)
    my_tree.column("First Name", anchor=W, width=140)
    my_tree.column("Last Name", anchor=W, width=140)
    my_tree.column("PPS", anchor=CENTER, width=140)
    my_tree.column("Role", anchor=CENTER, width=150)
    my_tree.column("Pay", anchor=CENTER, width=100)
    my_tree.column("Emp_Id", anchor=CENTER, width=140)
    my_tree.column("Hours Worked", anchor=CENTER, width=140)




    # Create Headings
    my_tree.heading("#0", text="", anchor=W)
    my_tree.heading("ID", text="ID", anchor=W)
    my_tree.heading("First Name", text="First Name", anchor=W)
    my_tree.heading("Last Name", text="Last Name", anchor=CENTER)
    my_tree.heading("PPS", text="PPS", anchor=CENTER)
    my_tree.heading("Role", text="Role", anchor=CENTER)
    my_tree.heading("Pay", text="Pay", anchor=CENTER)
    my_tree.heading("Emp_Id", text="Emp_Id", anchor=CENTER)
    my_tree.heading("Hours Worked", text="Hours Worked", anchor=CENTER)
    '''messagebox.showinfo("Insructions",
                        "1. When Calculating employee wage \n please click on the employee record \n and change the numbers of hours worked\n "
                        "2. When adding a new record to the databse \nleave the Id field blank as this will be assigned automatically")'''

    # Add Data
    def Query_database():

        conn = sqlite3.connect('Employee_Hours.db')
        c = conn.cursor()

        c.execute("SELECT rowid,* FROM Employees")
        records = c.fetchall()
        global count
        count = 0
        for record in records:
            if count % 2 == 0:
                my_tree.insert(parent='', index='end', iid=count, text='',
                               values=(record[0], record[1], record[2], record[3], record[4], record[5],record[6],record[7]),
                               tags=('evenrow',))
            else:
                my_tree.insert(parent='', index='end', iid=count, text='',
                               values=(record[0], record[1], record[2], record[3], record[4], record[5],record[6],record[7]),
                               tags=('oddrow',))
            # increment counter
            count += 1

        conn.commit()

        conn.close()





    # Create Striped Row Tags
    my_tree.tag_configure('oddrow', background="white")
    my_tree.tag_configure('evenrow', background="lightgrey")

    # Add our data to the screen
    global count
    count = 0


    # Add Record Entry Boxes
    data_frame = LabelFrame(root, text="Details")
    data_frame.pack(fill="x", expand="yes", padx=40)

    Id_lbl = Label(data_frame, text="Id")
    Id_lbl.grid(row=0, column=0, padx=10, pady=10)
    Id_entry = Entry(data_frame)
    Id_entry.grid(row=0, column=1, padx=10, pady=10)

    Firstname_lbl = Label(data_frame, text="First Name")
    Firstname_lbl.grid(row=0, column=2, padx=10, pady=10)
    Firstname_Entry = Entry(data_frame)
    Firstname_Entry.grid(row=0, column=3, padx=10, pady=10)

    Lastname_lbl = Label(data_frame, text="Last Name")
    Lastname_lbl.grid(row=0, column=4, padx=10, pady=10)
    Lastname_entry = Entry(data_frame)
    Lastname_entry.grid(row=0, column=5, padx=10, pady=10)

    PPS_lbl = Label(data_frame, text="PPS")
    PPS_lbl.grid(row=1, column=0, padx=10, pady=10)
    PPS_entry = Entry(data_frame)
    PPS_entry.grid(row=1, column=1, padx=10, pady=10)

    Role_lbl = Label(data_frame, text="Role")
    Role_lbl.grid(row=1, column=2, padx=10, pady=10)
    Role_entry = Entry(data_frame)
    Role_entry.grid(row=1, column=3, padx=10, pady=10)

    Pay_lbl = Label(data_frame, text="Pay")
    Pay_lbl.grid(row=1, column=4, padx=10, pady=10)
    Pay_entry = Entry(data_frame)
    Pay_entry.grid(row=1, column=5, padx=10, pady=10)

    Emp_id_label = Label(data_frame, text="Emp_Id")
    Emp_id_label.grid(row=0, column=6, padx=10, pady=10)
    Emp_id_entry = Entry(data_frame)
    Emp_id_entry.grid(row=0, column=7, padx=10, pady=10)

    Hours_worked_lbl = Label(data_frame, text="Hours Worked")
    Hours_worked_lbl.grid(row=1, column=6, padx=10, pady=10)
    Hours_worked_entry = Entry(data_frame)
    Hours_worked_entry.grid(row=1, column=7, padx=10, pady=10)


    def Clear_entries():
        Firstname_Entry.delete(0, END)
        Lastname_entry.delete(0, END)
        Id_entry.delete(0, END)
        PPS_entry.delete(0, END)
        Role_entry.delete(0, END)
        Pay_entry.delete(0, END)
        Emp_id_entry.delete(0, END)
        Hours_worked_entry.delete(0, END)
    def Record_up():
        rows = my_tree.selection()
        for row in rows:
            my_tree.move(row, my_tree.parent(row), my_tree.index(row)-1)

    def Record_Down():
        rows = my_tree.selection()
        for row in reversed(rows):
            my_tree.move(row, my_tree.parent(row), my_tree.index(row)+1)

    def Remove_one():
        remove  = my_tree.selection()[0]
        my_tree.delete(remove)
        response = messagebox.askyesno("Delete All.", "Are you sure you want to selcted record?")
        if response == 1:
            conn = sqlite3.connect("Employee_Hours.db")
            c=conn.cursor()
            c.execute("DELETE FROM Employees WHERE oid=" + Id_entry.get())

            Clear_entries()

            conn.commit()
            conn.close()
            messagebox.showinfo("Record Deleted.", "Your record has been removed")

    def Remove_many():
        remove  = my_tree.selection()
        response = messagebox.askyesno("Delete All.", "Are you sure you want to the selected records?")
        if response == 1:
            ids_to_delete =[]
            for record in remove:
                ids_to_delete.append((my_tree.item(record)))

            for record in remove:
                    my_tree.delete(record)

            conn = sqlite3.connect("Employee_Hours.db")
            c = conn.cursor()

            c.executemany("DELETE FROM Employees WHERE oid= ?", [(a,)for a in ids_to_delete])

            ids_to_delete =[]



            conn.commit()
            conn.close()
            messagebox.showinfo("Record Deleted.", "Your record has been removed")
            Clear_entries()




    def Remove_all():
        response = messagebox.askyesno("Delete All.", "Are you sure you want to delete all records?")
        if response == 1:
            for record in my_tree.get_children():
                my_tree.delete(record)

                conn = sqlite3.connect("Employee_Hours.db")
                c = conn.cursor()
                c.execute("DROP TABLE Employees ")

                Clear_entries()

                conn.commit()
                conn.close()
                messagebox.showinfo("Record Deleted.", "Your record has been removed")
                Clear_entries()






    def Update_record():
        selected = my_tree.focus()
        my_tree.item(selected, text="", values=(Id_entry.get(),Firstname_Entry.get(), Lastname_entry.get(),  PPS_entry.get(), Role_entry.get(), Pay_entry.get(), Emp_id_entry.get(),Hours_worked_entry.get(),))
        conn = sqlite3.connect('Employee_Hours.db')
        c = conn.cursor()

        c.execute("""UPDATE Employees SET 
                Firstname = :first, 
                Lastname = :last,
                PPS = :PPS,
                Role = :role,
                Pay = :pay,
                Emp_Id = :emp_id,
                Hours_Worked = :hours_worked
            
                WHERE oid = :oid""",
                {
                        "first": Firstname_Entry.get(),
                        "last": Lastname_entry.get(),
                        "PPS": PPS_entry.get(),
                        "role": Role_entry.get(),
                        "pay": Pay_entry.get(),
                        "emp_id": Emp_id_entry.get(),
                        "hours_worked": Hours_worked_entry.get(),
                        "oid": Id_entry.get(),

                 })



        conn.commit()

        conn.close()
        Clear_entries()




    def select_record(e):
        Id_entry.delete(0, END)
        Firstname_Entry.delete(0, END)
        Lastname_entry.delete(0, END)
        PPS_entry.delete(0, END)
        Role_entry.delete(0, END)
        Pay_entry.delete(0, END)
        Emp_id_entry.delete(0, END)
        Hours_worked_entry.delete(0, END)

        #Select record
        selected = my_tree.focus()
        #Select record values
        values = my_tree.item(selected, 'values')

        #Entry boxes that are populated
        Firstname_Entry.insert(0, values[1])
        Lastname_entry.insert(0, values[2])
        Id_entry.insert(0, values[0])
        PPS_entry.insert(0, values[3])
        Role_entry.insert(0, values[4])
        Pay_entry.insert(0, values[5])
        Emp_id_entry.insert(0, values[6])
        Hours_worked_entry.insert(0, values[7])

    def Add_Record():
        selected = my_tree.focus()
        my_tree.item(selected, text="", values=(Id_entry.get(), Firstname_Entry.get(), Lastname_entry.get(), PPS_entry.get(), Role_entry.get(), Pay_entry.get(),Emp_id_entry.get(),Hours_worked_entry.get(),))
        conn = sqlite3.connect('Employee_Hours.db')
        c = conn.cursor()

        c.execute("""INSERT INTO Employees VALUES (:first,:last,:PPS,:role,:pay,:emp_id,:hours_worked)
                    """,
                  {
                      "first": Firstname_Entry.get(),
                      "last": Lastname_entry.get(),
                      "PPS": PPS_entry.get(),
                      "role": Role_entry.get(),
                      "pay": Pay_entry.get(),
                      "emp_id": Emp_id_entry.get(),
                      "hours_worked": Hours_worked_entry.get(),





                  })

        conn.commit()

        conn.close()
        Id_entry.delete(0, END)
        Firstname_Entry.delete(0, END)
        Lastname_entry.delete(0, END)
        PPS_entry.delete(0, END)
        Role_entry.delete(0, END)
        Pay_entry.delete(0, END)
        Emp_id_entry.delete(0, END)
        Hours_worked_entry.delete(0, END)


        my_tree.delete(*my_tree.get_children())
        Query_database()



    def calculatewage():
        Usc = .002
        Paye = 0.02
        Prsi = 0.02
        pps = PPS_entry.get()
        Monthly_Tax_Credits = 1700/12
        employee_fname= Firstname_Entry.get()
        employee_lname = Lastname_entry.get()
        emp_id = Emp_id_entry.get()
        pay_rate = float(Pay_entry.get())

        hours_worked = float(Hours_worked_entry.get())
        #gross_pay = float(pay_rate * hours_worked)
        gross_pay = round(pay_rate * hours_worked + Monthly_Tax_Credits,2)
        Paye_Tax = round(float(gross_pay * Paye),2)
        Prsi_Tax =  round(float(gross_pay * Prsi),2)
        Usc_Tax = round(float(gross_pay * Usc),2)
        Total_Deductions = round(Paye_Tax + Prsi_Tax + Usc_Tax,2)
        Net_Income = round(gross_pay - Total_Deductions,2)


        conn = sqlite3.connect('Employee_Hours.db')
        c = conn.cursor()



        c.execute("""INSERT INTO Pay VALUES (:emp_id,:gross_income,:paye,:prsi,:usc,:total_deductions,:net_income,:date_created)
                    """,
                  {
                      "emp_id": Emp_id_entry.get(),
                      "gross_income": gross_pay,
                      "paye": Paye_Tax,
                      "prsi": Prsi_Tax,
                      "usc": Usc_Tax,
                      "total_deductions": Total_Deductions,
                      "net_income": Net_Income,
                      "date_created": today


                  })



        c.execute("""SELECT ROUND(SUM(Paye),2) TOTAL FROM Pay WHERE Emp_Id = :emp_id 
                            """,
                  {
                      "emp_id": Emp_id_entry.get(),
                  }
                  )
        Paye_Total = c.fetchall()



        c.execute("""SELECT ROUND(SUM(Prsi),2) TOTAL FROM Pay WHERE Emp_Id = :emp_id 
                                    """,
                  {
                      "emp_id": Emp_id_entry.get(),
                  }
                  )

        Prsi_Total = c.fetchall()



        c.execute("""SELECT ROUND(SUM(Usc),2) TOTAL FROM Pay WHERE Emp_Id = :emp_id 
                                            """,
                  {
                      "emp_id": Emp_id_entry.get(),
                  }
                  )
        Usc_Total = c.fetchall()


        c.execute("""SELECT ROUND(SUM(Total_Deductions),2) TOTAL FROM Pay WHERE Emp_Id = :emp_id 
                                                    """,
                  {
                      "emp_id": Emp_id_entry.get(),
                  }
                  )
        Total_Deductions_Year = c.fetchall()

        conn.commit()
        conn.close()



        canvas = Canvas(str(employee_fname) + str(emp_id) + "Payrol.pdf", pagesize=LEGAL)
        canvas.setFont("Helvetica", 11, )

        # date created
        canvas.drawString(400, 970, "Date Created", )
        canvas.drawString(500, 970, str(today))
        canvas.drawString(400, 950, "PPS")
        canvas.drawString(500, 950, str(pps))
        canvas.drawString(400, 930, "Employee Number")
        canvas.drawString(500, 930, str(emp_id))
        # First name
        canvas.drawString(0, 970, "Name")
        canvas.drawString(35, 970, str(employee_fname) + " " + str(employee_lname))
        # Gross earnings
        canvas.line(0, 897, 250, 897)
        canvas.drawString(0, 900, "Gross Income")
        # description
        canvas.drawString(0, 885, "Description")
        # Basic Hpurly
        canvas.drawString(0, 865, "Basic Hourly")

        # rate of pay
        canvas.drawString(100, 885, "Rate")
        canvas.drawString(100, 865, "€ " + str(pay_rate))
        # hours worked
        canvas.drawString(150, 885, "Hours")
        canvas.drawString(150, 865, str(hours_worked))
        # gross income
        canvas.drawString(200, 885, "Earnings")
        canvas.drawString(200, 865, str(gross_pay))
        #Deductions
        canvas.line(0, 830, 250, 830)
        canvas.drawString(0, 835, "Total Deductions")
        #This Period
        canvas.drawString(100, 820, "This Period")
        #Year to date
        canvas.drawString(200, 820, "Year to Date")
        # description
        canvas.drawString(0, 820, "Description")
        #paye
        canvas.drawString(0, 800, "Paye ")
        canvas.drawString(100, 800, "€ " + str(Paye_Tax))
        canvas.drawString(200, 800, "€ " + str(Paye_Total))
        # prsi
        canvas.drawString(0,780,"Prsi")
        canvas.drawString(100, 780, "€ " + str(Prsi_Tax))
        canvas.drawString(200, 780, "€ " + str(Prsi_Total))
        # usc
        canvas.drawString(0, 760, "Usc")
        canvas.drawString(100, 760, "€ " + str(Usc_Tax))
        canvas.drawString(200, 760, "€ " + str(Usc_Total))
        # total deductions
        canvas.drawString(0, 740, "Total Deductions")
        canvas.drawString(100, 740, "€ " + str(Total_Deductions))
        canvas.drawString(200, 740, "€ " + str(Total_Deductions_Year))
        # net income
        canvas.line(0, 712, 250, 712)
        canvas.drawString(0, 715, "Net Pay")
        canvas.drawString(200, 715, "€ " + str(Net_Income))



        canvas.save()



    def display_last_3():
        gui=Tk()
        gui.title('Last 3 MONTHS')

        gui.geometry("1920x1080")
        style = ttk.Style()

        # Pick A Theme
        style.theme_use('default')

        # Configure the Treeview Colors
        style.configure("Treeview",
                        background="#1a1919",
                        foreground="black",
                        rowheight=25,
                        fieldbackground="#1a1919")

        # Change Selected Color
        style.map('Treeview',
                  background=[('selected', "#2f5f6e")])

        # Create a Treeview Frame
        tree_frame = Frame(gui)
        tree_frame.pack(pady=10)

        # Create a Treeview Scrollbar
        treeview_scrollbar = Scrollbar(tree_frame)
        treeview_scrollbar.pack(side=RIGHT, fill=Y)

        # Create The Treeview
        my_tree = ttk.Treeview(tree_frame, yscrollcommand=treeview_scrollbar.set, selectmode="extended")
        my_tree.pack()

        # Configure the Scrollbar
        treeview_scrollbar.config(command=my_tree.yview)

        # Define Our Columns
        my_tree['columns'] = ("Emp_Id", "Gross Income", "Paye", "Prsi", "Usc", "Total Deductions", "Net Income", "Date Created")

        # Format Our Columns
        my_tree.column("#0", width=0, stretch=NO)
        my_tree.column("Emp_Id", anchor=CENTER, width=100)
        my_tree.column("Gross Income", anchor=W, width=140)
        my_tree.column("Paye", anchor=W, width=140)
        my_tree.column("Prsi", anchor=CENTER, width=140)
        my_tree.column("Usc", anchor=CENTER, width=150)
        my_tree.column("Total Deductions", anchor=CENTER, width=100)
        my_tree.column("Net Income", anchor=CENTER, width=140)
        my_tree.column("Date Created", anchor=CENTER, width=140)

        # Create Headings
        my_tree.heading("#0", text="", anchor=W)
        my_tree.heading("Emp_Id", text="Emp_Id", anchor=W)
        my_tree.heading("Gross Income", text="Gross Income", anchor=W)
        my_tree.heading("Paye", text="Paye", anchor=CENTER)
        my_tree.heading("Prsi", text="Prsi", anchor=CENTER)
        my_tree.heading("Usc", text="Usc", anchor=CENTER)
        my_tree.heading("Total Deductions", text="Total Deductions", anchor=CENTER)
        my_tree.heading("Net Income", text="Net Income", anchor=CENTER)
        my_tree.heading("Date Created", text="Date Created", anchor=CENTER)
        conn = sqlite3.connect('Employee_Hours.db')
        c = conn.cursor()

        c.execute("""SELECT * FROM Pay WHERE Emp_ID = :emp_id ORDER BY Date_Created DESC LIMIT 3
                            """,
                  {
                      "emp_id": Emp_id_entry.get(),
                  }
                  )
        records = c.fetchall()
        #global count
        count = 0
        for record in records:
            if count % 2 == 0:
                my_tree.insert(parent='', index='end', iid=count, text='',
                               values=(
                               record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7]),
                               tags=('evenrow',))
            else:
                my_tree.insert(parent='', index='end', iid=count, text='',
                               values=(
                               record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7]),
                               tags=('oddrow',))
            # increment counter
            count += 1



        gui.mainloop()








        conn.commit()

        conn.close()

    button_frame = LabelFrame(root, text="Options")
    button_frame.pack(fill="x", expand="yes", padx=40)

    update_button = Button(button_frame, text="Update Record", command=Update_record)
    update_button.grid(row=0, column=0, padx=10, pady=10)

    add_button = Button(button_frame, text="Add Record", command=Add_Record)
    add_button.grid(row=0, column=1, padx=10, pady=10)

    remove_all_button = Button(button_frame, text="Remove All Records", command=Remove_all)
    remove_all_button.grid(row=0, column=2, padx=10, pady=10)

    remove_one_button = Button(button_frame, text="Remove One Selected", command=Remove_one)
    remove_one_button.grid(row=0, column=3, padx=10, pady=10)

    remove_many_button = Button(button_frame, text="Remove Selected", command=Remove_many)
    remove_many_button.grid(row=0, column=4, padx=10, pady=10)

    move_up_button = Button(button_frame, text="Move Up", command=Record_up)
    move_up_button.grid(row=0, column=5, padx=10, pady=10)

    move_down_button = Button(button_frame, text="Move Down", command=Record_Down)
    move_down_button.grid(row=0, column=6, padx=10, pady=10)

    select_record_button = Button(button_frame, text="Clear Record", command=Clear_entries)
    select_record_button.grid(row=0, column=7, padx=10, pady=10)

    wage_button = Button(button_frame, text="Wage", command=calculatewage)
    wage_button.grid(row=0, column=8, padx=10, pady=10)

    wage_button = Button(button_frame, text="Cummalative", command=display_last_3)
    wage_button.grid(row=0, column=9, padx=10, pady=10)

    # binding
    my_tree.bind('<ButtonRelease-1>', select_record)



    # Add Buttons


    Query_database()
    root.mainloop()



    






