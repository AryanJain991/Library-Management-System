from tkinter import*
from tkinter import ttk


class LibraryManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Library Management system")
        self.root.geometry("1550x800+0+0")


        lbtitle=Label(self.root,text="LIBRARY MANAGEMENT SYSTEM",bg="powder blue",fg="green",bd=20,relief=RIDGE,font=("times new roman",50,"bold",),padx=2,pady=6)
        lbtitle.pack(side=TOP,fill=X)

        frame=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        frame.place(x=0,y=130,width=1530,height=400)


        # =================================DataFrameLeft=============================================================================
        DataFrameLeft=LabelFrame(frame,text="Library Membership Information,",bg="powder blue",fg="green",bd=12,relief=RIDGE,font=("arial",12,"bold",))
        DataFrameLeft.place(x=0,y=5,width=900,height=350)

        lblMember=Label(DataFrameLeft,bg="powder blue",text="Member Type",font=("arial",12,"bold",),padx=2,pady=6)
        lblMember.grid(row=0,column=0,sticky=W)

        comMember=ttk.Combobox(DataFrameLeft,font=("times new roman",15,"bold"),width=27,state="readonly")
        comMember["values"]=("Admin Staff","Lecturer","Student")
        comMember.current(0)
        comMember.grid(row=0,column=1)

        lblMember=Label(DataFrameLeft,bg="powder blue",text="PRN No",font=("times new roman",12,"bold",),padx=2,pady=6)
        lblMember.grid(row=1,column=0,sticky=W)


        lblPRN_NO=Label(DataFrameLeft,font=("arial",12,"bold"),text="PRN No:",padx=2,bg="powder blue")
        lblPRN_NO.grid(row=1,column=0,sticky=W)
        txtPRN_NO=Entry(DataFrameLeft,font=("arial",13,"bold"),width="29")
        txtPRN_NO.grid(row=1,column=1)

        lblTitle=Label(DataFrameLeft,font=("arial",12,"bold"),text="ID No:",padx=2,pady=4,bg="powder blue")
        lblTitle.grid(row=2,column=0,sticky=W)
        txtTitle=Entry(DataFrameLeft,font=("arial",13,"bold"),width="29")
        txtTitle.grid(row=2,column=1)

        lblFirstName=Label(DataFrameLeft,font=("arial",12,"bold"),text="FirstName:",padx=2,pady=6,bg="powder blue")
        lblFirstName.grid(row=3,column=0,sticky=W)
        txtFirstName=Entry(DataFrameLeft,font=("arial",13,"bold"),width="29")
        txtFirstName.grid(row=3,column=1)

        lblLastName=Label(DataFrameLeft,font=("arial",12,"bold"),text="LastName:",padx=2,pady=6,bg="powder blue")
        lblLastName.grid(row=4,column=0,sticky=W)
        txtLastName=Entry(DataFrameLeft,font=("arial",13,"bold"),width="29")
        txtLastName.grid(row=4,column=1)  

        lblAddress1=Label(DataFrameLeft,font=("arial",12,"bold"),text="Address1:",padx=2,pady=6,bg="powder blue")
        lblAddress1.grid(row=5,column=0,sticky=W)
        txtAddress1=Entry(DataFrameLeft,font=("arial",13,"bold"),width="29")
        txtAddress1.grid(row=5,column=1)   

        lblAddress2=Label(DataFrameLeft,font=("arial",12,"bold"),text="Address2:",padx=2,pady=6,bg="powder blue")
        lblAddress2.grid(row=6,column=0,sticky=W)
        txtAddress2=Entry(DataFrameLeft,font=("arial",13,"bold"),width="29")
        txtAddress2.grid(row=6,column=1)

        lblPostCode=Label(DataFrameLeft,font=("arial",12,"bold"),text="PostCode:",padx=2,pady=4,bg="powder blue")
        lblPostCode.grid(row=7,column=0,sticky=W)
        txtPostCode=Entry(DataFrameLeft,font=("arial",13,"bold"),width="29")
        txtPostCode.grid(row=7,column=1)

        lblMobile=Label(DataFrameLeft,font=("arial",12,"bold"),text="Mobile:",padx=2,pady=6,bg="powder blue")
        lblMobile.grid(row=8,column=0,sticky=W)
        txtMobile=Entry(DataFrameLeft,font=("arial",13,"bold"),width="29")
        txtMobile.grid(row=8,column=1)        

        lblBookId=Label(DataFrameLeft,font=("arial",12,"bold"),text="BookId:",padx=2,bg="powder blue")
        lblBookId.grid(row=0,column=2,sticky=W)
        txtBookId=Entry(DataFrameLeft,font=("arial",12,"bold"),width="29")
        txtBookId.grid(row=0,column=3)   

        lblBookTitle=Label(DataFrameLeft,font=("arial",12,"bold"),text="Book Title:",padx=2,pady=6,bg="powder blue")
        lblBookTitle.grid(row=1,column=2,sticky=W)
        txtBookTitle=Entry(DataFrameLeft,font=("arial",12,"bold"),width="29")
        txtBookTitle.grid(row=1,column=3)       


        lblAuthor=Label(DataFrameLeft,font=("arial",12,"bold"),text="Author Name:",padx=2,pady=6,bg="powder blue")
        lblAuthor.grid(row=2,column=2,sticky=W)
        txtAuthor=Entry(DataFrameLeft,font=("arial",12,"bold"),width="29")
        txtAuthor.grid(row=2,column=3) 

        lblDateBorrowed=Label(DataFrameLeft,font=("arial",12,"bold"),text="Date Borrowed:",padx=2,pady=6,bg="powder blue")
        lblDateBorrowed.grid(row=3,column=2,sticky=W)
        txtDateBorrowed=Entry(DataFrameLeft,font=("arial",12,"bold"),width="29")
        txtDateBorrowed.grid(row=3,column=3)    

        lblDateDue=Label(DataFrameLeft,font=("arial",12,"bold"),text="Date Due:",padx=2,pady=6,bg="powder blue")
        lblDateDue.grid(row=4,column=2,sticky=W)
        txtDateDue=Entry(DataFrameLeft,font=("arial",12,"bold"),width="29")
        txtDateDue.grid(row=4,column=3)      

        lblDaysOnBook=Label(DataFrameLeft,font=("arial",12,"bold"),text="Days On Book:",padx=2,pady=6,bg="powder blue")
        lblDaysOnBook.grid(row=5,column=2,sticky=W)
        txtDaysOnBook=Entry(DataFrameLeft,font=("arial",12,"bold"),width="29")
        txtDaysOnBook.grid(row=5,column=3)            

        lblLateReturnFine=Label(DataFrameLeft,font=("arial",12,"bold"),text="Late Return Fine:",padx=2,pady=6,bg="powder blue")
        lblLateReturnFine.grid(row=6,column=2,sticky=W)
        txtLateReturnFine=Entry(DataFrameLeft,font=("arial",12,"bold"),width="29")
        txtLateReturnFine.grid(row=6,column=3)  

        lblDateOverdate=Label(DataFrameLeft,font=("arial",12,"bold"),text="Date Over Due:",padx=2,pady=6,bg="powder blue")
        lblDateOverdate.grid(row=7,column=2,sticky=W)
        txtDateOverdate=Entry(DataFrameLeft,font=("arial",12,"bold"),width="29")
        txtDateOverdate.grid(row=7,column=3)

        lblActualPrice=Label(DataFrameLeft,font=("arial",12,"bold"),text="Actual Price:",padx=2,pady=6,bg="powder blue")
        lblActualPrice.grid(row=8,column=2,sticky=W)
        txtActualPrice=Entry(DataFrameLeft,font=("arial",12,"bold"),width="29")
        txtActualPrice.grid(row=8,column=3)  

        # =============================DataFrame Right==============================                    
  

        DataFrameRight=LabelFrame(frame,bd=12,padx=20,relief=RIDGE,bg="powder blue",font=("arial",12,"bold"),text="Book Details")
        DataFrameRight.place(x=870,y=5,width=580,height=350)

        self.txtBox=Text(DataFrameRight,font=("arial",12,"bold"),width=32,height=16,padx=2,pady=6)
        self.txtBox.grid(row=0,column=2)

        listScrollbar=Scrollbar(DataFrameRight)
        listScrollbar.grid(row=0,column=1,sticky="ns")

        listBooks=['Head First Book','Learn Python The Hard Way','Python Programming','Secrate Rahsaya', 'Python CookBook','Introduction to Machine Learning','Fluent Python','programming Python','the Algorithm','The technich Python','Machine Tecno','My Python','Joss Elif guru','Elite Jungle Python', 'Jungli python','Mumbai Python','Pune Python','Guru Of Python','Yellow Dragon','Red Dragon','Machine Python','Advance Python','intro Python','RedChilli Python','Ishq Python']

        listBox=Listbox(DataFrameRight,font=("arial",12,"bold"),width=20,height=16)
        listBox.grid(row=0,column=0,padx=4)
        listScrollbar.config(command=listBox.yview)

        for item in listBooks:
            listBox.insert(END,item)

        # ====================================Buttons Frame =======================================
        Framebutton=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        Framebutton.place(x=0,y=530,width=1530,height=70)

        btnAdddata=Button(Framebutton,text="Add Data",font=("arial",12,"bold"),width=23,bg="blue",fg="white")
        btnAdddata.grid(row=0,column=0)
        
        btnAdddata=Button(Framebutton,text="Show Data",font=("arial",12,"bold"),width=23,bg="blue",fg="white")
        btnAdddata.grid(row=0,column=1)

        btnAdddata=Button(Framebutton,text="Update",font=("arial",12,"bold"),width=23,bg="blue",fg="white")
        btnAdddata.grid(row=0,column=2) 

        btnAdddata=Button(Framebutton,text="Delete",font=("arial",12,"bold"),width=23,bg="blue",fg="white")
        btnAdddata.grid(row=0,column=3)         

        btnAdddata=Button(Framebutton,text="Reset",font=("arial",12,"bold"),width=23,bg="blue",fg="white")
        btnAdddata.grid(row=0,column=4)            

        btnAdddata=Button(Framebutton,text="Exit",font=("arial",12,"bold"),width=23,bg="blue",fg="white")
        btnAdddata.grid(row=0,column=5)                  
        # ====================================InformationFrame =======================================
        FrameDetails=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        FrameDetails.place(x=0,y=590,width=1530,height=210)




        Table_frame=Frame(FrameDetails,bd=6,relief=RIDGE,bg="powder blue")
        Table_frame.place(x=0,y=2,width=1460,height=196)

        self.library_table=ttk.Treeview(Table_frame,columns=("membertype","prnno","firstname","lastname","address1","adress2","postid","mobile","bookid","booktitle","author","dateborrowed","datadue","days","latereturnfine","dateoverdue","finalprice"))




        # self.library_table.heading("membertype",text="Member Type")
        # self.library_table.heading("prnno",text="Reference No.")
        # self.library_table.heading("title",text="Title")
        # self.library_table.heading("firstname",text="First Name")
        # self.library_table.heading("lastname",text="Last Name")




if __name__ == "__main__":
    root=Tk()
    obj=LibraryManagementSystem(root)
    root.mainloop()