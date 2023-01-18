from tkinter import *
from tkinter import messagebox
import mysql.connector
from screens.home import createHomePage

# mysql database connector
mydb = mysql.connector.connect(
    user="root",
    password="sql123",
)
cursor = mydb.cursor(buffered=True)
# verify login fields


def verifyLogin():
    global uname, password
    uname = name.get()
    password = pwd.get()
    cursor.execute('use DietTracker')
    if (uname == '' or password == ''):
        messagebox.showerror('Error', 'Fields cannot be left empty')
    elif (uname != '' and password != ''):
        try:
            cursor.execute("select * from userdata where username = '" +
                           uname + "' and password = '" + password + "'")
            result = cursor.fetchall()
            if result == []:
                messagebox.showerror('Error', 'Invalid credentials')
            else:
                root.destroy()
                createHomePage(uname.title())
        except:
            messagebox.showerror(
                'Error', "Username and Password\ndoesn't exist")
    else:
        messagebox.showerror('Error', 'Incorrect Credentials')

# verify registration fields


def verifyReg():
    global uname, password, phone
    uname = name.get()
    password = pwd.get()
    phone = pnum.get()
    cursor.execute('use DietTracker')
    try:
        cursor.execute('create table userdata(username varchar(255) primary key not null, password varchar(255) not null, phoneNo varchar(255) not null, gender varchar(1), height varchar(255), weight varchar(255), age varchar(255))')
    except:
        None

    cursor.execute(f"select * from userdata where username='{uname}'")

    if (uname == '' or password == '' or phone == ''):
        messagebox.showerror('Error', 'Fields cannot be left empty')
    elif (cursor.fetchall() != []):
        messagebox.showerror('Error', 'Username exists')
    elif (len(password) < 4):
        messagebox.showerror(
            'Error', 'Password must contain\n4 or more characters')
    elif (len(phone) != 10):
        messagebox.showerror('Error', 'Phone no. must contain\n10 characters')
    else:
        root.destroy()
        personalInfoScreen()

# verify fields of personal info screen


def verifyPersonalInfo():
    global gender, height, weight, age
    gender = genderEntry.get().upper()
    height = heightEntry.get()
    weight = weightEntry.get()
    age = ageEntry.get()

    if (gender == "" or height == "" or weight == "" or age == ""):
        messagebox.showerror('Error', 'Fields cannot be left empty')
    elif (gender not in 'fFmM'):
        messagebox.showerror('Error', 'Invalid gender (M/F)')
    elif (int(height) <= 0.0):
        messagebox.showerror(
            'Error', 'Height out of range\nMust be greater than 0.0')
    elif (int(weight) <= 0.0):
        messagebox.showerror(
            'Error', 'Weight out of range\nMust be greater than 0.0')
    elif (int(age) <= 0):
        messagebox.showerror(
            'Error', 'Age out of range\nMust be greater than 0')
    else:
        if register(callPersonalInfoScreen=False) == True:
            root.destroy()
            ('SUCCESS: Registered')


# enter the values in the database
def register(callPersonalInfoScreen):
    try:
        if callPersonalInfoScreen:
            personalInfoScreen()
        query = f"insert into userdata values('{uname}','{password}','{phone}','{gender}','{height}','{weight}','{age}');"
        cursor.execute(query)
        mydb.commit()
        root.destroy()
        loginScreen()
        return True
    except:
        return False


...
# personal info screen


def personalInfoScreen():
    global root
    root = Tk()
    root.resizable(False, False)
    root.eval('tk::PlaceWindow . center')
    root.title("Personal Information")
    root.geometry("300x250")
    ...
    Label(root, width="300", text="Please enter details below",
          bg="orange", fg="white").pack()
    # labels for usergender and PWD
    Label(root, text='Gender').place(x=20, y=40)
    Label(root, text='Height (cm)').place(x=20, y=80)
    Label(root, text='Weight (kg)').place(x=20, y=120)
    Label(root, text='Age (years)').place(x=20, y=160)
    ...
    # input fields
    global genderEntry
    genderEntry = Entry(root)
    genderEntry.place(x=90, y=42)
    genderEntry.focus()

    global heightEntry
    heightEntry = Entry(root)
    heightEntry.place(x=90, y=82)

    global weightEntry
    weightEntry = Entry(root)
    weightEntry.place(x=90, y=122)

    global ageEntry
    ageEntry = Entry(root)
    ageEntry.place(x=90, y=162)
    ...
    Button(root, text="Submit", width=10, height=1, bg="orange",
           command=verifyPersonalInfo).place(x=105, y=200)

