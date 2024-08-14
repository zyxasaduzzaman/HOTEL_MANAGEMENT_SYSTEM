from tkinter import *
from PIL import Image, ImageTk
from customer import Customer
from room import Room
from details import AddRoom



class HotelManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1366x768+-10+0")

        # ==================hotel side view========================
        img2 = Image.open(r"Image\hotelside.jpg")
        img2 = img2.resize((1360, 130))
        self.sideView = ImageTk.PhotoImage(img2)  # Keep a reference to the image

        self.sideImageL = Label(root, image=self.sideView, bd=4, relief=RIDGE)
        self.sideImageL.place(x=0, y=0)

        # ====================logo===================
        img1 = Image.open(r"Image\logo.jpg")
        img1 = img1.resize((180, 130))
        self.logo_image = ImageTk.PhotoImage(img1)  # Keep a reference to the image

        self.logo_label = Label(root, image=self.logo_image, bd=4, relief=RIDGE)
        self.logo_label.place(x=0, y=0)

        # =======================title======================
        self.titleLabel = Label(root, text="HOTEL MANAGEMENT SYSTEM", font=("times new roman", 40, "bold"), fg="gold",bg="black", bd=4, relief=RIDGE)
        self.titleLabel.place(x=0, y=130, width=1366, height=60)


        #===============main frame ====================
        self.mainFrame = Frame(self.root,bd=8,relief=RIDGE)
        self.mainFrame.place(x=-1,y=190,width= 1366,height=515)

        #================ menu lable ========================
        self.menuLable = Label(self.mainFrame,text="MENU",font=("times new roman",20,"bold"),bd=2,relief=RIDGE,bg="black",fg="gold")
        self.menuLable.place(x=3,y=3,width=200)


        #===================== button frame ==============================

        self.buttonFrame = Frame(self.mainFrame, bd=5, relief=RIDGE)
        self.buttonFrame.place(x=0, y=40, width=200,height=220)

        self.custButton = Button(self.buttonFrame,cursor="hand2",command=self.Customer_details,width=15,text="CUSTOMER",font=("times new roman",16,"bold"),activebackground="green",activeforeground="gold",bg="black",fg="gold")
        self.custButton.grid(row=0,column=0)

        self.roomButton = Button(self.buttonFrame, cursor="hand2",command=self.Room_details,width=15, text="ROOM", font=("times new roman", 16, "bold"),
                                 bg="black", fg="gold",activebackground="green",activeforeground="gold")
        self.roomButton.grid(row=1, column=0)

        self.detailsButton = Button(self.buttonFrame, width=15,cursor="hand2", command=self.AddRoom,text="DETAILS", activeforeground="gold",font=("times new roman", 16, "bold"),
                                 bg="black", activebackground="green",fg="gold")
        self.detailsButton.grid(row=2, column=0)


        self.logoutButton = Button(self.buttonFrame,command=self.logOut,cursor="hand2", width=15, text="LOG OUT",activeforeground="gold", font=("times new roman", 16, "bold"),
                                 bg="black",activebackground="green", fg="gold")
        self.logoutButton.grid(row=3, column=0)


        #======================== big pic =======================
        img3 = Image.open(r"Image\big.jpg")
        img3 = img3.resize((1145,495))
        self.bigPhoto = ImageTk.PhotoImage(img3)
        self.bigPhotoL = Label(self.mainFrame,image=self.bigPhoto,bd=4,relief=RIDGE)
        self.bigPhotoL.place(x=200,y=0)


        #===================side image ======================
        img4 = Image.open(r"Image\sideup.jpg")
        img4 = img4.resize((190, 140))
        self.sduPhoto = ImageTk.PhotoImage(img4)
        self.sduPhotoL = Label(self.mainFrame, image=self.sduPhoto, bd=4, relief=RIDGE)
        self.sduPhotoL.place(x=1, y=210)

        img5 = Image.open(r"Image\sidedown.jpg")
        img5 = img5.resize((190, 140))
        self.sddPhoto = ImageTk.PhotoImage(img5)
        self.sddPhotoL = Label(self.mainFrame, image=self.sddPhoto, bd=4, relief=RIDGE)
        self.sddPhotoL.place(x=1, y=355)

    def Customer_details(self):
        self.newWindow = Toplevel(self.root)
        self.app = Customer(self.newWindow)

    def Room_details(self):
        self.newWindow = Toplevel(self.root)
        self.app = Room(self.newWindow)

    def AddRoom(self):
        self.newWindow = Toplevel(self.root)
        self.app = AddRoom(self.newWindow)

    def logOut(self):
        self.root.destroy()

