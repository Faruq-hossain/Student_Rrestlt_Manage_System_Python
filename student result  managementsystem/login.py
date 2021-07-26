from tkinter import*
from PIL import Image, ImageTk, ImageDraw
from datetime import*
import time
from math import*  # atar help e line rotate korboo ghori er
# import pymysql
import sqlite3
import os
from tkinter import messagebox, ttk


class Login_window:
    def __init__(self, root):
        self.root = root
        self.root.title("Login System")
        self.root.geometry("1300x700+0+0")
        self.root.config(bg='#021e2f')
# ============background color==========

        # login er jonno
        left_lbl = Label(self.root, bg="#F5B7B1", bd=0)
        left_lbl.place(x=0, y=0, relheight=1, width=600)

        right_lbl = Label(self.root, bg="#3B3004", bd=0)
        right_lbl.place(x=600, y=0, relheight=1, relwidth=1)

        # title = Label(self.root, text="Welcome Analoge Clock", font=(
        # "times new roman", 50, "bold"), bg="#04444a", fg="white").place(x=0, y=50, relwidth=1)
    # ============Frames==========

        login_frame = Frame(self.root, bg="white")
        login_frame.place(x=250, y=100, width=800, height=500)

        title = Label(login_frame, text='LOGIN HERE', font=(
            "times new roman", 30, "bold"), bg="white", fg="#08A3D2").place(x=250, y=50)

        email = Label(login_frame, text='EMAIL ADDRESS', font=(
            "times new roman", 18, "bold"), bg="white", fg="gray").place(x=250, y=150)
        self.txt_email = Entry(login_frame, font=(
            "times new roman", 15, "bold"), bg="lightgray")
        self.txt_email.place(x=250, y=180, width=350, height=35)

        pass_ = Label(login_frame, text='PASSWORD', font=(
            "times new roman", 18, "bold"), bg="white", fg="gray").place(x=250, y=250)
        self.txt_pass = Entry(login_frame, font=(
            "times new roman", 15, "bold"), bg="lightgray")
        self.txt_pass.place(x=250, y=280, width=350, height=35)

        btn_reg = Button(
            login_frame, cursor="hand2", command=self.register_window, text="Registrer new Account?", font=("times new roman", 14), bg="white", bd=0, fg="#B00857").place(x=250, y=330)

        btn_forget = Button(
            login_frame, cursor="hand2", command=self.forget_password_window, text="Forget Password?", font=("times new roman", 14), bg="white", bd=0, fg="red").place(x=450, y=330)

        btn_login = Button(
            login_frame, text="Login", command=self.login, font=("times new roman", 20, "bold"), fg="white", bg="#B00857", cursor="hand2").place(x=250, y=375, width=180, height=40)