# make layout for login screen


def loginScreen():
    cursor.execute("show databases like 'diettracker'")
    if cursor.fetchall()[0] != 'diettracker':
        global root
        root = Tk()
        root.resizable(False, False)
        root.eval('tk::PlaceWindow . center')
        root.title("Login")
        root.geometry("300x250")
        ...
        Label(root, width="300", text="Please enter details below",
              bg="orange", fg="white").pack()
        # labels for username and PWD
        Label(root, text='Username').place(x=20, y=40)
        Label(root, text='Password').place(x=20, y=80)
        ...

        def toggle_password():
            if pwd.cget('show') == '':
                pwd.config(show='*')
                toggle_btn.config(image=closedEye)
            else:
                pwd.config(show='')
                toggle_btn.config(image=openEye)

        closedEye = PhotoImage(file=r"assets/closedEYE.png")
        openEye = PhotoImage(file=r"assets/openEYE.png")
        toggle_btn = Button(root, borderwidth=1, height=15,
                            width=15, image=closedEye, command=toggle_password)
        toggle_btn.place(x=220, y=82)
        ...
        # input fields
        global name
        name = Entry(root)
        name.place(x=90, y=42)
        name.focus()
        # customised input field for PWD
        global pwd
        pwd = Entry(root)
        pwd.config(show='*')
        pwd.place(x=90, y=82)
        ...

        def goToReg():
            root.destroy()
            regScreen()
        Button(root, text="Submit", width=10, height=1,
               bg="orange", command=verifyLogin).place(x=105, y=130)
        Button(root, text="Register", width=10, height=1,
               bg="orange", command=goToReg).place(x=105, y=170)
        ...
        root.mainloop()

# make layout for registration window


def regScreen():
    global root
    root = Tk()
    root.resizable(False, False)
    root.eval('tk::PlaceWindow . center')
    root.title("Register")
    root.geometry("300x250")
    ...
    Label(root, width="300", text="Please enter details below",
          bg="orange", fg="white").pack()
    # labels for username and PWD
    Label(root, text='Username').place(x=20, y=40)
    Label(root, text='Password').place(x=20, y=80)
    Label(root, text='Phone No.').place(x=20, y=120)
    ...

    def toggle_password():
        if pwd.cget('show') == '':
            pwd.config(show='*')
            toggle_btn.config(image=closedEye)
        else:
            pwd.config(show='')
            toggle_btn.config(image=openEye)

    closedEye = PhotoImage(file=r"assets/closedEYE.png")
    openEye = PhotoImage(file=r"assets/openEYE.png")
    toggle_btn = Button(root, borderwidth=1, height=15,
                        width=15, image=closedEye, command=toggle_password)
    toggle_btn.place(x=220, y=82)
    ...
    # input fields
    global name
    name = Entry(root)
    name.place(x=90, y=42)
    name.focus()
    # customised input field for PWD
    global pwd
    pwd = Entry(root)
    pwd.config(show='*')
    pwd.place(x=90, y=82)
    # phone num entry
    global pnum
    pnum = Entry(root)
    pnum.place(x=90, y=122)
    ...

    def goToLogin():
        root.destroy()
        loginScreen()
    Button(root, text="Next", width=10, height=1,
           bg="orange", command=verifyReg).place(x=105, y=160)
    Button(root, text="Login", width=10, height=1,
           bg="orange", command=goToLogin).place(x=105, y=200)
    ...
    root.mainloop()
