from tkinter import *
import datetime
import csv
import random

def getCSV():
    global dbData
    with open("Food Data.csv", "r") as dbFile:
        dbReader = csv.reader(dbFile)
        dbData = {}
        i = 0
        for line in dbReader:
            if i == 0:
                i+=1
            else:
                dbData.update({line[0]:{"cal":line[1],"unit":line[2],"mealType":line[3],
                                "altMealType":line[4],"v/n":line[5],"dishType":line[6]}})

def createWeekMenu(day="Not Set",monBg="teal",tueBg="teal",wedBg="teal",thursBg="teal",friBg="teal",satBg="teal",sunBg="teal",createNewMenu=False):
    global mon,tue,wed,thurs,fri,sat,sun
    global mealDetails
    mon.config(bg=monBg)
    tue.config(bg=tueBg)
    wed.config(bg=wedBg)
    thurs.config(bg=thursBg)
    fri.config(bg=friBg)
    sat.config(bg=satBg)
    sun.config(bg=sunBg)
    ...
    getCSV()
    meal_menu_final = {}
    calories = 200
    mealTypes = ["breakfast","lunch","snack","dinner"]
    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    cuisineType = "v"
    with open("weekMenu.txt","r") as weekMenuFile:
        prevDate_formatted = ''
        prevDate = weekMenuFile.readline()
        for i in range(16):
            if prevDate[i] != '-' and prevDate[i] != ' ' and prevDate[i] != ":":
                prevDate_formatted += prevDate[i]
        print(prevDate_formatted)
    dateNow = str(datetime.datetime.today())
    dateNow_formatted = ''
    for i in range(16):
        if dateNow[i] != '-' and dateNow[i] != ' ' and dateNow[i] != ":":
            dateNow_formatted += dateNow[i]
    print(dateNow_formatted)
    print(day)
    if ((int(dateNow_formatted) > int(prevDate_formatted) and datetime.datetime.today().weekday() == 0) or prevDate == '0000-00-00 00:00:00'):
        for meal_day in days:
            dayMenu = {}
            for mealType in mealTypes:
                meal_menu_filtered = {}
                key_li = []
                for foodItem in dbData:
                    if int(dbData[foodItem]["cal"]) <= calories and (dbData[foodItem]["mealType"].casefold() == mealType or dbData[foodItem]["altMealType"].casefold() == mealType) and dbData[foodItem]["v/n"] == cuisineType:
                        dbData[foodItem]["qty"] = calories//int(dbData[foodItem]["cal"])
                        meal_menu_filtered.update({foodItem:dbData[foodItem]})
                for key in meal_menu_filtered: key_li.append(key)
                rand_key = random.choice(key_li)
                dayMenu.update({mealType:{rand_key : meal_menu_filtered[rand_key]}})
                meal_menu_final.update({meal_day:dayMenu})
        ...
        if meal_menu_final != {}:
            with open("weekMenu.txt","w") as weekMenuFile:
                weekMenuFile.write(str(datetime.datetime.today())+"\n")
                weekMenuFile.write(str(meal_menu_final))
        print(meal_menu_final)
    ...
    mealDetails.config(state=NORMAL)
    mealDetails.delete(1.0,END)
    mealDetails.insert(END,"{:<10} {:<0}".format("","Welcome To CalCheck\n\n"))
    mealDetails.insert(END,"{:<10} {:<0} {:<0}".format("",f"{day}'s","Diet Plan\n"))
    mealDetails.insert(END,"=============+=============+============\n")
    mealDetails.insert(END,"                Breakfast               \n")
    mealDetails.insert(END,"=============+=============+============\n")
    mealDetails.insert(END,"    Item          Count       Calories  \n")
    mealDetails.insert(END,"=============+=============+============\n")
    mealDetails.insert(END,"     Idli    |      2      |     120    \n")
    mealDetails.insert(END,"=============+=============+============\n\n")
    
    mealDetails.insert(END,"=============+=============+============\n")
    mealDetails.insert(END,"                  Lunch                 \n")
    mealDetails.insert(END,"=============+=============+============\n")
    mealDetails.insert(END,"    Item          Count       Calories  \n")
    mealDetails.insert(END,"=============+=============+============\n")
    mealDetails.insert(END,"   Parantha  |      2      |     536    \n")
    mealDetails.insert(END,"=============+=============+============\n\n")

    mealDetails.insert(END,"=============+=============+============\n")
    mealDetails.insert(END,"                  Snacks                \n")
    mealDetails.insert(END,"=============+=============+============\n")
    mealDetails.insert(END,"    Item          Count       Calories  \n")
    mealDetails.insert(END,"=============+=============+============\n")
    mealDetails.insert(END,"   Smoothie  |      1      |     430    \n")
    mealDetails.insert(END,"=============+=============+============\n\n")

    mealDetails.insert(END,"=============+=============+============\n")
    mealDetails.insert(END,"                  Dinner                \n")
    mealDetails.insert(END,"=============+=============+============\n")
    mealDetails.insert(END,"    Item          Count       Calories  \n")
    mealDetails.insert(END,"=============+=============+============\n")
    mealDetails.insert(END,"     Dosa    |      3      |     300    \n")
    mealDetails.insert(END,"=============+=============+============\n")
    mealDetails.config(state=DISABLED)


