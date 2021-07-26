from tkinter import*
from typing import Counter
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
#import pymysql
import sqlite3
import os


class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Registration Window")
        self.root.geometry("1600x830+0+0")
        self.root.config(bg="white")
        # =======Bg Image======

        self.bg = ImageTk.PhotoImage(file="images/regi1.png")
        bg = Label(self.root, image=self.bg).place(
            x=250, y=0, relwidth=1, relheight=1)
        self.up = ImageTk.PhotoImage(file="images/regi1.png")
        # up = Label(self.root, image=self.up).place(
        # x=100, y=470, width=700, height=700)

        # =======Left Image======

        self.left = ImageTk.PhotoImage(file="images/regi2.png")
        left = Label(self.root, image=self.left).place(
            x=80, y=160, width=400, height=500)

        # -=======Register Frame=====
        frame1 = Frame(self.root, bg="white")
        frame1.place(x=480, y=160, width=900, height=500)

        title = Label(frame1, text="REGITER HERE", font=(
            "times new roman", 20, "bold"), bg="white", fg="green").place(x=100, y=30)

        # ------------------row 1--------------------------------------------
        # ata fatch korar 1st upai self.var_fname = StringVar() .......textvariable=self.var_fname ata text e bosbe light er pore
        f_name = Label(frame1, text="First Name", font=(
            "times new roman", 15, "bold"), bg="white", fg="gray").place(x=100, y=100)
        # entry field
        self.txt_fname = Entry(frame1, font=(
            "times new roman", 15), bg="lightgray")
        self.txt_fname.place(x=100, y=130, width=250)

        l_name = Label(frame1, text="Last Name", font=(
            "times new roman", 15, "bold"), bg="white", fg="gray").place(x=480, y=100)
        # entry field
        self.txt_lname = Entry(frame1, font=(
            "times new roman", 15), bg="lightgray")
        # data fetch korar 2nd upai self dibo then
        self.txt_lname.place(x=480, y=130, width=250)

        # ------------------row 2--------------------------------------------
        contact = Label(frame1, text="Contat No.", font=(
            "times new roman", 15, "bold"), bg="white", fg="gray").place(x=100, y=170)
        # entry field
        self.txt_contact = Entry(frame1, font=(
            "times new roman", 15), bg="lightgray")
        self.txt_contact.place(x=100, y=200, width=250)

        email = Label(frame1, text="Email", font=(
            "times new roman", 15, "bold"), bg="white", fg="gray").place(x=480, y=170)
        # entry field
        self.txt_email = Entry(frame1, font=(
            "times new roman", 15), bg="lightgray")
        self.txt_email.place(x=480, y=200, width=250)
      # ================row 3============
        question = Label(frame1, text="Security question", font=(
            "times new roman", 15, "bold"), bg="white", fg="gray").place(x=100, y=240)
        # entry field
        self.cmb_quest = ttk.Combobox(frame1, font=(
            "times new roman", 13), state='readonly', justify=CENTER)
        self.cmb_quest['values'] = (
            "Select", "Your First Pet Name", "Your Birth Place", "Your Best Friend Name")
        # opor theke place nice nia asci na hole error asbe
        self.cmb_quest.place(x=100, y=270, width=250)
        self.cmb_quest.current(0)  # bydefault select anar jonno

        answer = Label(frame1, text="Answer", font=(
            "times new roman", 15, "bold"), bg="white", fg="gray").place(x=480, y=240)
        # entry field
        self.txt_answer = Entry(frame1, font=(
            "times new roman", 15), bg="lightgray")
        self.txt_answer.place(x=480, y=270, width=250)
        # ------------------row 4--------------------------------------------
        password = Label(frame1, text="Password", font=(
            "times new roman", 15, "bold"), bg="white", fg="gray").place(x=100, y=310)
        # entry field
        self.txt_password = Entry(frame1, font=(
            "times new roman", 15), bg="lightgray")
        self.txt_password.place(x=100, y=340, width=250)

        cpassword = Label(frame1, text="Confirom Password", font=(
            "times new roman", 15, "bold"), bg="white", fg="gray").place(x=480, y=310)
        # entry field
        self.txt_cpassword = Entry(frame1, font=(
            "times new roman", 15), bg="lightgray")
        self.txt_cpassword.place(x=480, y=340, width=250)

        # ==============terms========
        # run er por fatch kore chack bosx hoini setar jonno
        self.var_chk = IntVar()
        chk = Checkbutton(
            frame1, text="I Agree The Terms & Conditions", variable=self.var_chk, onvalue=1, offvalue=0, bg="white", font=("times new roman", 12)).place(x=100, y=380)
        # ========button====
        self.btn_img = ImageTk.PhotoImage(file="images/btn2.jpg")
        btn_register = Button(frame1, image=self.btn_img, bd=0,
                              cursor="hand2", command=self.register_data).place(x=100, y=420)

        # ========login====
        btn_login = Button(self.root, text="Sign In", command=self.login_window, font=("times new roman", 20), bg="red", bd=0,
                           cursor="hand2").place(x=200, y=580, width=180)
    # =====data connect korar jonno=======

    def login_window(self):
       # reride korbo akhan theke register from e jabe
        self.root.destroy()
        os.system("python login.py")

    def clear(self):
        self.txt_fname.delete(0, END)
        self.txt_lname.delete(0, END)
        self.txt_contact.delete(0, END)
        self.txt_email.delete(0, END)
        self.txt_answer.delete(0, END)
        self.txt_password.delete(0, END)
        self.txt_cpassword.delete(0, END)
        self.cmb_quest.current(0)

       # ============================================================================================================
        # data fatch korar jonno amader python e 2ta way ace
       # 1.....kicu variable baniye oi varible re entry te pass kore oi variable e data fatch kore
       # 2.....entry field er object banaici okhane data fatch kora
       # ====constract er sathe

    def register_data(self):
        # print(self.var_fname.get(), self.txt_lname.get())ata 2nd fatch er jonno
        if self.txt_fname.get() == "" or self.txt_contact.get() == "" or self.txt_email.get() == "" or self.cmb_quest.get() == "Select" or self.txt_answer.get() == "" or self.txt_password.get() == "" or self.txt_cpassword.get() == "":
            messagebox.showerror(
                "Error", "All Fields Are Requires", parent=self.root)
        # password match korar jonno
        elif self.txt_password.get() != self.txt_cpassword.get():
            messagebox.showerror(
                "Error", "Password & Confirm Password should be same", parent=self.root)
        # chackbox er jonno
        elif self.var_chk.get() == 0:
            messagebox.showerror(
                "Error", "Please Agree our terms and conditions", parent=self.root)
        else:
            try:
                con = sqlite3.connect(database="rms.db")
                # con = pymysql.connect(
                # host="localhost", user="root", password="", database="employee2")
                # akhane aki data 2 bar save hosse aki data 2 bar save na hobar jonno

                cur = con.cursor()
                cur.execute("Select * from employee where email=?",
                            (self.txt_email.get(),))
                row = cur.fetchone()
                # print(row)
                if row != None:
                    messagebox.showerror(
                        "Error", "User Already Exits, Please Try With Another Email", parent=self.root)
                else:
                    cur.execute("insert into employee (f_name,l_name,contact,email,question,answer,password) values(?,?,?,?,?,?,?)",
                                (self.txt_fname.get(),
                                    self.txt_lname.get(),
                                    self.txt_contact.get(),
                                    self.txt_email.get(),
                                    self.cmb_quest.get(),
                                    self.txt_answer.get(),
                                    self.txt_password.get()
                                 ))
                    # ata function er databaser change gula auto change hbe
                    con.commit()
                    con.close()
                    messagebox.showinfo(
                        "Success", "Register Successful", parent=self.root)
                    # clear er jonno
                    self.clear()
                    self.login_window()

            except Exception as es:
                messagebox.showerror(
                    "Error", f"Error due to: {str(es)}", parent=self.root)

            # self.txt_lname.get(),
            # self.txt_contact.get(),
            # self.txt_email.get(),
            # self.cmb_quest.get(),
            # self.txt_answer.get(),
            # self.txt_password.get(),
            # self.txt_cpassword.get())


root = Tk()
obj = Register(root)
root.mainloop()
