from tkinter import*
from PIL import Image, ImageTk  # pip install pillow
from course import CourseClass
from student import StudentClass
from result import ResultClass
from report import ReportClass
from tkinter import messagebox
import os
from PIL import Image, ImageTk, ImageDraw
from datetime import*
import time
from math import*  # atar help e line rotate korboo ghori er
# import pymysql
import sqlite3
import os
from tkinter import messagebox, ttk


class RMS:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Result Management System")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")

        # =======icons========
        # self.logo_dash = ImageTk.PhotoImage(file="images/logo.png.png")padx=10, compound=LEFT, image=self.logo_dash,
        # =======title========
        title = Label(self.root, text="Student Result Management System",  font=(
            "goudy old style", 20, "bold"), bg="#033054", fg="white").place(x=0, y=0, relwidth=1)

        # ========Menu=========
        M_Frame = LabelFrame(self.root, text="Menu", font=(
            "times new roman", 15), bg="white")
        M_Frame.place(x=10, y=60, width=1523, height=80)

        btn_course = Button(M_Frame, text="Course", font=(
            "goudy old style", 15, "bold"), bg="#0b5377", fg="white", cursor="hand2", command=self.add_course).place(x=20, y=5, width=200, height=40)
        btn_student = Button(M_Frame, text="Student", font=(
            "goudy old style", 15, "bold"), bg="#0b5377", fg="white", cursor="hand2", command=self.add_student).place(x=240, y=5, width=200, height=40)
        btn_result = Button(M_Frame, text="Result", font=(
            "goudy old style", 15, "bold"), bg="#0b5377", fg="white", cursor="hand2", command=self.add_result).place(x=460, y=5, width=200, height=40)
        btn_view = Button(M_Frame, text="View", font=(
            "goudy old style", 15, "bold"), bg="#0b5377", fg="white", cursor="hand2", command=self.add_report).place(x=680, y=5, width=200, height=40)
        btn_logout = Button(M_Frame, text="Logout", font=(
            "goudy old style", 15, "bold"), bg="#0b5377", fg="white", cursor="hand2", command=self.logout).place(x=900, y=5, width=200, height=40)
        btn_exit = Button(M_Frame, text="Exit", font=(
            "goudy old style", 15, "bold"), bg="#0b5377", fg="white", cursor="hand2", command=self.exit_).place(x=1120, y=5, width=200, height=40)

        # =======content_windoe====
        self.bg_img = Image.open("images/11.jpg")
        self.bg_img = self.bg_img.resize((920, 350), Image.ANTIALIAS)
        self.bg_img = ImageTk.PhotoImage(self.bg_img)

        self.lbl_bg = Label(self.root, image=self.bg_img).place(
            x=550, y=180, width=920, height=350)

        # =====update_detail=========
        self.lbl_course = Label(self.root, text="Total Course\n[ 0 ]", font=(
            "goudy old style", 20), bd=10, relief=RIDGE, bg="#e43b06", fg="white")
        self.lbl_course.place(x=550, y=530, width=300, height=100)

        self.lbl_student = Label(self.root, text="Total Student\n[ 0 ]", font=(
            "goudy old style", 20), bd=10, relief=RIDGE, bg="#0676ad", fg="white")
        self.lbl_student.place(x=860, y=530, width=300, height=100)

        self.lbl_result = Label(self.root, text="Total Result\n[ 0 ]", font=(
            "goudy old style", 20), bd=10, relief=RIDGE, bg="#038074", fg="white")
        self.lbl_result.place(x=1170, y=530, width=300, height=100)

        # ============clock==========
        # relief=RAISED
        self.lbl = Label(self.root, text="\nWebCode Clock", font=(
            "Book Antiqua", 25, "bold"), fg="white", compound=BOTTOM, bg="#000000", bd=0)
        self.lbl.place(x=30, y=180, height=450, width=350)
    # self.clock_image()
        self.working()

        # =======footer========
        footer = Label(self.root, text="SRMS-Student Management System\nContact Us for any Technical Issue: 017xxx1421",  font=(
            "goudy old style", 12), bg="#262626", fg="white").pack(side=BOTTOM, fill=X)
        self.update_details()
# =========================================
# course student result er kaj

    def update_details(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:

            cur.execute(
                "select * from course ")
            cr = cur.fetchall()
            self.lbl_course.config(text=f"Total Course\n[{str(len(cr))}]")

            cur.execute(
                "select * from student ")
            cr = cur.fetchall()
            self.lbl_student.config(text=f"Total Students\n[{str(len(cr))}]")

            cur.execute(
                "select * from result ")
            cr = cur.fetchall()
            self.lbl_result.config(text=f"Total Result\n[{str(len(cr))}]")

            self.lbl_course.after(200, self.update_details)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

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

    # courseka call korar jonno

    def add_course(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = CourseClass(self.new_win)

    def add_student(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = StudentClass(self.new_win)

    def add_result(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = ResultClass(self.new_win)

    def add_report(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = ReportClass(self.new_win)

    def logout(self):
        op = messagebox.askyesno(
            "Confirm", "Do you really want to logout?", parent=self.root)
        if op == True:
            self.root.destroy()
            os.system("python login.py")

    def exit_(self):
        op = messagebox.askyesno(
            "Confirm", "Do you really want to Exit?", parent=self.root)
        if op == True:
            self.root.destroy()


if __name__ == "__main__":  # multiple time use er jonno
    root = Tk()
    obj = RMS(root)
    root.mainloop()