...
def createHomePage(uname='JohnDoe'):
    global root
    root = Tk()
    root.resizable(False,False)
    window_height = 600
    window_width = 600

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))

    root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
    ...
    Button(root, borderwidth=1, height=1,width=9,text="More",bg="teal",fg="white",command='toggle_password').grid(row=0,column=0,sticky= W+E+N+S)
    Button(root, borderwidth=1, height=1,width=9,text="Logout",bg="teal",fg="white",command='toggle_password').grid(row=0,column=3,sticky= W+E+N+S)
    Label(root,width=65,height=1, text=f"Welcome Back {uname}", bg="orange",fg="white").grid(row=0,column=1,sticky= W+E+N+S)
    ...
    global mealDetails
    mealDetails = Text(root, height = 20,width = 40,bg = "white",relief=RIDGE,borderwidth=2)
    mealDetails.place(x=150,y=50)
    ...
    global mon,tue,wed,thurs,fri,sat,sun
    mon = Button(root, borderwidth=1, height=2,width=5,text="Mon",bg="teal",fg="white",command=lambda: createWeekMenu(monBg="red",day="Monday"))
    mon.place(x=150,y=400)
    tue = Button(root, borderwidth=1, height=2,width=5,text="Tue",bg="teal",fg="white",command=lambda: createWeekMenu(tueBg="red",day="Tuesday"))
    tue.place(x=197,y=400)
    wed = Button(root, borderwidth=1, height=2,width=5,text="Wed",bg="teal",fg="white",command=lambda: createWeekMenu(wedBg="red",day="Wednesday"))
    wed.place(x=244,y=400)
    thurs = Button(root, borderwidth=1, height=2,width=5,text="Thurs",bg="teal",fg="white",command=lambda: createWeekMenu(thursBg="red",day="Thursday"))
    thurs.place(x=291,y=400)
    fri = Button(root, borderwidth=1, height=2,width=5,text="Fri",bg="teal",fg="white",command=lambda: createWeekMenu(friBg="red",day="Friday"))
    fri.place(x=337,y=400)
    sat = Button(root, borderwidth=1, height=2,width=5,text="Sat",bg="teal",fg="white",command=lambda: createWeekMenu(satBg="red",day="Saturday"))
    sat.place(x=383,y=400)
    sun = Button(root, borderwidth=1, height=2,width=5,text="Sun",bg="teal",fg="white",command=lambda: createWeekMenu(sunBg="red",day="Sunday"))
    sun.place(x=430,y=400)
    ...
    if datetime.datetime.today().weekday() == 0:
        createWeekMenu(monBg="red",day="Monday")
    elif datetime.datetime.today().weekday() == 1:
        createWeekMenu(tueBg="red",day="Tuesday")
    elif datetime.datetime.today().weekday() == 2:
        createWeekMenu(wedBg="red",day="Wednesday")
    elif datetime.datetime.today().weekday() == 3:
        createWeekMenu(thursBg="red",day="Thursday")
    elif datetime.datetime.today().weekday() == 4:
        createWeekMenu(friBg="red",day="Friday")
    elif datetime.datetime.today().weekday() == 5:
        createWeekMenu(satBg="red",day="Saturday")
    elif datetime.datetime.today().weekday() == 6:
        createWeekMenu(sunBg="red",day="Sunday")

    ...
    root.mainloop()

# TODO -> Remove after design done
createHomePage()

            
