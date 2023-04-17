from cgitb import text
from dbm.dumb import _Database
from tkinter import *
from tkinter import ttk
# import tkinter
import random
import time
import datetime
from tkinter import messagebox
from tkinter import font
from turtle import width
import mysql.connector


class Hospital:
    def __init__(self,root):
        self.root = root
        self.root.title("Hospital Management System")
        self.root.geometry('1540x800+0+0')

        self.Nameoftablets=StringVar()
        self.ref=StringVar()
        self.Dose=StringVar()
        self.NumberofTablets=StringVar()
        self.Lot=StringVar()
        self.IssueDate=StringVar()
        self.ExpDate=StringVar()
        self.DailyDose=StringVar()
        self.sideEffect=StringVar()
        self.FurtherInformation=StringVar()
        self.StorageAdvice=StringVar()
        self.DrivingUsingMachine=StringVar()
        self.howToUseMedication=StringVar()
        self.PatientId=StringVar()
        self.NHSnumber=StringVar()
        self.patientName=StringVar()
        self.DateOfBirth=StringVar()
        self.PatientAdress=StringVar()
        


        labltitle = Label(self.root,bd=20,relief=RIDGE,text="+ HOSPITAL MANAGEMENT SYSTEM",fg="red",bg="white",font=("times new roman",50,"bold"))
        labltitle.pack(side=TOP,fill=X)


        # ***********************************Data Frame***********************************

        DataFrame = Frame(self.root,bd=20,relief=RIDGE)
        DataFrame.place(x=0,y=130,width=1530,height=400)

        DataFrameLeft = LabelFrame(DataFrame, bd=10, padx = 20,relief=RIDGE,font=("times new roman",12,"bold"),text = "Patient Information")
        DataFrameLeft.place(x=0,y=5,width=980,height=350)

        DataFrameRight = LabelFrame(DataFrame, bd=10, padx = 20,relief=RIDGE,font=("times new roman",12,"bold"),text = "Prescription")
        DataFrameRight.place(x=990,y=5,width=460,height=350)



        # *************************************Buttons Frame**********************************

        ButtonFrame = Frame(self.root,bd=20,relief=RIDGE)
        ButtonFrame.place(x=0,y=530,width=1530,height=70)
    



        #**************************************Details Frame***********************************
        
        DetailFrame = Frame(self.root,bd=20,relief=RIDGE)
        DetailFrame.place(x=0,y=600,width=1530,height=190)


        # ***************************************DataFrame Left*********************************

        lablNametblet = Label(DataFrameLeft,text="Name of tablet",font=("times new roman",12,"bold"),padx=2,pady=6)
        lablNametblet.grid(row=0,column=0)

        comoboxtablet = ttk.Combobox(DataFrameLeft,textvariable=self.Nameoftablets,font=("times new roman",12,"bold"),width=37)
        comoboxtablet["value"] = ("Paracetamol","Corona Vaccine","Acetaminophen","Adderall","Amiodipine","Ativan")
        comoboxtablet.current(0)
        comoboxtablet.grid(row=0,column=1)

        lblref = Label(DataFrameLeft,font=("times new roman",12,"bold"),text = "Reference No:",padx=2)
        lblref.grid(row=1,column=0,sticky=W)
        txtref = Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.ref,width=35)
        txtref.grid(row=1,column=1)


        lblDose = Label(DataFrameLeft,font=("times new roman",12,"bold"),text = "Dose:",padx=2,pady=4)
        lblDose.grid(row=2,column=0,sticky=W)
        txtDose = Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.Dose,width=35)
        txtDose.grid(row=2,column=1)

        lblNofTablet = Label(DataFrameLeft,font=("times new roman",12,"bold"),text = "No of Tablet:",padx=2,pady=6)
        lblNofTablet.grid(row=3,column=0,sticky=W)
        txlNofTablet = Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.NumberofTablets,width=35)
        txlNofTablet.grid(row=3,column=1)

        lblLot = Label(DataFrameLeft,font=("times new roman",12,"bold"),text = "Lot:",padx=2,pady=6)
        lblLot.grid(row=4,column=0,sticky=W)
        txtLot = Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.Lot,width=35)
        txtLot.grid(row=4,column=1)

        
        lblIssueDate = Label(DataFrameLeft,font=("times new roman",12,"bold"),text = "Issue Date:",padx=2,pady=6)
        lblIssueDate.grid(row=5,column=0,sticky=W)
        txtIssueDate = Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.IssueDate,width=35)
        txtIssueDate.grid(row=5,column=1)

        lblExpDate = Label(DataFrameLeft,font=("times new roman",12,"bold"),text = "Exp Date:",padx=2,pady=6)
        lblExpDate.grid(row=6,column=0,sticky=W)
        txtExpDate = Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.ExpDate,width=35)
        txtExpDate.grid(row=6,column=1)

        lblDailyDose = Label(DataFrameLeft,font=("times new roman",12,"bold"),text = "Daily Dose:",padx=2,pady=6)
        lblDailyDose.grid(row=7,column=0,sticky=W)
        txtDailyDose = Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.DailyDose,width=35)
        txtDailyDose.grid(row=7,column=1)

        lblSideEff = Label(DataFrameLeft,font=("times new roman",12,"bold"),text = "Side Effect:",padx=2,pady=6)
        lblSideEff.grid(row=8,column=0,sticky=W)
        txtSideEff = Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.sideEffect,width=35)
        txtSideEff.grid(row=8,column=1)

        lblFrthInfo = Label(DataFrameLeft,font=("times new roman",12,"bold"),text = "Further Info:",padx=20,pady=6)
        lblFrthInfo.grid(row=0,column=2,sticky=W)
        txtFrthInfo = Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.FurtherInformation,width=35)
        txtFrthInfo.grid(row=0,column=3)


        lblbldprsr = Label(DataFrameLeft,font=("times new roman",12,"bold"),text = "Blood Pressure:",padx=20,pady=6)
        lblbldprsr.grid(row=1,column=2,sticky=W)
        txtbldprsr = Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.DrivingUsingMachine,width=35)
        txtbldprsr.grid(row=1,column=3)

        lblstgAdvi = Label(DataFrameLeft,font=("times new roman",12,"bold"),text = "Storage Advice:",padx=20,pady=6)
        lblstgAdvi.grid(row=2,column=2,sticky=W)
        txtstgAdvi = Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.StorageAdvice,width=35)
        txtstgAdvi.grid(row=2,column=3)

        lblmedication = Label(DataFrameLeft,font=("times new roman",12,"bold"),text = "Medication:",padx=20,pady=6)
        lblmedication.grid(row=3,column=2,sticky=W)
        txtmedication = Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.howToUseMedication,width=35)
        txtmedication.grid(row=3,column=3)

        lblpatntid = Label(DataFrameLeft,font=("times new roman",12,"bold"),text = "Patient ID:",padx=20,pady=6)
        lblpatntid.grid(row=4,column=2,sticky=W)
        txtpatntid = Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.PatientId,width=35)
        txtpatntid.grid(row=4,column=3)

        lblNHS = Label(DataFrameLeft,font=("times new roman",12,"bold"),text = "NHS No:",padx=20,pady=6)
        lblNHS.grid(row=5,column=2,sticky=W)
        txtNHS = Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.NHSnumber,width=35)
        txtNHS.grid(row=5,column=3)

        lblptnName = Label(DataFrameLeft,font=("times new roman",12,"bold"),text = "Patient Name:",padx=20,pady=6)
        lblptnName.grid(row=6,column=2,sticky=W)
        txtptnName = Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.patientName,width=35)
        txtptnName.grid(row=6,column=3)

        lblDOB = Label(DataFrameLeft,font=("times new roman",12,"bold"),text = "Date of Birth:",padx=20,pady=6)
        lblDOB.grid(row=7,column=2,sticky=W)
        txtDOB = Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.DateOfBirth,width=35)
        txtDOB.grid(row=7,column=3)

        lblADD = Label(DataFrameLeft,font=("times new roman",12,"bold"),text = "Patient Add:",padx=20,pady=6)
        lblADD.grid(row=8,column=2,sticky=W)
        txtADD = Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.PatientAdress,width=35)
        txtADD.grid(row=8,column=3)


        # *****************************************DataFrame Right*********************************************

        self.txtPrescription = Text(DataFrameRight,font=("arial",12,"bold"),width= 44,height=16,padx=2,pady=6)
        self.txtPrescription.grid(row=0,column=0)


        # ************************************************ Buttons **********************************************

        btnPrescription = Button(ButtonFrame,command=self.iPrescription,text="Prescription",bg="red",fg="white",font=("arial",12,"bold"),width=23,height=1,padx=6,pady=2)
        btnPrescription.grid(row=0,column=0)

        btnPrescriptionData = Button(ButtonFrame,text="Prescription Data",bg="red",fg="white",font=("arial",12,"bold"),width=23,height=1,padx=6,pady=2,command=self.iPrescriptionData)
        btnPrescriptionData.grid(row=0,column=1)

        btnUpdt = Button(ButtonFrame,text="Update",command=self.update_data,bg="red",fg="white",font=("arial",12,"bold"),width=23,height=1,padx=6,pady=2)
        btnUpdt.grid(row=0,column=2)

        btnDlt = Button(ButtonFrame,text="Delete",command=self.iDelete,bg="red",fg="white",font=("arial",12,"bold"),width=23,height=1,padx=6,pady=2)
        btnDlt.grid(row=0,column=3)

        btnClr = Button(ButtonFrame,command=self.iClear,text="Clear",bg="red",fg="white",font=("arial",12,"bold"),width=23,height=1,padx=6,pady=2)
        btnClr.grid(row=0,column=4)

        btnExt = Button(ButtonFrame,command=self.iExit,text="Exit",bg="red",fg="white",font=("arial",12,"bold"),width=23,height=1,padx=6,pady=2)
        btnExt.grid(row=0,column=5)



        # ************************************************* Table *************************************************************
        # *********************************************** scroll bar **********************************************************
        Scroll_x = ttk.Scrollbar(DetailFrame,orient=HORIZONTAL)
        Scroll_y = ttk.Scrollbar(DetailFrame,orient=VERTICAL)
        self.hospital_table=ttk.Treeview(DetailFrame,columns=("nameoftablets","ref","dose","nooftablets","lot","issuedate","expdate","dailydose","storage","NHSnumber","pname","dob","address"),xscrollcommand=Scroll_x.set,yscrollcommand=Scroll_y.set)
        Scroll_x.pack(side=BOTTOM,fill=X)
        Scroll_y.pack(side=RIGHT,fill=Y)
        Scroll_x=ttk.Scrollbar(command=self.hospital_table.xview)
        Scroll_y=ttk.Scrollbar(command=self.hospital_table.yview)

        self.hospital_table.heading("nameoftablets",text="Name of Table")
        self.hospital_table.heading("ref",text="Reference No")
        self.hospital_table.heading("dose",text="Dose")
        self.hospital_table.heading("nooftablets",text="No of Tablets")
        self.hospital_table.heading("lot",text="Lot")
        self.hospital_table.heading("issuedate",text="Issue Date")
        self.hospital_table.heading("expdate",text="Exp date")
        self.hospital_table.heading("dailydose",text="Daily Dose")
        self.hospital_table.heading("storage",text="Storage")
        self.hospital_table.heading("NHSnumber",text="NHS Number")
        self.hospital_table.heading("pname",text="Patient Name")
        self.hospital_table.heading("dob",text="Date of Birth")
        self.hospital_table.heading("address",text="Adress")
        

        self.hospital_table["show"]="headings"
        
        # self.hospital_table.pack(fill=BOTH,expand=1)


        self.hospital_table.column("nameoftablets",width=100)
        self.hospital_table.column("ref",width=100)
        self.hospital_table.column("dose",width=100)
        self.hospital_table.column("nooftablets",width=100)
        self.hospital_table.column("lot",width=100)
        self.hospital_table.column("issuedate",width=100)
        self.hospital_table.column("expdate",width=100)
        self.hospital_table.column("dailydose",width=100)
        self.hospital_table.column("storage",width=100)
        self.hospital_table.column("NHSnumber",width=100)
        self.hospital_table.column("pname",width=100)
        self.hospital_table.column("dob",width=100)
        self.hospital_table.column("address",width=100)

        self.hospital_table.pack(fill=BOTH,expand=1)
        self.hospital_table.bind("<ButtonRelease-1>",self.get_cursor)

        self.fetch_data()


        # ******************************************* Functionality Declaration(database)*****************************************

    def iPrescriptionData(self):
        if self.Nameoftablets.get()=="" or self.ref.get()=="":
            messagebox.showerror("Error","All fields are required")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Shadan8858@khan", database="mysystem")
            my_cursor = conn.cursor()
            
            my_cursor.execute("INSERT INTO mydata VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                              self.Nameoftablets.get(),
                                                                                              self.ref.get(),
                                                                                              self.Dose.get(),
                                                                                              self.NumberofTablets.get(),
                                                                                              self.Lot.get(),
                                                                                              self.IssueDate.get(),
                                                                                              self.ExpDate.get(),
                                                                                              self.DailyDose.get(),
                                                                                              self.StorageAdvice.get(),
                                                                                              self.NHSnumber.get(),
                                                                                              self.patientName.get(),
                                                                                              self.DateOfBirth.get(),
                                                                                              self.PatientAdress.get()
                                                                                              ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("success"," Record has been inserted")


    def update_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="123", database="mysystem")
        my_cursor = conn.cursor()
        my_cursor.execute('update mydata set NameofTablets=%s,dose=%s,NumberofTablets=%s,lot=%s,IssueDate=%s,ExpDate=%s,dailyDose=%s,storage=%s,NHSnumber=%s,patientName=%s,DOB=%s,patientAdd=%s where Reference_No=%s',(
                                                self.Nameoftablets.get(),
                                                self.Dose.get(),
                                                self.NumberofTablets.get(),
                                                self.Lot.get(),
                                                self.IssueDate.get(),
                                                self.ExpDate.get(),
                                                self.DailyDose.get(),
                                                self.StorageAdvice.get(),
                                                self.NHSnumber.get(),
                                                self.patientName.get(),
                                                self.DateOfBirth.get(),
                                                self.PatientAdress.get(),
                                                self.ref.get()
                                            ))
        conn.commit()
        self.fetch_data()
        conn.close()

        messagebox.showinfo("Update"," Record has been updated successfully")


    def iPrescription(self):
        self.txtPrescription.insert(END,"Name of Tablets:\t\t\t" + self.Nameoftablets.get()+"\n")
        self.txtPrescription.insert(END,"Reference No:\t\t\t" + self.ref.get()+"\n")
        self.txtPrescription.insert(END,"Dose:\t\t\t" + self.Dose.get()+"\n")
        self.txtPrescription.insert(END,"Number of Tablets:\t\t\t" + self.NumberofTablets.get()+"\n")
        self.txtPrescription.insert(END,"lot:\t\t\t" + self.Lot.get()+"\n")
        self.txtPrescription.insert(END,"Issue Date:\t\t\t" + self.IssueDate.get()+"\n")
        self.txtPrescription.insert(END,"Expiry Date:\t\t\t" + self.ExpDate.get()+"\n")
        self.txtPrescription.insert(END,"Daily Dose:\t\t\t" + self.DailyDose.get()+"\n")
        self.txtPrescription.insert(END,"Side Effect:\t\t\t" + self.sideEffect.get()+"\n")
        self.txtPrescription.insert(END,"Further Information:\t\t\t" + self.FurtherInformation.get()+"\n")
        self.txtPrescription.insert(END,"Storage Advice:\t\t\t" + self.StorageAdvice.get()+"\n")
        self.txtPrescription.insert(END,"Driving using Machine:\t\t\t" + self.DrivingUsingMachine.get()+"\n")
        self.txtPrescription.insert(END,"Patient ID:\t\t\t" + self.PatientId.get()+"\n")
        self.txtPrescription.insert(END,"NHS Number:\t\t\t" + self.NHSnumber.get()+"\n")
        self.txtPrescription.insert(END,"Patient Name:\t\t\t" + self.patientName.get()+"\n")
        self.txtPrescription.insert(END,"Date of Birth:\t\t\t" + self.DateOfBirth.get()+"\n")
        self.txtPrescription.insert(END,"Patient Address:\t\t\t" + self.PatientAdress.get()+"\n")


    def iDelete(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Shadan8858@khan", database="mysystem")
        my_cursor = conn.cursor()
        query = "DELETE FROM mydata WHERE Reference_No=%s"
        value = (self.ref.get(),)
        my_cursor.execute(query,value)

        conn.commit()
        conn.close()
        self.fetch_data()
        messagebox.showinfo("Delete", "Patient infromation deleted successfully")
    

    def iClear(self):
        self.Nameoftablets.set("")
        self.ref.set("")
        self.Dose.set("")
        self.NumberofTablets.set("")
        self.Lot.set("")
        self.IssueDate.set("")
        self.ExpDate.set("")
        self.sideEffect.set("")
        self.FurtherInformation.set("")
        self.StorageAdvice.set("")
        self.DrivingUsingMachine.set("")
        self.howToUseMedication.set("")
        self.PatientId.set("")
        self.NHSnumber.set("")
        self.patientName.set("")
        self.DateOfBirth.set("")
        self.PatientAdress.set("")
        self.txtPrescription.delete("1.0",END)

    
    def iExit(self):
        iExit = messagebox.askyesno("Hospital Management System","Confirm You want to exit")
        if iExit>0:
            root.destroy()
            return





    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Shadan8858@khan", database="mysystem")
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT * FROM mydata")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.hospital_table.delete(*self.hospital_table.get_children())
            for i in rows:
                self.hospital_table.insert("",END,values=i)
            conn.commit()
        conn.close()
    

    # return the data in column again
    
    def get_cursor(self,event =""):
        cursor_row = self.hospital_table.focus()
        content = self.hospital_table.item(cursor_row)
        row = content["values"]
        self.Nameoftablets.set(row[0])
        self.ref.set(row[1])
        self.Dose.set(row[2])
        self.NumberofTablets.set(row[3])
        self.Lot.set(row[4])
        self.IssueDate.set(row[5])
        self.ExpDate.set(row[6])
        self.DailyDose.set(row[7])
        self.StorageAdvice.set(row[8])
        self.NHSnumber.set(row[9])
        self.patientName.set(row[10])
        self.DateOfBirth.set(row[11])
        self.patientName.set(row[12])



      





root = Tk()
ob = Hospital(root)
root.mainloop()

