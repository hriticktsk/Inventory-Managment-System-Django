from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql


class Dashboard:
    def __init__(self, root):

        self.root = root
        self.root.title("Dashboard Page")
        self.root.withdraw()
        x = (self.root.winfo_screenwidth() - self.root.winfo_reqwidth()) / 3
        y = (self.root.winfo_screenheight() - self.root.winfo_reqheight()) / 5
        self.root.geometry("590x424+%d+%d" % (x, y))
        self.root.resizable(False, False)

        # Frame
        self.txt_frame = Frame(
            self.root, bd=4, relief=RIDGE, bg="navy")
        self.txt_frame.place(x=0, y=0, width=790, height=425)

        # Frame for Buttons
        self.btn_frame = Frame(
            self.txt_frame, bd=2, relief=RIDGE, bg="navy")
        self.btn_frame.place(x=60, y=43, width=466, height=330)

        # Input
        self.input_btn = Button(self.btn_frame, text='Product Input Fields', width=40, height=3, bd=2, relief=FLAT, bg="#fc5c01", fg="white",
                                font=("roboto sans-serif", 13, "bold"), command=self.input_view)
        self.input_btn.grid(row=1, column=5, pady=28, padx=23)

        # View
        self.view_btn = Button(self.btn_frame, text='Inventory & Sales', width=40, height=3, bd=2, relief=FLAT, bg="#fc5c01", fg="white",
                               font=("roboto sans-serif", 13, "bold"), command=self.view_page)
        self.view_btn.grid(row=2, column=5)

        # Close
        self.close_btn = Button(self.btn_frame, text='Exit System', width=40, height=3, bd=2, relief=FLAT, bg="#fc5c01", fg="white",
                                font=("roboto sans-serif", 13, "bold"), command=self.close_page)
        self.close_btn.grid(row=3, column=5, pady=28, padx=23)

    def input_view(self):

        top = Toplevel()
        top.title("Product Inventory Management System")
        
        x = (top.winfo_screenwidth() - top.winfo_reqwidth()) / 4
        y = (top.winfo_screenheight() - top.winfo_reqheight()) / 5
        top.geometry("790x424+%d+%d" % (x, y))
        top.resizable(False, False)

        def add_item():
            
            if product.get() == '' or customer.get() == '' or retailer.get() == '' or price.get() == '' or address.get() == '' or date.get() == '' or amount.get() == '' or change.get() == '':
                messagebox.showerror(
                    'Required Fields', 'Please include all fields')
                return
            else:
                con = pymysql.connect(
                    host="localhost", user="root", password="root", database="proinv")
                cur = con.cursor()

                cur.execute(
                    "insert into crud (product ,customer, retailer, price, address, date, amount, totalchange) values(%s,%s,%s,%s,%s,%s,%s,%s)",
                    (product.get(),
                     customer.get(),
                     retailer.get(),
                     price.get(),
                     address.get(),
                     date.get(),
                     amount.get(),
                     change.get()
                     ))
                con.commit()
                con.close()
                messagebox.showinfo("Success", "Adding Items Successfuly")
                clear_text()
               
                

        def clear_text():
            top.product_entry.delete(0, END)
            top.customer_entry.delete(0, END)
            top.retailer_entry.delete(0, END)
            top.price_entry.delete(0, END)
            top.address_entry.delete(0, END)
            top.date_entry.delete(0, END)
            top.amount_entry.delete(0, END)
            top.change_entry.delete(0, END)

        def compute():
            change_entry = (amount.get() - price.get())
            change.set(change_entry)

        # Head Label
        top.lbl_title = Label(
            top, text="Product Inventory Management System", bd=4, fg="white", relief=RIDGE,  bg="#fc5c00", font=("roboto sans-serif", 23), pady=7)
        top.lbl_title.pack(side=TOP, fill=X)

        # Frame
        top.txt_frame = Frame(
            top, bd=4, relief=RIDGE, bg="navy")
        top.txt_frame.place(x=0, y=55, width=790, height=370)
        # Space
        top.product_label = Label(top.txt_frame, text='',
                                  font=('', 14), pady=10, padx=10, bg="navy", fg="white").grid(row=0, column=0, sticky=W)
        # Product
        product = StringVar()
        top.product_label = Label(top.txt_frame, text='Product Name :',
                                  font=('bold', 14), pady=10, padx=14, bg="navy", fg="white").grid(row=1, column=0, sticky=W)
        top.product_entry = Entry(
            top.txt_frame, textvariable=product, width=25, bd=3, font=("bold", 11))
        top.product_entry.grid(row=1, column=1)
        # Customer
        customer = StringVar()
        top.customer_label = Label(top.txt_frame, text='Customer Name :', font=(
            'bold', 14), padx=10, bg="navy", fg="white").grid(row=1, column=2, sticky=W)
        top.customer_entry = Entry(top.txt_frame, textvariable=customer,
                                   width=25, bd=3, font=("bold", 11))
        top.customer_entry.grid(row=1, column=3)
        # Retailer
        retailer = StringVar()
        top.retailer_label = Label(top.txt_frame, text='Retailer Name :', font=(
            'bold', 14), padx=12, bg="navy", fg="white").grid(row=2, column=0, sticky=W)
        top.retailer_entry = Entry(top.txt_frame, textvariable=retailer,
                                   width=25, bd=3, font=("bold", 11))
        top.retailer_entry.grid(row=2, column=1)

        # Price
        price = IntVar()
        top.price_label = Label(top.txt_frame, text='Product Price :', font=('bold', 14),
                                padx=10, bg="navy", fg="white").grid(row=2, column=2, sticky=W)
        top.price_entry = Entry(top.txt_frame, textvariable=price,
                                width=25, bd=3, font=("bold", 11))
        top.price_entry.grid(row=2, column=3)
        # Address
        address = StringVar()
        top.address_label = Label(top.txt_frame, text='Address :', font=('bold', 14),
                               padx=10, pady=10, bg="navy", fg="white").grid(row=3, column=0, sticky=W)
        top.address_entry = Entry(top.txt_frame, textvariable=address,
                               width=25, bd=3, font=("bold", 11))
        top.address_entry.grid(row=3, column=1)
        # Date
        date = StringVar()
        top.date_label = Label(top.txt_frame, text='Transact Date :', font=('bold', 14),
                                   padx=10, pady=10, bg="navy", fg="white").grid(row=3, column=2, sticky=W)
        top.date_entry = Entry(top.txt_frame, textvariable=date,
                                   width=25, bd=3, font=("bold", 11))
        top.date_entry.grid(row=3, column=3)
        # Amount
        amount = IntVar()
        top.amount_label = Label(top.txt_frame, text='Amount :', font=('bold', 14),
                                 padx=10, bg="navy", fg="white").grid(row=4, column=0, sticky=W)
        top.amount_entry = Entry(top.txt_frame, textvariable=amount,
                                 width=25, bd=3, font=("bold", 11))
        top.amount_entry.grid(row=4, column=1)
        # Change
        change = IntVar()
        top.change_label = Label(top.txt_frame, text='Customer Change :', font=('bold', 14),
                              padx=10, bg="navy", fg="white").grid(row=4, column=2, sticky=W)
        top.change_entry = Entry(top.txt_frame, textvariable=change,
                              width=25, bd=3, font=("bold", 11))
        top.change_entry.grid(row=4, column=3)

        # Frame for Buttons
        top.btn_frame = Frame(
            top.txt_frame, bd=2, relief=RIDGE, bg="navy")
        top.btn_frame.place(x=0, y=252, width=781, height=110)

        # Button
        # Space
        top.space_lbl = Label(top.btn_frame, text='',
                              font=('bold', 14), bg="navy", fg="white", padx=25).grid(
            row=1, column=1, sticky=W)

        top.add_btn = Button(top.btn_frame, text='Ok', width=20, height=2, bd=2, relief=FLAT, bg="#fc5c01", fg="white",
                             font=("roboto sans-serif", 12, "bold"), command=add_item)
        top.add_btn.grid(row=1, column=2, pady=26)

        top.delete_btn = Button(top.btn_frame, text='Clear', width=20, height=2, bg="#fc5c01", fg="white", bd=2, relief=FLAT,
                                font=("roboto sans-serif", 12, "bold"), command=clear_text)
        top.delete_btn.grid(row=1, column=3, padx=22)

        top.compute_btn = Button(top.btn_frame, text='Compute', width=20, height=2, bg="#fc5c01", fg="white", bd=2, relief=FLAT,
                               font=("roboto sans-serif", 12, "bold"), command=compute)
        top.compute_btn.grid(row=1, column=4)


        top.deiconify()
        top.mainloop()


    def view_page(self):
        top = Toplevel()
        top.title("Product Inventory Management System")
        x = (top.winfo_screenwidth() -
             top.winfo_reqwidth()) / 10
        y = (top.winfo_screenheight() - top.winfo_reqheight()) / 30
        top.geometry("1130x665+%d+%d" % (x, y))
        top.resizable(False, False)


        def populate_data():

            con = pymysql.connect(
                host="localhost", user="root", password="root", database="proinv")
            cur = con.cursor()

            cur.execute("select * from crud")
            rows = cur.fetchall()

            if len(rows) != 0:
                top.data_list.delete(*top.data_list.get_children())
                for row in rows:
                    top.data_list.insert('', END, values=row)
                con.commit()
            con.close()

        def clear_text():
            top.id_entry.delete(0, END)
            top.product_entry.delete(0, END)
            top.customer_entry.delete(0, END)
            top.retailer_entry.delete(0, END)
            top.price_entry.delete(0, END)
            top.address_entry.delete(0, END)
            top.date_entry.delete(0, END)
            top.amount_entry.delete(0, END)
            top.change_entry.delete(0, END)

        def update_item():
            con = pymysql.connect(
                host="localhost", user="root", password="root", database="proinv")
            cur = con.cursor()
            cur.execute(
                "update crud set id=%s, product=%s, customer=%s, retailer=%s, price=%s, address=%s, date=%s, amount=%s, totalchange=%s where crud . id=%s",
                (id_text.get(),
                 product_text.get(),
                 customer_text.get(),
                 retailer_text.get(),
                 price_text.get(),
                 address_text.get(),
                 date_text.get(),
                 amount_text.get(),
                 change_text.get(),
                 id_text.get()
                 ))
            con.commit()
            messagebox.showinfo("Success", "Update Successfuly")
            populate_data()
            clear_text()
            con.close()

        def delete_item():
            con = pymysql.connect(
                host="localhost", user="root", password="root", database="proinv")
            cur = con.cursor()
            cur.execute("delete from crud where id=%s", id_text.get())

            dlt = messagebox.askyesno(
                'Gadgets', 'Do you want to delete this file ')

            clear_text()
            con.commit()

            if dlt > 0:
                clear_text()
                populate_data()

            con.close()

        def select_item(ev):

            cursor_row = top.data_list.focus()
            contents = top.data_list.item(cursor_row)
            row = contents['values']
            id_text.set(row[0])
            product_text.set(row[1])
            customer_text.set(row[2])
            retailer_text.set(row[3])
            price_text.set(row[4])
            address_text.set(row[5])
            date_text.set(row[6])
            amount_text.set(row[7])
            change_text.set(row[8])

        def clear():
            top.id_entry.delete(0, END)
            top.product_entry.delete(0, END)
            top.customer_entry.delete(0, END)
            top.retailer_entry.delete(0, END)
            top.price_entry.delete(0, END)
            top.address_entry.delete(0, END)
            top.date_entry.delete(0, END)
            top.amount_entry.delete(0, END)
            top.change_entry.delete(0, END)

        def close():
            ext = messagebox.askyesno(
                'Database', 'Do you want to this window ')

            if ext > 0:
                top.destroy()

        # Head Label
        top.lbl_title = Label(
            top, text="Product Inventory Sales Management System", bd=4, fg="white", relief=RIDGE,  bg="#fc5c00", font=("roboto sans-serif", 23), pady=7)
        top.lbl_title.pack(side=TOP, fill=X)

        # Frame Table
        top.detail_frame = Frame(
            top, bd=4, relief=RIDGE, bg="navy")
        top.detail_frame.place(x=0, y=390, width=1130, height=276)

        # Frame Input
        top.txt_frame = Frame(
            top, bd=4, relief=RIDGE, bg="navy")
        top.txt_frame.place(x=0, y=55, width=1130, height=340)

        # Buttons Frame
        top.btn_frame = Frame(
            top.detail_frame, bd=3, relief=RIDGE, bg="navy")
        top.btn_frame.place(x=0, y=170, width=1122, height=98)

        # Button Here
        # Space for Buttons
        top.space_label = Label(top.btn_frame, text='',
                                font=('', 10), bg="navy", fg="white").grid(row=1, column=2, pady=20, padx=5)
        # Edit
        top.edit_btn = Button(top.btn_frame, text='Change', width=24, height=2, bd=2, relief=FLAT, bg="#fc5c01", fg="white",
                              font=("roboto sans-serif", 13, "bold"), command=update_item)
        top.edit_btn.grid(row=1, column=3, pady=20, padx=10)

        # Delete
        top.delete_btn = Button(top.btn_frame, text='Delete', width=24, height=2, bd=2, relief=FLAT, bg="#fc5c01", fg="white",
                                font=("roboto sans-serif", 13, "bold"), command=delete_item)
        top.delete_btn.grid(row=1, column=4, pady=20, padx=10)

        # Back
        top.bck_btn = Button(top.btn_frame, text='Clear', width=24, height=2, bg="#fc5c01", fg="white", bd=2, relief=FLAT,
                             font=("roboto sans-serif", 13, "bold"), command=clear)
        top.bck_btn.grid(row=1, column=5, padx=12)

        # Exit
        top.exit_btn = Button(top.btn_frame, text='Exit', width=24, height=2, bg="#fc5c01", fg="white", bd=2, relief=FLAT,
                              font=("roboto sans-serif", 13, "bold"), command=close)
        top.exit_btn.grid(row=1, column=6, padx=12)

        # Space
        top.space_label = Label(top.txt_frame, text='',
                                font=('', 10), bg="navy", fg="white").grid(row=0, column=2, pady=10, sticky=W, padx=43)
        # ID
        id_text = StringVar()
        top.id_label = Label(top.txt_frame, text='List Number :',
                             font=('bold', 14), bg="navy", fg="white").grid(row=1, column=0, sticky=W, padx=55)
        top.id_entry = Entry(
            top.txt_frame, textvariable=id_text, width=25, bd=3, font=("bold", 15))
        top.id_entry.grid(row=1, column=1)

        # Product
        product_text = StringVar()
        top.product_label = Label(top.txt_frame, text='Product Name :',
                                  font=('bold', 14), bg="navy", fg="white").grid(row=2, column=0, sticky=W, padx=52)
        top.product_entry = Entry(
            top.txt_frame, textvariable=product_text, width=25, bd=3, font=("bold", 15))
        top.product_entry.grid(row=2, column=1)

        # Customer
        customer_text = StringVar()
        top.customer_label = Label(top.txt_frame, text='Customer Name :', font=(
            'bold', 14), bg="navy", fg="white").grid(row=1, column=2, sticky=W, padx=50)
        top.customer_entry = Entry(top.txt_frame, textvariable=customer_text,
                                   width=25, bd=3, font=("bold", 15))
        top.customer_entry.grid(row=1, column=3)

        # Retailer
        retailer_text = StringVar()
        top.retailer_label = Label(top.txt_frame, text='Retailer Name :', font=(
            'bold', 14), bg="navy", fg="white").grid(row=3, column=0, sticky=W, padx=50)
        top.retailer_entry = Entry(top.txt_frame, textvariable=retailer_text,
                                   width=25, bd=3, font=("bold", 15))
        top.retailer_entry.grid(row=3, column=1)

        # Price
        price_text = StringVar()
        top.price_label = Label(top.txt_frame, text='Product Price :', font=('bold', 14),
                                bg="navy", fg="white").grid(row=2, column=2, sticky=W, padx=50, pady=20)
        top.price_entry = Entry(top.txt_frame, textvariable=price_text,
                                width=25, bd=3, font=("bold", 15))
        top.price_entry.grid(row=2, column=3)

        # Address
        address_text = StringVar()
        top.address_label = Label(top.txt_frame, text='Customer Address :', font=('bold', 14),
                               bg="navy", fg="white").grid(row=4, column=0, sticky=W, padx=50,  pady=20)
        top.address_entry = Entry(top.txt_frame, textvariable=address_text,
                               width=25, bd=3, font=("bold", 15))
        top.address_entry.grid(row=4, column=1)

        # Date
        date_text = StringVar()
        top.date_label = Label(top.txt_frame, text='Transact Date :', font=('bold', 14),
                                   bg="navy", fg="white").grid(row=5, column=0, sticky=W, padx=50)
        top.date_entry = Entry(top.txt_frame, textvariable=date_text,
                                   width=25, bd=3, font=("bold", 15))
        top.date_entry.grid(row=5, column=1)

        # Amount
        amount_text = StringVar()
        top.amount_label = Label(top.txt_frame, text='Total Amount :', font=('bold', 14),
                                 bg="navy", fg="white").grid(row=3, column=2, sticky=W, padx=50)
        top.amount_entry = Entry(top.txt_frame, textvariable=amount_text,
                                 width=25, bd=3, font=("bold", 15))
        top.amount_entry.grid(row=3, column=3)

        # Change
        change_text = StringVar()
        top.change_label = Label(top.txt_frame, text='Total Change :', font=('bold', 14),
                              bg="navy", fg="white").grid(row=4, column=2, sticky=W, padx=50)
        top.change_entry = Entry(top.txt_frame, textvariable=change_text,
                              width=25, bd=3, font=("bold", 15))
        top.change_entry.grid(row=4, column=3)

        # Listbox Frame
        top.list_frame = Frame(
            top.detail_frame, bd=2, relief=RIDGE, bg="navy")
        top.list_frame.place(x=0, y=0, width=1122, height=170)

        # Treeview Scrollbar
        scroll_x = Scrollbar(top.list_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(top.list_frame, orient=VERTICAL)

        # Treeview
        top.data_list = ttk.Treeview(top.list_frame, height=12, columns=(
            "list", "product", "customer", "retailer", "price", "address", "date", "amount", "change"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        top.data_list.configure(yscrollcommand=scroll_x.set)
        scroll_x.configure(command=top.data_list.xview)

        top.data_list.configure(yscrollcommand=scroll_y.set)
        scroll_y.configure(command=top.data_list.yview)

        top.data_list.heading("list", text="List No.")
        top.data_list.heading("product", text="Product Name")
        top.data_list.heading("customer", text="Customer Name")
        top.data_list.heading("retailer", text="Retailer Name")
        top.data_list.heading("price", text="Price")
        top.data_list.heading("address", text="Address")
        top.data_list.heading("date", text="Date")
        top.data_list.heading("amount", text="Amount")
        top.data_list.heading("change", text="Change")

        top.data_list['show'] = 'headings'

        top.data_list.column("list", width=30)
        top.data_list.column("product", width=160)
        top.data_list.column("customer", width=146)
        top.data_list.column("retailer", width=140)
        top.data_list.column("price", width=66)
        top.data_list.column("address", width=80)
        top.data_list.column("date", width=80)
        top.data_list.column("amount", width=50)
        top.data_list.column("change", width=30)

        top.data_list.pack(fill=BOTH, expand=1)

        top.data_list.bind('<ButtonRelease-1>', select_item)

        # To show all Data in Treeview
        populate_data()

    def close_page(self):
        ext = messagebox.askyesno(
            'Dashboard', 'Do you want to this window ')

        if ext > 0:
            self.root.destroy()


root = Tk()
obj = Dashboard(root)
root.deiconify()
root.mainloop()
