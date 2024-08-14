from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
import re
import random


class AddRoom:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1150x470+200+230")
        self.root.resizable(False,False)
        self.root.title("Room Add System")


        #========== variables ============
        self.floorNumberVar = StringVar()
        self.roomNumberVar = StringVar()
        self.roomTypeVar = StringVar()

        # ================= roombookinroomTitle=============
        self.addRoomTitle = Label(self.root, text="Room Details", font=("times new roman", 30, "bold"),
                               fg="gold", bg="black")
        self.addRoomTitle.place(x=0, y=0, width=1150, height=50)

        # ====================logo===================
        imgLogo = Image.open(r"Image\logo.jpg")
        imgLogo = imgLogo.resize((150, 48))
        self.logo_image1 = ImageTk.PhotoImage(imgLogo)  # Keep a reference to the image

        self.logo_label1 = Label(self.root, image=self.logo_image1, bd=0, relief=RIDGE)
        self.logo_label1.place(x=50, y=0)

        # ===============lable frame left =============

        self.lableFrameLeft = LabelFrame(self.root, text="Add Room", font=("times new roman", 14, "bold"), bd=3,
                                         padx=2)
        self.lableFrameLeft.place(x=5, y=50, width=360, height=300)

        self.floorNumber = Label(self.lableFrameLeft, text="Floor No", font=("arial", 10, "bold"), padx=2, pady=4)
        self.floorNumber.grid(row=0, column=0, sticky=W)
        self.floorNumberEntry = ttk.Entry(self.lableFrameLeft, textvariable=self.floorNumberVar,font=("arial", 10, "bold"),
                                         width=20)
        self.floorNumberEntry.grid(row=0, column=1, sticky=W)

        self.roomNumber = Label(self.lableFrameLeft, text="Room No", font=("arial", 10, "bold"), padx=2, pady=4)
        self.roomNumber.grid(row=1, column=0, sticky=W)
        self.roomNumberEntry = ttk.Entry(self.lableFrameLeft, textvariable=self.roomNumberVar,font=("arial", 10, "bold"),
                                      width=20)
        self.roomNumberEntry.grid(row=1, column=1, sticky=W)

        self.roomType = Label(self.lableFrameLeft, text="Room Type", font=("arial", 10, "bold"), padx=2, pady=4)
        self.roomType.grid(row=2, column=0, sticky=W)
        self.combo_roomType = ttk.Combobox(self.lableFrameLeft,textvariable=self.roomTypeVar,
                                           font=("arial", 10, "bold"), state="readonly", width=27)
        self.combo_roomType["values"] = ("Single", "Double", "Laxary")
        self.combo_roomType.current(0)
        self.combo_roomType.grid(row=2, column=1)

        # ================ button frame =========================

        self.buttonFrame = Frame(self.lableFrameLeft, bd=2, relief=RIDGE)
        self.buttonFrame.place(x=5, y=180, width=335, height=30)

        self.addButton = Button(self.buttonFrame,command=self.add_data, cursor="hand2", text="ADD",
                                font=("arial", 10, "bold"), fg="gold", bg="black", width=9)
        self.addButton.grid(row=0, column=0)

        self.updateButton = Button(self.buttonFrame,command=self.update, text="UPDATE", cursor="hand2",
                                   font=("arial", 10, "bold"), fg="gold", bg="black", width=9, padx=4)
        self.updateButton.grid(row=0, column=1)

        self.deleteButton = Button(self.buttonFrame,command=self.delete, text="DELETE", cursor="hand2",
                                   font=("arial", 10, "bold"), fg="gold", bg="black", width=9)
        self.deleteButton.grid(row=0, column=2)

        self.resetButton = Button(self.buttonFrame,command=self.reset, text="RESET", cursor="hand2",
                                  font=("arial", 10, "bold"), fg="gold", bg="black", width=9)
        self.resetButton.grid(row=0, column=4)

        # ==============table details==============================
        self.tableDetails = Frame(self.root, bd=3, relief=RIDGE, )
        self.tableDetails.place(x=380, y=60, width=760, height=290)

        # +================= scroll bar++++++++++++++++++

        self.x_scroll = ttk.Scrollbar(self.tableDetails, orient=HORIZONTAL)
        self.y_scroll = ttk.Scrollbar(self.tableDetails, orient=VERTICAL)

        self.room_details_view = ttk.Treeview(self.tableDetails,
                                              columns=("floorNo","roomNo","roomType"),
                                              xscrollcommand=self.x_scroll.set, yscrollcommand=self.y_scroll.set)
        self.x_scroll.pack(side=BOTTOM, fill=X)
        self.y_scroll.pack(side=RIGHT, fill=Y)
        self.x_scroll.config(command=self.room_details_view.xview)
        self.y_scroll.config(command=self.room_details_view.yview)

        self.room_details_view.heading("floorNo", text="Floor No")
        self.room_details_view.heading("roomNo", text="Room No")
        self.room_details_view.heading("roomType", text="Room Type")

        self.room_details_view["show"] = "headings"

        self.room_details_view.column("floorNo", width=150)
        self.room_details_view.column("roomNo", width=150)
        self.room_details_view.column("roomType", width=150)

        self.room_details_view["show"] = "headings"

        self.room_details_view.pack(fill=BOTH, expand=1)
        self.room_details_view.bind("<ButtonRelease-1>", self.getCursor)
        self.data_fetch()


        #======== footer picture =====================
        self.footPic = Frame(self.root, bd=3, relief=RIDGE, )
        self.footPic.place(x=5, y=350, width=1135, height=115)

        imgSingle = Image.open(r"Image\single.jpg")
        imgSingle = imgSingle.resize((375, 115))
        self.logo_image3 = ImageTk.PhotoImage(imgSingle)  # Keep a reference to the image

        self.logo_label3 = Label(self.footPic, image=self.logo_image3, bd=0, relief=RIDGE)
        self.logo_label3.grid(row=0,column=0)

        imgDouble = Image.open(r"Image\double.jpg")
        imgDouble = imgDouble.resize((380, 115))
        self.logo_image4 = ImageTk.PhotoImage(imgDouble)  # Keep a reference to the image

        self.logo_label4 = Label(self.footPic, image=self.logo_image4, bd=0, relief=RIDGE)
        self.logo_label4.grid(row=0, column=1)

        imgLaxary = Image.open(r"Image\laxary.jpg")
        imgLaxary = imgLaxary.resize((375, 115))
        self.logo_image5 = ImageTk.PhotoImage(imgLaxary)  # Keep a reference to the image

        self.logo_label5 = Label(self.footPic, image=self.logo_image5, bd=0, relief=RIDGE)
        self.logo_label5.grid(row=0, column=2)



    def add_data(self):
        if self.floorNumberVar.get()=="" or self.roomNumberVar.get()=="":
            messagebox.showerror("Error", "All fields are required", parent=self.root)


        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="", database="hotel")
                cursor = conn.cursor()
                cursor.execute("insert into roomDetails values (%s,%s,%s)",
                               (self.floorNumberVar.get(),
                                self.roomNumberVar.get(),
                                self.roomTypeVar.get(),

                                ))

                self.floorNumberVar.set("")
                self.roomNumberVar.set("")
                self.roomTypeVar.set("Single")

                conn.commit()
                self.data_fetch()
                conn.close()
                messagebox.showinfo("Success", "Information has bend added", parent=self.root)

            except Exception as e:
                messagebox.showerror("Error", f"Something went wrong {e}", parent=self.root)
    def data_fetch(self):
        try:
            conn = mysql.connector.connect(host="localhost", username="root", password="", database="hotel")
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM roomDetails")
            rows = cursor.fetchall()
            if len(rows)==0:
                self.room_details_view.delete(*self.room_details_view.get_children())
            if len(rows) != 0:
                self.room_details_view.delete(*self.room_details_view.get_children())
                for row in rows:
                    self.room_details_view.insert("", END, values=row)
                conn.commit()
            conn.close()
        except Exception as e:
            messagebox.showerror("Error", f"Something went wrong: {e}",parent=self.root)
    def getCursor(self, event=""):
        cursorRow = self.room_details_view.focus()
        content = self.room_details_view.item(cursorRow)
        row = content["values"]
        if len(row)!=0:
            self.floorNumberVar.set(row[0])
            self.roomNumberVar.set(row[1])
            self.roomTypeVar.set(row[2])

    def reset(self):
        self.floorNumberVar.set("")
        self.roomNumberVar.set("")
        self.roomTypeVar.set("Single")

    def update(self):
        if self.floorNumberVar.get() == "" or self.roomNumberVar.get() == "" or self.roomTypeVar.get() == "":
            messagebox.showwarning("Warning", "All fields are required", parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="", database="hotel")
            cursor = conn.cursor()
            try:
                cursor.execute("""
                    UPDATE roomDetails
                    SET floorNo = %s, roomType = %s
                    WHERE roomNo = %s
                """, (
                    self.floorNumberVar.get(),
                    self.roomTypeVar.get(),
                    self.roomNumberVar.get()
                ))
                conn.commit()
                self.data_fetch()  # Assuming this method refreshes your data display
                messagebox.showinfo("Success", "Information updated successfully", parent=self.root)
            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"Error updating information: {err}", parent=self.root)
            finally:
                conn.close()

    def delete(self):
        delete = messagebox.askyesno("Room Adding System", "Do you want to delete?",parent=self.root)
        if delete > 0:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="", database="hotel")
                cursor = conn.cursor()
                cursor.execute("DELETE FROM roomDetails WHERE roomNo = %s", (self.roomNumberVar.get(),))
                conn.commit()
                messagebox.showinfo("Success", "Record deleted successfully", parent=self.root)
                self.data_fetch()
                conn.close()
            except Exception as e:
                messagebox.showerror("Error", f"Something went wrong: {e}", parent=self.root)
        else:
            return



