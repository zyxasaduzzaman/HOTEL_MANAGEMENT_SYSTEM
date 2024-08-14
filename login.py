from tkinter import *
from tkinter import messagebox
import mysql.connector
from PIL import Image, ImageTk
from forgot import ForgotPassword
from register import Register
from hotel import HotelManagementSystem

class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Login System")
        self.root.geometry("1366x768+-10+0")
        self.root.resizable(False, False)  # Disable window resizing

        # Load and resize background image
        img2 = Image.open(r"Image\login.jpg")
        img2 = img2.resize((1366, 768))
        self.sideView = ImageTk.PhotoImage(img2)  # Keep a reference to the image

        # Display background image
        self.sideImageL = Label(root, image=self.sideView, bd=4, relief=RIDGE)
        self.sideImageL.place(x=0, y=0)

        # Login Frame
        Frame_login = Frame(self.root, bg="white")
        Frame_login.place(x=480, y=100, height=500, width=400)

        # Title of the login frame
        title = Label(Frame_login, text="Login Here", font=("Impact", 35, "bold"), fg="#d77337", bg="white")
        title.place(x=70, y=30)

        # Description label
        desc = Label(Frame_login, text="Admin Login Only", font=("Goudy old style", 15, "bold"), fg="#d25d17", bg="white")
        desc.place(x=70, y=100)

        # Username label and entry field
        lbl_user = Label(Frame_login, text="Username", font=("Goudy old style", 15, "bold"), fg="gray", bg="white")
        lbl_user.place(x=70, y=140)

        self.txt_user = Entry(Frame_login, font=("times new roman", 15), bg="lightgray")
        self.txt_user.place(x=70, y=170, width=250, height=35)

        # Password label and entry field
        lbl_pass = Label(Frame_login, text="Password", font=("Goudy old style", 15, "bold"), fg="gray", bg="white")
        lbl_pass.place(x=70, y=210)

        self.txt_pass = Entry(Frame_login, font=("times new roman", 15), bg="lightgray", show="*")
        self.txt_pass.place(x=70, y=240, width=250, height=35)

        # Forgot password button
        forget_btn = Button(Frame_login, command=self.forgot, text="Forgot Password", cursor="hand2", bg="white", bd=0, activebackground="white", fg="#d77337", font=("times new roman", 12))
        forget_btn.place(x=70, y=280)

        # Register button
        register_btn = Button(Frame_login, command=self.register, text="Register now", cursor="hand2", bg="white", activebackground="white", bd=0, fg="#d77337", font=("times new roman", 12))
        register_btn.place(x=70, y=310)

        # Login button
        login_btn = Button(self.root, command=self.login_function, text="Login", cursor="hand2", fg="white", bg="#d77337", font=("times new roman", 20))
        login_btn.place(x=570, y=500, width=180, height=40)

    def login_function(self):
        username = self.txt_user.get()
        password = self.txt_pass.get()

        try:
            # Connect to MySQL database
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",  # Replace with your MySQL password
                database="hotel"
            )

            cursor = conn.cursor()

            # Execute query to fetch password for the given username
            cursor.execute("SELECT password FROM users WHERE userName = %s", (username,))
            row = cursor.fetchone()

            if row:
                stored_password = row[0]
                if password == stored_password:
                    messagebox.showinfo("Success", f"Welcome, {username}!")
                    self.root.destroy()
                    # Open Hotel Management System within the same root window
                    root=Tk() # Hide login window
                    hotel = HotelManagementSystem(root)  # Initialize Hotel Management System

                else:
                    messagebox.showerror("Error", "Invalid password")
            else:
                messagebox.showerror("Error", "Invalid username")

        except mysql.connector.Error as e:
            messagebox.showerror("Error", f"Error connecting to MySQL: {e}")

        finally:
            # Close cursor and connection
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    def forgot(self):
        self.root.withdraw()  # Hide login window
        forgot_window = Toplevel(self.root)
        forgot = ForgotPassword(forgot_window)

    def register(self):
        self.root.withdraw()  # Hide login window
        register_window = Toplevel(self.root)
        register = Register(register_window)

root = Tk()
login = Login(root)
root.mainloop()
