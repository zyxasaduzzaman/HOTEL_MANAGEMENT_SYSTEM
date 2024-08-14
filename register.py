from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector

class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Registration System")
        self.root.geometry("1366x768+-10+0")
        self.root.resizable(False, False)  # Disable window resizing

        # Background Image
        img2 = Image.open(r"Image\register.jpg")
        img2 = img2.resize((1360, 750))
        self.sideView = ImageTk.PhotoImage(img2)  # Keep a reference to the image

        self.sideImageL = Label(root, image=self.sideView, bd=4, relief=RIDGE)
        self.sideImageL.place(x=0, y=0)

        # Registration Frame
        Frame_register = Frame(self.root, bg="white")
        Frame_register.place(x=480, y=50, height=650, width=360)

        title = Label(Frame_register, text="Register Here", font=("Impact", 35, "bold"), fg="#d77337", bg="white")
        title.place(x=50, y=30)

        # Fullname
        lbl_fullname = Label(Frame_register, text="Fullname", font=("Goudy old style", 15, "bold"), fg="gray", bg="white")
        lbl_fullname.place(x=50, y=100)
        self.txt_fullname = Entry(Frame_register, font=("times new roman", 15), bg="lightgray")
        self.txt_fullname.place(x=50, y=130, width=250, height=35)

        # Username
        lbl_user = Label(Frame_register, text="Username", font=("Goudy old style", 15, "bold"), fg="gray", bg="white")
        lbl_user.place(x=50, y=170)
        self.txt_user = Entry(Frame_register, font=("times new roman", 15), bg="lightgray")
        self.txt_user.place(x=50, y=200, width=250, height=35)

        # Phone Number
        lbl_phone = Label(Frame_register, text="Phone Number", font=("Goudy old style", 15, "bold"), fg="gray", bg="white")
        lbl_phone.place(x=50, y=240)
        self.txt_phone = Entry(Frame_register, font=("times new roman", 15), bg="lightgray")
        self.txt_phone.place(x=50, y=270, width=250, height=35)

        # Password
        lbl_pass = Label(Frame_register, text="Password", font=("Goudy old style", 15, "bold"), fg="gray", bg="white")
        lbl_pass.place(x=50, y=310)
        self.txt_pass = Entry(Frame_register, font=("times new roman", 15), bg="lightgray", show="*")
        self.txt_pass.place(x=50, y=340, width=250, height=35)

        # Age
        lbl_age = Label(Frame_register, text="Age", font=("Goudy old style", 15, "bold"), fg="gray", bg="white")
        lbl_age.place(x=50, y=380)
        self.txt_age = Entry(Frame_register, font=("times new roman", 15), bg="lightgray")
        self.txt_age.place(x=50, y=410, width=250, height=35)

        # Favorite Color
        lbl_color = Label(Frame_register, text="Favorite Color", font=("Goudy old style", 15, "bold"), fg="gray", bg="white")
        lbl_color.place(x=50, y=450)
        self.txt_color = Entry(Frame_register, font=("times new roman", 15), bg="lightgray")
        self.txt_color.place(x=50, y=480, width=250, height=35)

        # Favorite Flower
        lbl_flower = Label(Frame_register, text="Favorite Flower", font=("Goudy old style", 15, "bold"), fg="gray", bg="white")
        lbl_flower.place(x=50, y=520)
        self.txt_flower = Entry(Frame_register, font=("times new roman", 15), bg="lightgray")
        self.txt_flower.place(x=50, y=550, width=250, height=35)

        # Register Button
        register_btn = Button(self.root, command=self.register_function, text="Register", cursor="hand2", fg="white", bg="#d77337", font=("times new roman", 20))
        register_btn.place(x=570, y=648, width=180, height=40)

    def register_function(self):
        fullname = self.txt_fullname.get()
        username = self.txt_user.get()
        phone = self.txt_phone.get()
        password = self.txt_pass.get()
        age = self.txt_age.get()
        favorite_color = self.txt_color.get()
        favorite_flower = self.txt_flower.get()

        if fullname == "" or username == "" or phone == "" or password == "" or age == "" or favorite_color == "" or favorite_flower == "":
            messagebox.showerror("Error", "All fields are required")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="", database="hotel")
                cursor = conn.cursor()
                cursor.execute("INSERT INTO users (fullName, userName, phoneNumber, password, age, favoriteColor, favoriteFlower) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                               (fullname, username, phone, password, age, favorite_color, favorite_flower))
                conn.commit()
                conn.close()
                messagebox.showinfo("Success", "Registration Successful")
                self.root.destroy()
            except Exception as e:
                messagebox.showerror("Error", f"Something went wrong: {e}")

