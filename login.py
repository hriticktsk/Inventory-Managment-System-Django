from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql


class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Login Employee Form")

        self.root.withdraw()
        x = (self.root.winfo_screenwidth() - self.root.winfo_reqwidth()) / 3
        y = (self.root.winfo_screenheight() -
             self.root.winfo_reqheight()) / 4.5
        self.root.geometry("560x400+%d+%d" % (x, y))

        self.root.resizable(False, False)

        # Frames
        self.title_frame = Frame(
            self.root, bd=4, relief=RIDGE, bg="navy")
        self.title_frame.place(x=0, y=0, width=560, height=326)

        # Title Head
        self.lbl_title = Label(
            self.title_frame, text="Login Form", bd=4, relief=RIDGE,  bg="navy", fg="#fc5c00", font=("roboto sans-serif", 23), pady=14)
        self.lbl_title.pack(side=TOP, fill=X)

        # Form Frame
        self.form_frame = Frame(
            self.root, bd=4, relief=RIDGE, bg="navy")
        self.form_frame.place(x=0, y=75, width=560, height=326)

        
        self.fname_label = Label(self.form_frame, text='',
                                 font=('bold', 24), bg="navy", fg="white", padx=20, pady=7).grid(row=2, column=2, sticky=W)
        # Username
        self.username_text = StringVar()
        self.username_label = Label(self.form_frame, text='Username :',
                                    font=("roboto sans-serif", 14), bg="navy", fg="white", padx=5, pady=10).grid(
            row=3, column=3, sticky=W)
        self.username_entry = Entry(
            self.form_frame, textvariable=self.username_text, width=30, bd=5, font=("roboto sans-serif", 14))
        self.username_entry.grid(row=3, column=4)

        # Password
        self.password_text = StringVar()
        self.password_label = Label(self.form_frame, text='Password :',
                                    font=("roboto sans-serif", 14), bg="navy", fg="white", padx=5, pady=14).grid(
            row=4, column=3, sticky=W)
        self.password_entry = Entry(
            self.form_frame, textvariable=self.password_text, width=30, bd=5, show="*", font=("roboto sans-serif", 14))
        self.password_entry.grid(row=4, column=4)

        # Buttons and Frame
        # Frame
        self.btn_frame = Frame(
            self.form_frame, bd=2, relief=RIDGE, bg="navy")
        self.btn_frame.place(x=87, y=199, width=382, height=90)

        
        self.space_lbl = Label(self.btn_frame, text='',
                               bg="navy", padx=12).grid(row=2, column=0)

        # Buttons
        self.register_btn = Button(self.btn_frame, text='Login Now', width=15, height=2,  bd=2,
                                   relief=FLAT, bg="#fc5c01", fg="white", command=self.fields, font=("roboto sans-serif", 10, "bold"))
        self.register_btn.grid(row=2, column=1, padx=19, pady=23)

        self.back_btn = Button(self.btn_frame, text='Register Now', width=15, height=2,
                               bg="#fc5c01", fg="white", bd=2, relief=FLAT, command=self.register, font=("roboto sans-serif", 10, "bold"))
        self.back_btn.grid(row=2, column=2)

    def clear(self):
        self.username_entry.delete(0, END)
        self.password_entry.delete(0, END)

    
    def fields(self):

        if self.username_entry.get() == '' or self.password_entry.get() == '':
            messagebox.showerror(
                'Required Fields', 'Please include all fields')
            self.clear()
        else:
            try:
                con = pymysql.connect(
                    host="localhost", user="root", password="root", database="proinv")
                cur = con.cursor()
                cur.execute("select * from user where username=%s and password=%s",
                            (self.username_text.get(), self.password_text.get()))
                row = cur.fetchone()

                if row == None:
                    messagebox.showerror(
                        'Error', 'Undefined Username and Password, Please Try Again Later')
                    self.clear()
                else:
                    messagebox.showinfo(
                        'Success', 'Welcome to Product Database')
                    self.clear()
                    self.root.destroy()
                    import dashboard
                con.close()
            except Exception as es:
                messagebox.showerror(
                    'Error', f'Error due to: {str(es)}')

    

    def register(self):
        
        top = Toplevel()
        top.title("Registration Form")
        x = (top.winfo_screenwidth() - top.winfo_reqwidth()) / 2.9
        y = (top.winfo_screenheight() -
             top.winfo_reqheight()) / 4.4
        top.geometry("530x470+%d+%d" % (x, y))
        top.resizable(False, False)

        def register_data():

            
            if fname_text.get() == '' or lname_text.get() == '' or username_text.get() == '' or email_text.get() == '' or password_text.get() == '' or cpassword_text.get() == '':
                messagebox.showerror(
                    'Required Fields', 'Please include all fields')
                clear()

            elif password_text.get() != cpassword_text.get():
                messagebox.showerror(
                    'Error', 'Password should be same of Confirm Password')
                clear()
            
            else:
                try:
                    con = pymysql.connect(
                        host="localhost", user="root", password="root", database="proinv")
                    cur = con.cursor()
                    cur.execute("select * from user where email=%s",
                                email_text.get())
                    row = cur.fetchone()

                    
                    if row != None:
                        messagebox.showerror(
                            'Error', 'Your Email is Already Exist ')

                    
                    else:
                        cur.execute(
                            "insert into user (fname,lname,username,email,password) values(%s,%s,%s,%s,%s)",
                            (fname_text.get(),
                            lname_text.get(),
                            username_text.get(),
                            email_text.get(),
                            password_text.get()
                            ))
                        con.commit()
                        con.close()
                        messagebox.showinfo("Success", "Register Successfully")

                except Exception as es:
                    messagebox.showerror(
                        'Error', f'Error due to: {str(es)}')

                # Clear
                clear()
        def clear():
            top.fname_entry.delete(0, END)
            top.lname_entry.delete(0, END)
            top.username_entry.delete(0, END)
            top.email_entry.delete(0, END)
            top.password_entry.delete(0, END)
            top.cpassword_entry.delete(0, END)

        def login_field():
            ext = messagebox.askyesno(
                'Database', 'Are you sure do want to back? ')

            if ext > 0:
                self.root.destroy()
                import login

        # Title Head
        top.lbl_title = Label(
            top, text="Registration Form", bd=4, fg="white", relief=RIDGE,  bg="#fc5c00", font=("roboto sans-serif", 23), pady=7)
        top.lbl_title.pack(side=TOP, fill=X)

        # Frames
        top.title_frame = Frame(
            top, bd=4, relief=RIDGE, bg="navy")
        top.title_frame.place(x=0, y=55, width=530, height=417)

        
        top.fname_label = Label(top.title_frame, text='',
                                 font=('bold', 14), bg="navy", fg="white", padx=12, pady=20).grid(
                                     row=2, column=2, sticky=W)

        # Firstname
        fname_text = StringVar()
        top.fname_label = Label(top.title_frame, text='First Name :',
                                 font=("roboto sans-serif", 14), bg="navy", fg="white", padx=10, pady=20).grid(
                                     row=2, column=3, sticky=W)

        top.fname_entry = Entry(
            top.title_frame, textvariable=fname_text, width=32, bd=3,
            font=("bold", 10))
        top.fname_entry.grid(row=2, column=4)

        # Last Name
        lname_text = StringVar()
        top.lname_label = Label(top.title_frame, text='Last Name :',
                                 font=("roboto sans-serif", 14), bg="navy", fg="white", padx=10).grid(
            row=3, column=3, sticky=W)
        top.lname_entry = Entry(
            top.title_frame, textvariable=lname_text, width=32, bd=3,
            font=("bold", 10))
        top.lname_entry.grid(row=3, column=4)

        # Username
        username_text = StringVar()
        top.username_label = Label(top.title_frame, text='Username :',
                                    font=("roboto sans-serif", 14), bg="navy", fg="white", padx=10, pady=20).grid(
            row=4, column=3, sticky=W)
        top.username_entry = Entry(
            top.title_frame, textvariable=username_text, width=32, bd=3,
            font=("bold", 10))
        top.username_entry.grid(row=4, column=4)

        # Email
        email_text = StringVar()
        top.email_label = Label(top.title_frame, text='Email :',
                                 font=("roboto sans-serif", 14), bg="navy", fg="white", padx=10).grid(
                                     row=5, column=3, sticky=W)
        top.email_entry = Entry(
            top.title_frame, textvariable=email_text, width=32, bd=3,
            font=("bold", 10))
        top.email_entry.grid(row=5, column=4)

        # Password
        password_text = StringVar()
        top.password_label = Label(top.title_frame, text='Create Password :',
                                    font=("roboto sans-serif", 14), bg="navy", fg="white", padx=10, pady=20).grid(
            row=6, column=3, sticky=W)
        top.password_entry = Entry(
            top.title_frame, textvariable=password_text, width=32, bd=3, show="*",
            font=("bold", 10))
        top.password_entry.grid(row=6, column=4)

        # Confirm Password
        cpassword_text = StringVar()
        top.cpassword_label = Label(top.title_frame, text='Confirm Password :',
                                     font=("roboto sans-serif", 14), bg="navy", fg="white", padx=10).grid(
            row=7, column=3, sticky=W)
        top.cpassword_entry = Entry(
            top.title_frame, textvariable=cpassword_text, width=32, bd=3, show="*",
            font=("bold", 10))
        top.cpassword_entry.grid(row=7, column=4)

        
        top.space_lbl = Label(top.title_frame, text='',
                               font=('bold', 14), bg="navy", fg="white", padx=20).grid(
            row=8, column=2, sticky=W)

        
        # Frames
        top.btn_frame = Frame(
            top.title_frame, bd=2, relief=RIDGE, bg="navy")
        top.btn_frame.place(x=0, y=300, width=523, height=110)

        
        top.space_lbl = Label(top.btn_frame, text='',
                               font=('bold', 14), bg="navy", fg="white", padx=32).grid(
            row=1, column=2, sticky=W)

        # Buttons
        top.register_btn = Button(top.btn_frame, text='Register Now', command=register_data, width=15, height=2,  bd=2,
                                   relief=FLAT, bg="#fc5c01", fg="white", font=("roboto sans-serif", 12, "bold"))
        top.register_btn.grid(row=2, column=3, padx=19)

        top.back_btn = Button(top.btn_frame, text='Back', width=15, height=2,
                               bg="#fc5c01", fg="white", bd=2, relief=FLAT, command=login_field, font=("roboto sans-serif", 12, "bold"))
        top.back_btn.grid(row=2, column=4)

        top.mainloop()

        
root = Tk()
obj = Login(root)
root.deiconify()
root.mainloop()
