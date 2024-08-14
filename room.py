from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
from datetime import datetime
import re
import random

class Room:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1150x470+200+230")
        self.root.resizable(False,False)
        self.root.title("Room Booking System")



        #=================== variables =================
        self.contactVar = StringVar()
        self.checkInVar = StringVar()
        self.checkOutVar = StringVar()
        self.roomTypeVar = StringVar()
        self.availRoomVar = StringVar()
        self.mealVar = StringVar()
        self.noOfDayVar =StringVar()
        self.paidTaxVar = StringVar()
        self.subTotalVar = StringVar()
        self.totalCostVar = StringVar()

        # ================= roombookinroomTitle=============
        self.roomTitle = Label(self.root, text="Room Booking Details", font=("times new roman", 30, "bold"),
                                   fg="gold", bg="black")
        self.roomTitle.place(x=0, y=0, width=1150, height=50)

        # ====================logo===================
        imgLogo = Image.open(r"Image\logo.jpg")
        imgLogo = imgLogo.resize((150, 48))
        self.logo_image1 = ImageTk.PhotoImage(imgLogo)  # Keep a reference to the image

        self.logo_label1 = Label(self.root, image=self.logo_image1, bd=0, relief=RIDGE)
        self.logo_label1.place(x=50, y=0)


        # ===============lable frame left =============
        self.lableFrameLeft = LabelFrame(self.root, text="Room Booking", font=("times new roman", 14, "bold"), bd=3,
                                         padx=2)
        self.lableFrameLeft.place(x=5, y=50, width=360, height=415)

        self.contact = Label(self.lableFrameLeft, text="Customer Contact", font=("arial", 10, "bold"), padx=2, pady=4)
        self.contact.grid(row=0, column=0, sticky=W)
        self.contactEntry = ttk.Entry(self.lableFrameLeft,textvariable=self.contactVar, font=("arial", 10, "bold"),width=20)
        self.contactEntry.grid(row=0, column=1,sticky=W)

        #fetch button

        self.fetchButton = Button(self.lableFrameLeft, command=self.FetchContact,cursor="hand2", text="Fetch",
                                font=("arial", 8, "bold"), fg="gold", bg="black", width=7)
        self.fetchButton.place(x=270,y=2)

        self.checkIn = Label(self.lableFrameLeft, text="Check_in", font=("arial", 10, "bold"), padx=2, pady=4)
        self.checkIn.grid(row=1, column=0, sticky=W)
        self.checkInEntry = ttk.Entry(self.lableFrameLeft, textvariable=self.checkInVar,font=("arial", 10, "bold"),
                                       width=30)
        self.checkInEntry.grid(row=1, column=1)

        self.checkOut = Label(self.lableFrameLeft, text="Check_out", font=("arial", 10, "bold"), padx=2, pady=4)
        self.checkOut.grid(row=2, column=0, sticky=W)
        self.checkOutEntry = ttk.Entry(self.lableFrameLeft,textvariable=self.checkOutVar, font=("arial", 10, "bold"),width=30)
        self.checkOutEntry.grid(row=2, column=1)

        self.roomType = Label(self.lableFrameLeft, text="RoomType", font=("arial", 10, "bold"), padx=2, pady=4)
        self.roomType.grid(row=3, column=0, sticky=W)
        self.combo_roomType = ttk.Combobox(self.lableFrameLeft,textvariable=self.roomTypeVar,
                                         font=("arial", 10, "bold"), state="readonly", width=27)
        self.combo_roomType["values"] = ("Single", "Double", "Laxary")
        self.combo_roomType.current(0)
        self.combo_roomType.grid(row=3, column=1)
        self.combo_roomType.bind("<<ComboboxSelected>>", self.update_available_rooms)



        self.fetchButton = Button(self.lableFrameLeft, text="Fetch Available Rooms", command=self.fetch_available_rooms)



        self.availRoom = Label(self.lableFrameLeft, text="Available Room", font=("arial", 10, "bold"), padx=2, pady=4)
        self.availRoom.grid(row=4, column=0, sticky=W)


        self.combo_availRoom = ttk.Combobox(self.lableFrameLeft, textvariable=self.availRoomVar,
                                           font=("arial", 10, "bold"), state="readonly", width=27)
        self.combo_availRoom.grid(row=4, column=1)


        self.meal = Label(self.lableFrameLeft, text="Meal", font=("arial", 10, "bold"), padx=2, pady=4)
        self.meal.grid(row=5, column=0, sticky=W)
        self.combo_meal = ttk.Combobox(self.lableFrameLeft, textvariable=self.mealVar,
                                           font=("arial", 10, "bold"), state="readonly", width=27)
        self.combo_meal["values"] = ("Breakfast", "Launch", "Dinner")
        self.combo_meal.current(0)
        self.combo_meal.grid(row=5, column=1)




        self.noOfDay = Label(self.lableFrameLeft, text="No Off Days",font=("arial", 10, "bold"), padx=2, pady=4)
        self.noOfDay.grid(row=6, column=0, sticky=W)
        self.noOfDayEntry = ttk.Entry(self.lableFrameLeft,text="b",state="readonly", font=("arial", 10, "bold"),textvariable=self.noOfDayVar,
                                     width=30)
        self.noOfDayEntry.grid(row=6, column=1)

        self.paidTax = Label(self.lableFrameLeft, text="Paid Tax", font=("arial", 10, "bold"), padx=2, pady=4)
        self.paidTax.grid(row=7, column=0, sticky=W)
        self.paidTaxEntry = ttk.Entry(self.lableFrameLeft, state="readonly",textvariable=self.paidTaxVar, font=("arial", 10, "bold"),
                                    width=30)
        self.paidTaxEntry.grid(row=7, column=1)

        self.subTotal = Label(self.lableFrameLeft, text="Sub Total", font=("arial", 10, "bold"), padx=2, pady=4)
        self.subTotal.grid(row=8, column=0, sticky=W)
        self.subTotalEntry = ttk.Entry(self.lableFrameLeft,state="readonly", textvariable=self.subTotalVar,font=("arial", 10, "bold"),
                                       width=30)
        self.subTotalEntry.grid(row=8, column=1)

        self.totalCost = Label(self.lableFrameLeft, text="Total Cost", font=("arial", 10, "bold"), padx=2, pady=4)
        self.totalCost.grid(row=9, column=0, sticky=W)
        self.totalCostEntry = ttk.Entry(self.lableFrameLeft,state="readonly",textvariable=self.totalCostVar, font=("arial", 10, "bold"),
                                       width=30)
        self.totalCostEntry.grid(row=9, column=1)


        #=====bil button =========
        self.billButton = Button(self.lableFrameLeft,command=self.bill,cursor="hand2",width=8,text="Bill",font=("arial",10,"bold"),bg="black",fg="gold")
        self.billButton.grid(row=12,column=0,padx=3,sticky=W)

        # ================ button frame =========================

        self.buttonFrame = Frame(self.lableFrameLeft, bd=2, relief=RIDGE)
        self.buttonFrame.place(x=5, y=345, width=335, height=30)

        self.addButton = Button(self.buttonFrame, command=self.add_data, cursor="hand2", text="ADD",
                                font=("arial", 10, "bold"), fg="gold", bg="black", width=9)
        self.addButton.grid(row=0, column=0)

        self.updateButton = Button(self.buttonFrame,command=self.update,  text="UPDATE", cursor="hand2",
                                   font=("arial", 10, "bold"), fg="gold", bg="black", width=9, padx=4)
        self.updateButton.grid(row=0, column=1)

        self.deleteButton = Button(self.buttonFrame, command=self.delete, text="DELETE", cursor="hand2",
                                   font=("arial", 10, "bold"), fg="gold", bg="black", width=9)
        self.deleteButton.grid(row=0, column=2)

        self.resetButton = Button(self.buttonFrame,text="RESET",command=self.reset, cursor="hand2",
                                  font=("arial", 10, "bold"), fg="gold", bg="black", width=9)
        self.resetButton.grid(row=0, column=4)


        #=============== table up image ========================
        imgBed = Image.open(r"Image\bed.jpg")
        imgBed = imgBed.resize((490,200))
        self.logo_image2 = ImageTk.PhotoImage(imgBed)  # Keep a reference to the image

        self.logo_label2 = Label(self.root, image=self.logo_image2, bd=0, relief=RIDGE)
        self.logo_label2.place(x=650, y=55)

        # ========================= table frame ======================
        self.tableFrame = LabelFrame(self.root, text="View Details and searching system", bd=3, relief=RIDGE,
                                     font=("times new roman", 14, "bold"))
        self.tableFrame.place(x=370, y=200, width=776, height=265)

        self.searchByL = Label(self.tableFrame, text="Search by", font=("times new roman", 14, "bold"), fg="pink",
                               bg="black")
        self.searchByL.grid(row=0, column=0, padx=5)

        self.combo_searchVar = StringVar()
        self.txtSearchEntryVar = StringVar()

        self.combo_search = ttk.Combobox(self.tableFrame, textvariable=self.combo_searchVar,
                                         font=("times new roman", 10, "bold"), width=15, state="readonly")
        self.combo_search["value"] = ("mobile", "bookedRoom")
        self.combo_search.current(1)
        self.combo_search.grid(row=0, column=1, padx=4)

        self.txtSearchEntry = Entry(self.tableFrame, textvariable=self.txtSearchEntryVar,
                                    font=("times new roman", 14, "bold"), width=25)
        self.txtSearchEntry.grid(row=0, column=2, padx=20)

        self.searchButton = Button(self.tableFrame, command=self.search,cursor="hand2", text="Search", width=12,
                                   font=("times new roman", 10, "bold"), fg="gold", bg="black")
        self.searchButton.grid(row=0, column=3, padx=5)

        self.showAllButton = Button(self.tableFrame,command=self.data_fetch, cursor="hand2", text="Show All", width=12,
                                    font=("times new roman", 10, "bold"), fg="gold", bg="black")
        self.showAllButton.grid(row=0, column=4, padx=10)


        #============== table data show===========================

        self.tableDetails = Frame(self.tableFrame, bd=3, relief=RIDGE, )
        self.tableDetails.place(x=3, y=30, width=760, height=200)

        # +================= scroll bar++++++++++++++++++

        self.x_scroll = ttk.Scrollbar(self.tableDetails, orient=HORIZONTAL)
        self.y_scroll = ttk.Scrollbar(self.tableDetails, orient=VERTICAL)

        self.cust_details_view = ttk.Treeview(self.tableDetails,
                                              columns=("mobile", "checkIn", "checkOut", "roomType",
                                                       "bookedRoom", "Meal", "noOffDay"),
                                              xscrollcommand=self.x_scroll.set, yscrollcommand=self.y_scroll.set)
        self.x_scroll.pack(side=BOTTOM, fill=X)
        self.y_scroll.pack(side=RIGHT, fill=Y)
        self.x_scroll.config(command=self.cust_details_view.xview)
        self.y_scroll.config(command=self.cust_details_view.yview)

        self.cust_details_view.heading("mobile", text="Mobile")
        self.cust_details_view.heading("checkIn", text="Check In")
        self.cust_details_view.heading("checkOut", text="Check Out")
        self.cust_details_view.heading("roomType", text="Room Type")
        self.cust_details_view.heading("bookedRoom", text="Booked Room")
        self.cust_details_view.heading("Meal", text="Meal")
        self.cust_details_view.heading("noOffDay", text="No Off Days")

        self.cust_details_view["show"] = "headings"

        self.cust_details_view.column("mobile", width=150)
        self.cust_details_view.column("checkIn", width=150)
        self.cust_details_view.column("checkOut", width=150)
        self.cust_details_view.column("roomType", width=150)
        self.cust_details_view.column("bookedRoom", width=150)
        self.cust_details_view.column("Meal", width=150)
        self.cust_details_view.column("noOffDay", width=150)
        self.cust_details_view["show"] = "headings"

        self.cust_details_view.pack(fill=BOTH, expand=1)
        self.showDataFrame = Frame(self.root, bd=4, relief=RIDGE, padx=2)
        self.showDataFrame.place(x=370, y=50, width=274, height=155)
        self.cust_details_view.bind("<ButtonRelease-1>", self.getCursor)
        self.data_fetch()

    def FetchContact(self):
        if self.contactVar.get() == "":
            messagebox.showerror("Error", "Fill number field", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="", database="hotel")
                cursor = conn.cursor()
                cursor.execute(
                    "SELECT custName, address, email, custGender, postCode, nationality, idNumber FROM htable WHERE mobile=%s",
                    (self.contactVar.get(),))
                number = self.contactVar.get()
                row = cursor.fetchone()

                if row is None:
                    messagebox.showwarning("Warning", "Not found, please fill up Add Customer details form", parent=self.root)
                else:
                    self.reset()
                    self.contactVar.set(number)
                    custName, address, email, custGender, postCode, nationality, idNumber = row

                    Nlabel = Label(self.showDataFrame, text=f"Customer Name\t: {custName}")
                    Nlabel.grid(row=0, column=0, sticky='w')
                    Glabel = Label(self.showDataFrame, text=f"Gender\t\t: {custGender}")
                    Glabel.grid(row=1, column=0, sticky='w')
                    Alabel = Label(self.showDataFrame, text=f"Address\t\t: {address}")
                    Alabel.grid(row=2, column=0, sticky='w')
                    Plabel = Label(self.showDataFrame, text=f"Post Code\t: {postCode}")
                    Plabel.grid(row=3, column=0, sticky='w')
                    Elabel = Label(self.showDataFrame, text=f"Email\t\t: {email}")
                    Elabel.grid(row=4, column=0, sticky='w')
                    Ntlabel = Label(self.showDataFrame, text=f"Nationality\t: {nationality}")
                    Ntlabel.grid(row=5, column=0, sticky='w')
                    Ilabel = Label(self.showDataFrame, text=f"Id Number\t: {idNumber}")
                    Ilabel.grid(row=6, column=0, sticky='w')

            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"Error connecting to the database: {err}", parent=self.root)
            finally:
                if conn.is_connected():
                    cursor.close()
                    conn.close()

    def reset(self):
        self.contactVar.set("")
        self.checkInVar.set("")
        self.roomTypeVar.set("Single")
        self.fetch_available_rooms()
        self.checkOutVar.set("")
        self.mealVar.set("Breakfast")
        self.noOfDayVar.set("")
        self.paidTaxVar.set("")
        self.subTotalVar.set("")
        self.totalCostVar.set("")


        if self.showDataFrame:
            self.showDataFrame.destroy()
            self.showDataFrame = None
            self.showDataFrame = Frame(self.root, bd=4, relief=RIDGE, padx=2)
            self.showDataFrame.place(x=370, y=50, width=274, height=155)
    def bill(self):
        if self.checkInVar.get()=="" or self.checkOutVar.get()=="" or self.availRoomVar.get()=="" or self.contactVar.get()=="":
            messagebox.showerror("Error","All field are required",parent=self.root)
        else:
            try:
                start_date = self.checkInVar.get()
                end_date = self.checkOutVar.get()
                if end_date>start_date:


                    start_date_obj = datetime.strptime(start_date, "%d/%m/%Y")
                    end_date_obj = datetime.strptime(end_date, "%d/%m/%Y")


                    date_difference = end_date_obj - start_date_obj
                    day=date_difference.days
                    self.noOfDayVar.set(day)
                    if self.roomTypeVar.get() == "Single" and self.mealVar.get() == "Breakfast":
                        single = 1000
                        breakfast = 600
                        pTx = (((single + breakfast) * 0.1 )* day)
                        self.paidTaxVar.set(pTx)
                        subTotal = (single+breakfast)*day
                        total = subTotal+pTx
                        self.subTotalVar.set(subTotal)
                        self.totalCostVar.set(total)
                    elif self.roomTypeVar.get() == "Single" and self.mealVar.get() == "Launch":
                        single = 1000
                        launch = 1200
                        pTx = (((single + launch) * 0.1 )* day)
                        self.paidTaxVar.set(pTx)
                        subTotal = (single+launch)*day
                        total = subTotal+pTx
                        self.subTotalVar.set(subTotal)
                        self.totalCostVar.set(total)
                    elif self.roomTypeVar.get() == "Single" and self.mealVar.get() == "Dinner":
                        single = 1000
                        dinner = 1000
                        pTx = (((single + dinner) * 0.1 )* day)
                        self.paidTaxVar.set(pTx)
                        subTotal = (single+dinner)*day
                        total = subTotal+pTx
                        self.subTotalVar.set(subTotal)
                        self.totalCostVar.set(total)
                    elif self.roomTypeVar.get() == "Double" and self.mealVar.get() == "Breakfast":
                        double = 1600
                        breakfast = 600
                        pTx = (((double + breakfast) * 0.1) * day)
                        self.paidTaxVar.set(pTx)
                        subTotal = (double+breakfast)*day
                        total = subTotal+pTx
                        self.subTotalVar.set(subTotal)
                        self.totalCostVar.set(total)
                    elif self.roomTypeVar.get() == "Double" and self.mealVar.get() == "Launch":
                        double = 1600
                        launch = 1200
                        pTx = (((double + launch) * 0.1 )* day)
                        self.paidTaxVar.set(pTx)
                        subTotal = (double+launch)*day
                        total = subTotal+pTx
                        self.subTotalVar.set(subTotal)
                        self.totalCostVar.set(total)

                    elif self.roomTypeVar.get() == "Double" and self.mealVar.get() == "Dinner":
                        double = 1600
                        dinner = 1000
                        pTx = (((double + dinner) * 0.1 )* day)
                        self.paidTaxVar.set(pTx)
                        subTotal = (double+dinner)*day
                        total = subTotal+pTx
                        self.subTotalVar.set(subTotal)
                        self.totalCostVar.set(total)
                    elif self.roomTypeVar.get() == "Laxary" and self.mealVar.get() == "Breakfast":
                        laxary = 2000
                        breakfast = 600
                        pTx = (((laxary + breakfast) * 0.1 )* day)
                        self.paidTaxVar.set(pTx)
                        subTotal = (laxary+breakfast)*day
                        total = subTotal+pTx
                        self.subTotalVar.set(subTotal)
                        self.totalCostVar.set(total)
                    elif self.roomTypeVar.get() == "Laxary" and self.mealVar.get() == "Launch":
                        laxary = 2000
                        launch = 1200
                        pTx = (((laxary + launch) * 0.1)* day)
                        self.paidTaxVar.set(pTx)
                        subTotal = (laxary+launch)*day
                        total = subTotal+pTx
                        self.subTotalVar.set(subTotal)
                        self.totalCostVar.set(total)
                    elif self.roomTypeVar.get() == "Laxary" and self.mealVar.get() == "Dinner":
                        laxary = 2000
                        dinner = 1000
                        pTx = (((laxary + dinner) * 0.1 )* day)
                        self.paidTaxVar.set(pTx)
                        subTotal = (laxary+dinner)*day
                        total = subTotal+pTx
                        self.subTotalVar.set(subTotal)
                        self.totalCostVar.set(total)
                else:
                    messagebox.showerror("Error","invalid input")


            except Exception:
                messagebox.showerror("Error","Enter date dd/mm/yyyy this format")

    def fetch_available_rooms(self):
        try:
            conn = mysql.connector.connect(host="localhost", username="root", password="", database="hotel")
            cursor = conn.cursor()

            room_type = self.roomTypeVar.get()
            cursor.execute("SELECT roomNo FROM roomdetails WHERE roomType = %s", (room_type,))
            rows = cursor.fetchall()

            if rows:
                available_rooms = [row[0] for row in rows]
                self.combo_availRoom["values"] = available_rooms
                self.combo_availRoom.current(0)
            else:
                messagebox.showwarning("No Rooms Found", "No rooms available for the selected room type.")

        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error connecting to the database: {err}")

        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    def update_available_rooms(self, event):
        self.fetch_available_rooms()


    def add_data(self):
        if self.contactVar.get()=="" or self.checkInVar.get()=="" or self.checkOutVar.get()=="" or self.roomTypeVar.get()=="" or self.availRoomVar.get()=="" or self.mealVar.get()=="" or self.noOfDayVar.get()=="" "":
            messagebox.showerror("Error","All fields are required",parent=self.root)


        else:
            try:
                conn = mysql.connector.connect(host="localhost",username="root",password="",database="hotel")
                cursor = conn.cursor()
                cursor.execute("insert into roomBooking values (%s,%s,%s,%s,%s,%s,%s)",
                                (self.contactVar.get(),
                                self.checkInVar.get(),
                                self.checkOutVar.get(),
                                self.roomTypeVar.get(),
                                self.availRoomVar.get(),
                                self.mealVar.get(),
                                self.noOfDayVar.get(),
                                ))


                self.contactVar.set("")
                self.checkInVar.set("")
                self.checkOutVar.set("")
                self.roomTypeVar.set("Single")
                self.fetch_available_rooms()
                self.mealVar.set("Breakfast")
                self.noOfDayVar.set("")
                self.paidTaxVar.set("")
                self.subTotalVar.set("")
                self.totalCostVar.set("")


                conn.commit()
                self.data_fetch()
                conn.close()
                messagebox.showinfo("Success","Information has bend added",parent=self.root)
                self.reset()

            except Exception as e:
                messagebox.showerror("Error",f"Something went wrong {e}",parent=self.root)
    def data_fetch(self):
        try:
            conn = mysql.connector.connect(host="localhost", username="root", password="", database="hotel")
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM roomBooking")
            rows = cursor.fetchall()
            if len(rows)==0:
                self.cust_details_view.delete(*self.cust_details_view.get_children())
            if len(rows) != 0:
                self.cust_details_view.delete(*self.cust_details_view.get_children())
                for row in rows:
                    self.cust_details_view.insert("", END, values=row)
                conn.commit()
            conn.close()
        except Exception as e:
            messagebox.showerror("Error", f"Something went wrong: {e}",parent=self.root)

    def getCursor(self, event=""):
        cursorRow = self.cust_details_view.focus()
        content = self.cust_details_view.item(cursorRow)
        row = content["values"]
        if len(row)!=0:
            self.contactVar.set("0"+str(row[0]))
            self.checkInVar.set(row[1])
            self.checkOutVar.set(row[2])
            self.roomTypeVar.set(row[3])
            self.availRoomVar.set(row[4])
            self.mealVar.set(row[5])
            self.noOfDayVar.set(row[6])

    def update(self):
        if self.contactVar.get()=="" or self.checkInVar.get()=="" or self.checkOutVar.get()=="" or self.roomTypeVar.get()=="" or self.availRoomVar.get()=="" or self.mealVar.get()=="" or self.noOfDayVar.get()=="" "":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost",username="root",password="",database="hotel")
                cursor = conn.cursor()
                cursor.execute("UPDATE roomBooking SET checkIn=%s, checkOut=%s, roomType=%s, bookedRoom=%s, Meal=%s, noOffDay=%s WHERE mobile=%s",
                               (self.checkInVar.get(),
                                self.checkOutVar.get(),
                                self.roomTypeVar.get(),
                                self.availRoomVar.get(),
                                self.mealVar.get(),
                                self.noOfDayVar.get(),
                                self.contactVar.get()))
                conn.commit()
                self.data_fetch()
                conn.close()
                messagebox.showinfo("Success","Information has been updated",parent=self.root)

            except Exception as e:
                messagebox.showerror("Error",f"Something went wrong {e}",parent=self.root)

    def delete(self):
        # Ask for confirmation before deleting
        delete = messagebox.askyesno("Hotel Management System", "Do you want to delete?", parent=self.root)
        if delete > 0:
            try:
                # Establish connection to the database
                conn = mysql.connector.connect(host="localhost", username="root", password="", database="hotel")
                cursor = conn.cursor()

                # Execute delete query using the mobile number from self.contactVar
                cursor.execute("DELETE FROM roomBooking WHERE mobile = %s", (self.contactVar.get(),))

                # Show success message and refresh data
                messagebox.showinfo("Success", "Record deleted successfully", parent=self.root)
                conn.commit()
                self.data_fetch()
            except Exception as e:
                # Show error message in case of an exception
                messagebox.showerror("Error", f"Something went wrong: {e}", parent=self.root)
            finally:
                # Ensure that the connection is closed properly
                conn.close()
        else:
            return

    def search(self):
        try:
            conn = mysql.connector.connect(host="localhost", username="root", password="", database="hotel")
            cursor = conn.cursor()

            # Assuming combo_searchVar selects the column name like 'roomNo'
            column_name = str(self.combo_searchVar.get())
            query = f"SELECT * FROM roomBooking WHERE {column_name} LIKE %s"

            cursor.execute(query, ('%' + str(self.txtSearchEntryVar.get()) + '%',))
            rows = cursor.fetchall()

            if rows:
                self.cust_details_view.delete(*self.cust_details_view.get_children())
                for row in rows:
                    self.cust_details_view.insert("", "end", values=row)

            conn.commit()
        except Exception as e:
            messagebox.showerror("Error", f"Something went wrong: {e}", parent=self.root)
        finally:
            conn.close()


