from tkinter import *
from tkinter import messagebox
import mysql.connector
from PIL import Image, ImageTk

class ForgotPassword:
    def __init__(self, root):
        self.root = root
        self.root.title("Forgot Password")
        self.root.geometry("1366x768+-10+0")
        self.root.resizable(False, False)  # Disable window resizing

        #======= variable +==============
        self.phoneNumberVar = StringVar()
        self.ageVar = StringVar()
        self.colorVar = StringVar()
        self.flowerVar = StringVar()
        self.newPassVar = StringVar()

        # Background Image
        img2 = Image.open(r"Image\register.jpg")
        img2 = img2.resize((1366, 768))
        self.sideView = ImageTk.PhotoImage(img2)  # Keep a reference to the image

        self.sideImageL = Label(root, image=self.sideView, bd=4, relief=RIDGE)
        self.sideImageL.place(x=0, y=0)

        # Forgot Password Frame
        Frame_forgot = Frame(self.root, bg="white")
        Frame_forgot.place(x=480, y=100, height=540, width=400)

        title = Label(Frame_forgot, text="Forgot Password", font=("Impact", 35, "bold"), fg="#d77337", bg="white")
        title.place(x=50, y=30)

        # Phone Number
        lbl_phone = Label(Frame_forgot, text="Phone Number", font=("Goudy old style", 15, "bold"), fg="gray", bg="white")
        lbl_phone.place(x=50, y=100)
        self.txt_phone = Entry(Frame_forgot, textvariable=self.phoneNumberVar, font=("times new roman", 15), bg="lightgray")
        self.txt_phone.place(x=50, y=130, width=250, height=35)

        # Age
        lbl_age = Label(Frame_forgot, text="Age", font=("Goudy old style", 15, "bold"), fg="gray", bg="white")
        lbl_age.place(x=50, y=170)
        self.txt_age = Entry(Frame_forgot, textvariable=self.ageVar, font=("times new roman", 15), bg="lightgray")
        self.txt_age.place(x=50, y=200, width=250, height=35)

        # Favorite Color
        lbl_color = Label(Frame_forgot, text="Favorite Color", font=("Goudy old style", 15, "bold"), fg="gray", bg="white")
        lbl_color.place(x=50, y=240)
        self.txt_color = Entry(Frame_forgot, textvariable=self.colorVar, font=("times new roman", 15), bg="lightgray")
        self.txt_color.place(x=50, y=270, width=250, height=35)

        # Favorite Flower
        lbl_flower = Label(Frame_forgot, text="Favorite Flower", font=("Goudy old style", 15, "bold"), fg="gray", bg="white")
        lbl_flower.place(x=50, y=310)
        self.txt_flower = Entry(Frame_forgot, textvariable=self.flowerVar, font=("times new roman", 15), bg="lightgray")
        self.txt_flower.place(x=50, y=340, width=250, height=35)

        # New password
        lbl_newPass = Label(Frame_forgot, text="New Password", font=("Goudy old style", 15, "bold"), fg="gray", bg="white")
        lbl_newPass.place(x=50, y=380)
        self.txt_newPass = Entry(Frame_forgot, textvariable=self.newPassVar, font=("times new roman", 15), bg="lightgray")
        self.txt_newPass.place(x=50, y=410, width=250, height=35)

        # Submit Button
        submit_btn = Button(self.root, text="Submit", command=self.update, cursor="hand2", fg="white", bg="#d77337", font=("times new roman", 20))
        submit_btn.place(x=570, y=580, width=180, height=40)

    def update(self):
        if (self.phoneNumberVar.get() == "" or self.ageVar.get() == "" or
            self.colorVar.get() == "" or self.flowerVar.get() == "" or
            self.newPassVar.get() == ""):
            messagebox.showwarning("Warning", "All fields are required", parent=self.root)
        else:
            try:
                # Connect to MySQL database
                conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="",  # Replace with your MySQL password
                    database="hotel"
                )

                cursor = conn.cursor()

                # Fetch user details based on provided phone number and age
                query = "SELECT userName FROM users WHERE phoneNumber = %s AND age = %s AND favoriteColor = %s AND favoriteFlower = %s"
                cursor.execute(query, (self.phoneNumberVar.get(), self.ageVar.get(), self.colorVar.get(), self.flowerVar.get()))
                row = cursor.fetchone()

                if row:
                    username = row[0]
                    # Update password for the found username
                    update_query = "UPDATE users SET password = %s WHERE userName = %s"
                    cursor.execute(update_query, (self.newPassVar.get(), username))
                    conn.commit()

                    messagebox.showinfo("Success", "Password updated successfully!", parent=self.root)
                    self.root.destroy()
                else:
                    messagebox.showerror("Error", "User not found with provided details", parent=self.root)


            except mysql.connector.Error as e:
                messagebox.showerror("Error", f"Error connecting to MySQL: {e}", parent=self.root)

            finally:
                # Close cursor and connection
                if cursor:
                    cursor.close()
                if conn:
                    conn.close()