# ============clock==========
        # relief=RAISED
        self.lbl = Label(self.root, text="\nWebCode Clock", font=(
            "Book Antiqua", 25, "bold"), fg="white", compound=BOTTOM, bg="#000000", bd=0)
        self.lbl.place(x=90, y=120, height=450, width=350)
    # self.clock_image()
        self.working()

    # page reset er jonno

    def reset(self):
        self.cmb_quest.current(0)
        self.txt_new_pass.delete(0, END)
        self.txt_answer.delete(0, END)
        self.txt_pass.delete(0, END)
        self.txt_email.delete(0, END)

    def forget_password(self):
        if self.txt_email.get() == "Select" or self.cmb_quest.get() == "" or self.txt_answer.get() == "" or self.txt_new_pass.get() == "":
            messagebox.showerror(
                "Error", "All fields are required", parent=self.root2)
        else:

            try:
                con = sqlite3.connect(database="rms.db")
                cur = con.cursor()
                cur.execute("select * from employee where email=? and question=? and answer=? ",
                            (self.txt_email.get(), self.cmb_quest.get(), self.txt_answer.get()))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror(
                        "Error", "Please Select the Correct Security Question / Enter Answer", parent=self.root)
                else:
                    cur.execute("Update employee set password=? where email=? ",
                                (self.txt_new_pass.get(), self.txt_email.get()))
                    con.commit()
                    con.close()
                    messagebox.showinfo(
                        "Success", "Your Password has been reset, Please login with new password", parent=self.root2)

                    self.reset()
                    self.root2.destroy()

            except Exception as es:

                messagebox.showerror(
                    "Error", f"Error Due to : {str(es)}", parent=self.root)

        # ====forget password er jonno========
    def forget_password_window(self):
        if self.txt_email.get() == "":
            messagebox.showerror(
                "Error", "Please enter the  email address to reset your password", parent=self.root)
        else:
            try:
                con = sqlite3.connect(database="rms.db")
                cur = con.cursor()
                cur.execute("select * from employee where email=?",
                            (self.txt_email.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror(
                        "Error", "Please enter the valid email address to reset your password", parent=self.root)

                else:

                    con.close()
                    self.root2 = Toplevel()
                    self.root2.title("Forget Password")
                    self.root2.geometry("350x400+495+150")

                    self.root2.config(bg="white")

                    self.root2.focus_force()
                    self.root2.grab_set()

                    t = Label(self.root2, text="Forget Password", font=(
                        "times new roman", 20, "bold"), bg="white", fg="red").place(x=0, y=10, relwidth=1)

                    # ================Forget Password============
                    question = Label(self.root2, text="Security question", font=(
                        "times new roman", 15, "bold"), bg="white", fg="gray").place(x=50, y=100)
                    # entry field
                    self.cmb_quest = ttk.Combobox(self.root2, font=(
                        "times new roman", 13), state='readonly', justify=CENTER)
                    self.cmb_quest['values'] = (
                        "Select", "Your First Pet Name", "Your Birth Place", "Your Best Friend Name")
                    # opor theke place nice nia asci na hole error asbe
                    self.cmb_quest.place(x=50, y=130, width=250)
                    self.cmb_quest.current(0)  # bydefault select anar jonno

                    answer = Label(self.root2, text="Answer", font=(
                        "times new roman", 15, "bold"), bg="white", fg="gray").place(x=50, y=180)
                    # entry field
                    self.txt_answer = Entry(self.root2, font=(
                        "times new roman", 15), bg="lightgray")
                    self.txt_answer.place(x=50, y=210, width=250)

                    new_password = Label(self.root2, text="New Password", font=(
                        "times new roman", 15, "bold"), bg="white", fg="gray").place(x=50, y=260)
                    # entry field
                    self.txt_new_pass = Entry(self.root2, font=(
                        "times new roman", 15), bg="lightgray")
                    self.txt_new_pass.place(x=50, y=290, width=250)

                    btn_change_password = Button(self.root2, text="Reset Password", command=self.forget_password, bg="green", fg="white", font=(
                        "times new roman", 15, "bold")).place(x=90, y=340)

                    # messagebox.showinfo("Success", "Welcome", parent=self.root)
                    # self.root.destroy()
                    # import student

            except Exception as es:

                messagebox.showerror(
                    "Error", f"Error Due to : {str(es)}", parent=self.root)


# =====data connect korar jonno=======


    def register_window(self):
       # reride korbo akhan theke register from e jabe
        self.root.destroy()
        import register

    def login(self):
        if self.txt_email.get() == "" or self.txt_pass.get() == "":
            messagebox.showerror(
                "Error", "All fields are required", parent=self.root)
        else:
            try:
                con = sqlite3.connect(database="rms.db")
                cur = con.cursor()
                cur.execute("select * from employee where email=? and password=? ",
                            (self.txt_email.get(), self.txt_pass.get()))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror(
                        "Error", "INVALID USERNAME & PASSWORD", parent=self.root)

                else:
                    messagebox.showinfo(
                        "Success", f"Welcome: {self.txt_email.get()}", parent=self.root)
                    self.root.destroy()
                    os.system("python dashboard.py")
                con.close()

            except Exception as es:

                messagebox.showerror(
                    "Error", f"Error Due to : {str(es)}", parent=self.root)

    def clock_image(self, hr, min_, sec_):
        clock = Image.new("RGB", (400, 400), (0, 0, 0))
        draw = ImageDraw.Draw(clock)
# =============for clock image====================
        bg = Image.open("images/watch4.png")
        bg = bg.resize((300, 300), Image.ANTIALIAS)
        clock.paste(bg, (50, 50))
        # Formola To Rotate the Anticlock

        # angel_in _radians = angel_in_degrees * math.pi/180
        # line_length = 100
        # center_x = 250
        # center_y = 250
        # end_x = center_x - line_length * math.cos(angle_in_radians)
        # end_y = center_y - line_length * math.sin(angl e_in_radians)

        clock.save("clock_new.png")
# =============hours line image====================
#                  x1,  y1    x2   y2
        origin = 200, 200
        draw.line((origin, 200+50*sin(radians(hr)), 200-50 *
                   cos(radians(hr))), fill="black", width=3)
# =============min line image====================
        draw.line((origin, 200+80*sin(radians(min_)), 200 -
                   80*cos(radians(min_))), fill="blue", width=3)
# =============sec line image====================
        draw.line((origin, 200+100*sin(radians(sec_)), 200 -
                   100*cos(radians(sec_))), fill="green", width=3)
        draw.ellipse((195, 195, 210, 210), fill="black")
        clock.save("clock_new.png")

# ======ghori kaj korar jonno time onujaiye-========
    def working(self):
        h = datetime.now().time().hour
        m = datetime.now().time().minute
        s = datetime.now().time().second

        # =====time k angel e define korbo-====
        hr = (h/12)*360
        min_ = (m/60)*360
        sec_ = (s/60)*360
        # print(h, m, s)
        # print(hr, min_, sec_)
        self.clock_image(hr, min_, sec_)
        # ======image run er ppor dekhar jonno==
        self.img = ImageTk.PhotoImage(file="clock_new.png")
        self.lbl.config(image=self.img)
        self.lbl.after(200, self.working)


root = Tk()
obj = Login_window(root)
root.mainloop()
