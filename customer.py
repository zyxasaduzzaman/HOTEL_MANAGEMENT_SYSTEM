from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
import re
import random


class Customer:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1150x470+200+230")
        self.root.resizable(False,False)
        self.root.title("Customer Add System")


    #============ variables ==========================
        self.custRefVar = StringVar()
        try:
            conn = mysql.connector.connect(
                host='localhost',
                user='root',
                password='',
                database='hotel'
            )

            cursor = conn.cursor()
            cursor.execute("SELECT COUNT(*) FROM htable")
            row_count = int(cursor.fetchone()[0])
            random_number = random.randint(111, 2000)
            row_count+=random_number
            self.custRefVar.set(row_count)
            conn.commit()
            conn.close()

        except Exception as e:
            messagebox.showerror("Error", f"Something went wrong {e}",parent=self.root)
        self.custNameVar = StringVar()
        self.custFNameVar = StringVar()
        self.custMNameVar = StringVar()
        self.custGenderVar = StringVar()
        self.postCodeVar = StringVar()
        self.mobileVar = StringVar()
        self.emailVar = StringVar()
        self.nationalityVar = StringVar()
        self.idProofVar = StringVar()
        self.idNumberVar = StringVar()
        self.addressVar = StringVar()

        #================= add customer details lable=============
        self.cust_detailsL = Label(self.root,text="ADD CUSTOMER DETAILS",font=("times new roman",30,"bold"),fg="gold",bg="black")
        self.cust_detailsL.place(x=0,y=0,width=1150,height=50)

        # ====================logo===================
        img1 = Image.open(r"Image\logo.jpg")
        img1 = img1.resize((150, 48))
        self.logo_image = ImageTk.PhotoImage(img1)  # Keep a reference to the image

        self.logo_label = Label(self.root, image=self.logo_image,bd=0,relief=RIDGE)
        self.logo_label.place(x=150, y=0)
        self.logo_label = Label(self.root, image=self.logo_image, bd=0, relief=RIDGE)
        self.logo_label.place(x=850, y=0)

        #===============lable frame left =============
        self.lableFrameLeft = LabelFrame(self.root,text="CustomerDetails",font=("times new roman",14,"bold"),bd=3,padx=2)
        self.lableFrameLeft.place(x=5,y=50,width=360,height=415)

        self.custRef = Label(self.lableFrameLeft,text="Customer Ref",font=("arial",10,"bold"),padx=2,pady=4)
        self.custRef.grid(row=0,column=0,sticky=W)

        self.custRefEntry = ttk.Entry(self.lableFrameLeft,font=("arial",10,"bold"),textvariable=self.custRefVar,width=30,state="readonly")
        self.custRefEntry.grid(row=0,column = 1)

        self.custName = Label(self.lableFrameLeft, text="Customer Name", font=("arial", 10, "bold"),padx=2,pady=4)
        self.custName.grid(row=1, column=0,sticky=W)
        self.custNameEntry = ttk.Entry(self.lableFrameLeft, textvariable=self.custNameVar,font=("arial", 10, "bold"), width=30)
        self.custNameEntry.grid(row=1, column=1)

        self.custFName = Label(self.lableFrameLeft, text="Father Name", font=("arial", 10, "bold"),padx=2,pady=4)
        self.custFName.grid(row=2, column=0,sticky=W)
        self.custFNameEntry = ttk.Entry(self.lableFrameLeft,textvariable=self.custFNameVar, font=("arial", 10, "bold"), width=30)
        self.custFNameEntry.grid(row=2, column=1)

        self.custMName = Label(self.lableFrameLeft, text="Mother Name", font=("arial", 10, "bold"),padx=2,pady=4)
        self.custMName.grid(row=3, column=0, sticky=W)
        self.custMNameEntry = ttk.Entry(self.lableFrameLeft,textvariable=self.custMNameVar, font=("arial", 10, "bold"), width=30)
        self.custMNameEntry.grid(row=3, column=1)

        self.custGender = Label(self.lableFrameLeft, text="Gender", font=("arial", 10, "bold"),padx=2,pady=4)
        self.custGender.grid(row=4, column=0, sticky=W)
        self.combo_gender= ttk.Combobox(self.lableFrameLeft,textvariable=self.custGenderVar,font=("arial", 10, "bold"),state="readonly",width=27)
        self.combo_gender["values"]=("Male","Female","Other")
        self.combo_gender.current(0)
        self.combo_gender.grid(row=4,column=1)

        self.postCode = Label(self.lableFrameLeft, text="Post Code", font=("arial", 10, "bold"),padx=2,pady=4)
        self.postCode.grid(row=5, column=0, sticky=W)
        self.postCodeEntry = ttk.Entry(self.lableFrameLeft, textvariable=self.postCodeVar,font=("arial", 10, "bold"), width=30)
        self.postCodeEntry.grid(row=5,column=1)


        self.mobile = Label(self.lableFrameLeft, text="Mobile", font=("arial", 10, "bold"),padx=2,pady=4)
        self.mobile.grid(row=6, column=0, sticky=W)
        self.mobileEntry = ttk.Entry(self.lableFrameLeft,textvariable=self.mobileVar, font=("arial", 10, "bold"), width=30)
        self.mobileEntry.grid(row=6, column=1)

        self.email = Label(self.lableFrameLeft, text="Email", font=("arial", 10, "bold"),padx=2,pady=4)
        self.email.grid(row=7, column=0, sticky=W)
        self.emailEntry = ttk.Entry(self.lableFrameLeft, textvariable=self.emailVar,font=("arial", 10, "bold"), width=30)
        self.emailEntry.grid(row=7, column=1)


        self.nationality = Label(self.lableFrameLeft, text="Nationality", font=("arial", 10, "bold"),padx=2,pady=4)
        self.nationality.grid(row=8, column=0, sticky=W)
        self.combo_nationality = ttk.Combobox(self.lableFrameLeft, textvariable=self.nationalityVar,font=("arial", 10, "bold"), state="readonly",width=27)
        self.combo_nationality["value"]= ("Bangladesh", "Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Antigua and Barbuda", "Argentina", "Armenia",
    "Australia", "Austria", "Azerbaijan", "Bahamas", "Bahrain", "Barbados", "Belarus", "Belgium", "Belize", "Benin",
    "Bhutan", "Bolivia", "Bosnia and Herzegovina", "Botswana", "Brazil", "Brunei", "Bulgaria", "Burkina Faso", "Burundi",
    "Cabo Verde", "Cambodia", "Cameroon", "Canada", "Central African Republic", "Chad", "Chile", "China", "Colombia",
    "Comoros", "Congo, Democratic Republic of the", "Congo, Republic of the", "Costa Rica", "Croatia", "Cuba", "Cyprus",
    "Czech Republic", "Denmark", "Djibouti", "Dominica", "Dominican Republic", "Ecuador", "Egypt", "El Salvador",
    "Equatorial Guinea", "Eritrea", "Estonia", "Eswatini", "Ethiopia", "Fiji", "Finland", "France", "Gabon", "Gambia",
    "Georgia", "Germany", "Ghana", "Greece", "Grenada", "Guatemala", "Guinea", "Guinea-Bissau", "Guyana", "Haiti",
    "Honduras", "Hungary", "Iceland", "India", "Indonesia", "Iran", "Iraq", "Ireland", "Israel", "Italy", "Ivory Coast",
    "Jamaica", "Japan", "Jordan", "Kazakhstan", "Kenya", "Kiribati", "Kuwait", "Kyrgyzstan", "Laos", "Latvia", "Lebanon",
    "Lesotho", "Liberia", "Libya", "Liechtenstein", "Lithuania", "Luxembourg", "Madagascar", "Malawi", "Malaysia",
    "Maldives", "Mali", "Malta", "Marshall Islands", "Mauritania", "Mauritius", "Mexico", "Micronesia", "Moldova",
    "Monaco", "Mongolia", "Montenegro", "Morocco", "Mozambique", "Myanmar", "Namibia", "Nauru", "Nepal", "Netherlands",
    "New Zealand", "Nicaragua", "Niger", "Nigeria", "North Korea", "North Macedonia", "Norway", "Oman", "Pakistan",
    "Palau", "Panama", "Papua New Guinea", "Paraguay", "Peru", "Philippines", "Poland", "Portugal", "Qatar", "Romania",
    "Russia", "Rwanda", "Saint Kitts and Nevis", "Saint Lucia", "Saint Vincent and the Grenadines", "Samoa",
    "San Marino", "Sao Tome and Principe", "Saudi Arabia", "Senegal", "Serbia", "Seychelles", "Sierra Leone", "Singapore",
    "Slovakia", "Slovenia", "Solomon Islands", "Somalia", "South Africa", "South Korea", "South Sudan", "Spain",
    "Sri Lanka", "Sudan", "Suriname", "Sweden", "Switzerland", "Syria", "Taiwan", "Tajikistan", "Tanzania", "Thailand",
    "Timor-Leste", "Togo", "Tonga", "Trinidad and Tobago", "Tunisia", "Turkey", "Turkmenistan", "Tuvalu", "Uganda",
    "Ukraine", "United Arab Emirates", "United Kingdom", "United States", "Uruguay", "Uzbekistan", "Vanuatu", "Vatican City",
    "Venezuela", "Vietnam", "Yemen", "Zambia", "Zimbabwe")
        self.combo_nationality.current(0)
        self.combo_nationality.grid(row=8, column=1)

        self.idProof= Label(self.lableFrameLeft, text="Id Proof Type", font=("arial", 10, "bold"),padx=2,pady=4)
        self.idProof.grid(row=9, column=0, sticky=W)
        self.combo_idProof = ttk.Combobox(self.lableFrameLeft,textvariable=self.idProofVar, font=("arial", 10, "bold"), state="readonly", width=27)
        self.combo_idProof["values"] = ("National ID", "Driving Licence", "Passport")
        self.combo_idProof.current(0)
        self.combo_idProof.grid(row=9, column=1)

        self.idNumber = Label(self.lableFrameLeft, text="Id Number", font=("arial", 10, "bold"),padx=2,pady=4)
        self.idNumber.grid(row=10, column=0, sticky=W)
        self.idNumberEntry = ttk.Entry(self.lableFrameLeft, textvariable=self.idNumberVar,font=("arial", 10, "bold"), width=30)
        self.idNumberEntry.grid(row=10, column=1)

        self.address = Label(self.lableFrameLeft, text="Address", font=("arial", 10, "bold"),padx=2,pady=4)
        self.address.grid(row=11, column=0, sticky=W)
        self.addressEntry = ttk.Entry(self.lableFrameLeft,textvariable=self.addressVar, font=("arial", 10, "bold"), width=30)
        self.addressEntry.grid(row=11, column=1)

        #================ button frame =========================

        self.buttonFrame = Frame(self.lableFrameLeft,bd=2,relief=RIDGE)
        self.buttonFrame.place(x=5,y=345,width=335,height=30)

        self.addButton = Button(self.buttonFrame,command=self.add_data,cursor="hand2",text="ADD",font=("arial",10,"bold"),fg="gold",bg="black",width=9)
        self.addButton.grid(row=0,column=0)

        self.updateButton = Button(self.buttonFrame,command=self.update,text="UPDATE",cursor="hand2",font=("arial",10,"bold"),fg="gold",bg="black",width=9,padx=4)
        self.updateButton.grid(row=0,column=1)

        self.deleteButton = Button(self.buttonFrame,command=self.delete,text="DELETE",cursor="hand2",font=("arial",10,"bold"),fg="gold",bg="black",width=9)
        self.deleteButton.grid(row=0,column=2)

        self.resetButton = Button(self.buttonFrame,text="RESET",command=self.reset,cursor="hand2",font=("arial",10,"bold"),fg="gold",bg="black",width=9)
        self.resetButton.grid(row=0,column=4)


        # ========================= table frame ======================
        self.tableFrame =LabelFrame(self.root,text="View Details and searching system",bd=3,relief=RIDGE,font=("times new roman",14,"bold"))
        self.tableFrame.place(x=370,y=50,width=776,height=414)

        self.searchByL = Label(self.tableFrame,text="Search by",font=("times new roman",14,"bold"),fg="pink",bg="black")
        self.searchByL.grid(row = 0 ,column = 0,padx=5)

        self.combo_searchVar = StringVar()
        self.txtSearchEntryVar = StringVar()

        self.combo_search = ttk.Combobox(self.tableFrame,textvariable=self.combo_searchVar,font=("times new roman",10,"bold"),width=15,state="readonly")
        self.combo_search["value"]=("custRef","mobile","custName","email","nationality","address","postCode","idNumber")
        self.combo_search.current(1)
        self.combo_search.grid(row =0 ,column = 1,padx=4)

        self.txtSearchEntry = Entry(self.tableFrame,textvariable=self.txtSearchEntryVar,font=("times new roman",14,"bold"),width=25)
        self.txtSearchEntry.grid(row=0,column=2,padx=20)

        self.searchButton = Button(self.tableFrame,command=self.search,cursor="hand2",text="Search",width=12,font=("times new roman",10,"bold"),fg="gold",bg="black")
        self.searchButton.grid(row=0,column=3,padx=5)

        self.showAllButton= Button(self.tableFrame,cursor="hand2",command=self.data_fetch,text="Show All",width=12,font=("times new roman",10,"bold"),fg="gold",bg="black")
        self.showAllButton.grid(row=0,column=4,padx=10)


        #==============table details==============================
        self.tableDetails = Frame(self.tableFrame,bd=3,relief=RIDGE,)
        self.tableDetails.place(x=3,y=30,width=760,height=300)

        #+================= scroll bar++++++++++++++++++

        self.x_scroll = ttk.Scrollbar(self.tableDetails,orient=HORIZONTAL)
        self.y_scroll =ttk.Scrollbar(self.tableDetails,orient=VERTICAL)

        self.cust_details_view = ttk.Treeview(self.tableDetails,columns=("custRef","custName","custFName","custMName",
                                                                         "custGender","postCode","mobile","email",
                                                                         "nationality","idProof","idNumber","address"),xscrollcommand=self.x_scroll.set,yscrollcommand=self.y_scroll.set)
        self.x_scroll.pack(side=BOTTOM,fill=X)
        self.y_scroll.pack(side=RIGHT,fill=Y)
        self.x_scroll.config(command=self.cust_details_view.xview)
        self.y_scroll.config(command=self.cust_details_view.yview)

        self.cust_details_view.heading("custRef",text="Refer No")
        self.cust_details_view.heading("custName",text="Name")
        self.cust_details_view.heading("custFName",text="Father Name")
        self.cust_details_view.heading("custMName",text="Mother Name")
        self.cust_details_view.heading("custGender",text="Gender")
        self.cust_details_view.heading("postCode",text="Post")
        self.cust_details_view.heading("mobile",text="Mobile")
        self.cust_details_view.heading("email",text="Email")
        self.cust_details_view.heading("nationality",text="Nationality")
        self.cust_details_view.heading("idProof",text="ID Type")
        self.cust_details_view.heading("idNumber",text="ID Number")
        self.cust_details_view.heading("address",text="Address")

        self.cust_details_view["show"]="headings"

        self.cust_details_view.column("custRef", width=150)
        self.cust_details_view.column("custName", width=150)
        self.cust_details_view.column("custFName",width=150)
        self.cust_details_view.column("custMName", width=150)
        self.cust_details_view.column("custGender", width=150)
        self.cust_details_view.column("postCode", width=150)
        self.cust_details_view.column("mobile", width=150)
        self.cust_details_view.column("email", width=150)
        self.cust_details_view.column("nationality", width=150)
        self.cust_details_view.column("idProof", width=150)
        self.cust_details_view.column("idNumber",width=150)
        self.cust_details_view.column("address", width=150)
        self.cust_details_view["show"] = "headings"


        self.cust_details_view.pack(fill=BOTH,expand=1)
        self.cust_details_view.bind("<ButtonRelease-1>", self.getCursor)
        self.data_fetch()
    def add_data(self):
        if self.custNameVar.get()=="" or self.custFNameVar.get()=="" or self.custMNameVar.get()=="" or self.postCodeVar.get()=="" or self.mobileVar.get()=="" or self.emailVar.get()=="" or self.idNumberVar.get()=="" or self.addressVar.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)


        else:
            if self.isNumber(self.mobileVar.get()) and self.isEmail(self.emailVar.get()):
                try:
                    conn = mysql.connector.connect(host="localhost",username="root",password="",database="hotel")
                    cursor = conn.cursor()
                    cursor.execute("insert into htable values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                                   (self.custRefVar.get(),
                                   self.custNameVar.get(),
                                   self.custFNameVar.get(),
                                   self.custMNameVar.get(),
                                   self.custGenderVar.get(),
                                   self.postCodeVar.get(),
                                   self.mobileVar.get(),
                                   self.emailVar.get(),
                                   self.nationalityVar.get(),
                                   self.idProofVar.get(),
                                   self.idNumberVar.get(),
                                   self.addressVar.get()
                                   ))
                    cursor.execute("SELECT COUNT(*) FROM htable")
                    row_count = int(cursor.fetchone()[0])
                    row_count += 1234
                    self.custRefVar.set(row_count)
                    self.custNameVar.set("")
                    self.custFNameVar.set("")
                    self.custFNameVar.set("")
                    self.custMNameVar.set("")
                    self.postCodeVar.set("")
                    self.mobileVar.set("")
                    self.emailVar.set("")
                    self.idNumberVar.set("")
                    self.addressVar.set("")

                    conn.commit()
                    self.data_fetch()
                    conn.close()
                    messagebox.showinfo("Success","Information has bend added",parent=self.root)

                except Exception as e:
                    messagebox.showerror("Error",f"Something went wrong {e}",parent=self.root)
            else:
                messagebox.showerror("Error","Invalid mobile or email",parent=self.root)

    def isNumber(self, number):
        pattern = r'^01[2-9]\d{8}$'
        return re.match(pattern, number)

    def isEmail(self, email):
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email)

    def data_fetch(self):
        try:
            conn = mysql.connector.connect(host="localhost", username="root", password="", database="hotel")
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM htable")
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
            self.custRefVar.set(row[0])
            self.custNameVar.set(row[1])
            self.custFNameVar.set(row[2])
            self.custMNameVar.set(row[3])
            self.custGenderVar.set(row[4])
            self.postCodeVar.set(row[5])
            self.mobileVar.set("0"+str(row[6]))
            self.emailVar.set(row[7])
            self.nationalityVar.set(row[8])
            self.idProofVar.set(row[9])
            self.idNumberVar.set(row[10])
            self.addressVar.set(row[11])

    def reset(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="", database="hotel")
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM htable")
        row_count = int(cursor.fetchone()[0])
        random_number = random.randint(1, 100)
        row_count += random_number
        self.custRefVar.set(row_count)
        self.custNameVar.set("")
        self.custFNameVar.set("")
        self.custMNameVar.set("")
        self.custGenderVar.set("Male")
        self.postCodeVar.set("")
        self.mobileVar.set("")
        self.emailVar.set("")
        self.nationalityVar.set("Bangladesh")
        self.idProofVar.set("National ID")
        self.idNumberVar.set("")
        self.addressVar.set("")
        conn.commit()
        conn.close()

    def delete(self):
        delete = messagebox.askyesno("Hotel Management System", "Do you want to delete?",parent=self.root)
        if delete > 0:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="", database="hotel")
                cursor = conn.cursor()
                cursor.execute("DELETE FROM htable WHERE custRef = %s", (self.custRefVar.get(),))
                conn.commit()
                messagebox.showinfo("Success", "Record deleted successfully", parent=self.root)
                self.data_fetch()
                conn.close()
            except Exception as e:
                messagebox.showerror("Error", f"Something went wrong: {e}", parent=self.root)
        else:
            return
    def update(self):
        if self.custNameVar.get()=="" or self.custFNameVar.get()=="" or self.custMNameVar.get()=="" or self.postCodeVar.get()=="" or self.mobileVar.get()=="" or self.emailVar.get()=="" or self.idNumberVar.get()=="" or self.addressVar.get()=="":
            messagebox.showwarning("Warning","All fields are required",parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="", database="hotel")
            cursor = conn.cursor()
            cursor.execute("update htable set custName=%s,custFName=%s,custMName =%s,custGender=%s,postCode=%s,mobile=%s,email=%s,nationality=%s,idProof=%s,idNumber=%s,address=%s where custRef = %s",

                           (self.custNameVar.get(),
                            self.custFNameVar.get(),
                            self.custMNameVar.get(),
                            self.custGenderVar.get(),
                            self.postCodeVar.get(),
                            self.mobileVar.get(),
                            self.emailVar.get(),
                            self.nationalityVar.get(),
                            self.idProofVar.get(),
                            self.idNumberVar.get(),
                            self.addressVar.get(),
                            self.custRefVar.get(),
                            ))
            conn.commit()
            self.data_fetch()
            conn.close()
            messagebox.showinfo("Success","Information updated successfully",parent=self.root)

    def search(self):
        try:
            conn = mysql.connector.connect(host="localhost", username="root", password="", database="hotel")
            cursor = conn.cursor()
            query = "SELECT * FROM htable WHERE " + str(self.combo_searchVar.get()) + " LIKE %s"
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


