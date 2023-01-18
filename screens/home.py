from tkinter import *
from tkinter import messagebox
import datetime
import csv
import random
import mysql.connector

# mysql database connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="sql123",
)
cursor = mydb.cursor(buffered=True)

# function executed when user chooses to leave app through 1. logout or 2. Exit


def quitHome(leavingMethod):
    if leavingMethod == "logout":
        answer = messagebox.askokcancel(
            "Logout", "You will be required\nto login again.", icon="warning")
        if answer == True:
            root.destroy()
            from auth.auth_handler import loginScreen
            loginScreen()
    elif leavingMethod == "exit":
        answer = messagebox.askokcancel(
            "Exit", "Are you sure you\nwant to exit?")
        if answer == True:
            root.destroy()
            print("...Terminated")

# if user is unhappy with his current menu, it will recreate the entire weeks menu with same calorie count for all 7 days


def refreshMenu():
    answer = messagebox.askokcancel(
        "Reset Menu", "Your current menu will be\ndeleted and a new one will\nbe made.", icon="warning")
    if answer == True:
        cursor.execute(
            f"select distinct date from menudata where username='{username}'")
        dateToBeRemoved = cursor.fetchall()[-1][0]
        cursor.execute(f"delete from menudata where date='{dateToBeRemoved}'")
        # creates new menu and sets day to current day
        if datetime.datetime.today().weekday() == 0:
            createWeekMenu(monBg="red", day="Monday")
        elif datetime.datetime.today().weekday() == 1:
            createWeekMenu(tueBg="red", day="Tuesday")
        elif datetime.datetime.today().weekday() == 2:
            createWeekMenu(wedBg="red", day="Wednesday")
        elif datetime.datetime.today().weekday() == 3:
            createWeekMenu(thursBg="red", day="Thursday")
        elif datetime.datetime.today().weekday() == 4:
            createWeekMenu(friBg="red", day="Friday")
        elif datetime.datetime.today().weekday() == 5:
            createWeekMenu(satBg="red", day="Saturday")
        elif datetime.datetime.today().weekday() == 6:
            createWeekMenu(sunBg="red", day="Sunday")

# get all data from the food database (csv file)


def getCSV():
    global dbData
    with open("Food Data.csv", "r") as dbFile:
        dbReader = csv.reader(dbFile)
        dbData = {}
        i = 0
        for line in dbReader:
            if i == 0:
                i += 1
            else:
                dbData.update({line[0]: {"cal": line[1], "unit": line[2], "mealType": line[3],
                                         "altMealType": line[4], "v/n": line[5]}})

# function to create a menu for all days and change the color of the buttons when clicked


def createWeekMenu(day="Not Set", monBg="teal", tueBg="teal", wedBg="teal", thursBg="teal", friBg="teal", satBg="teal", sunBg="teal"):
    global mon, tue, wed, thurs, fri, sat, sun
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
    # get user info from the sql database to calculate daily calories based on height, weight, age and gender
    meal_menu_final = {}
    cursor.execute(
        f"select weight from userdata where username = '{username}'")
    weight = float(cursor.fetchone()[0])
    cursor.execute(
        f"select height from userdata where username = '{username}'")
    height = float(cursor.fetchone()[0])
    cursor.execute(f"select age from userdata where username = '{username}'")
    age = int(cursor.fetchone()[0])
    cursor.execute(
        f"select gender from userdata where username = '{username}'")
    gender = str(cursor.fetchone()[0])
    if gender.casefold() == "m":
        calories = 66.5+(13.8*weight+5*height/6.8*age)
    else:
        calories = 655+(9.6*weight+1.9*height/4.7*age)
    mealTypes = ["breakfast", "lunch", "snack", "dinner"]
    days = ['Monday', 'Tuesday', 'Wednesday',
            'Thursday', 'Friday', 'Saturday', 'Sunday']
    preference = "v"
    # get previous date
    cursor.execute(
        f"select distinct date from menudata where username='{username}'")
    allDates = cursor.fetchall()  # all the dates in the database for the current user
    prevDate = '00000000000000'
    for date in allDates:
        tempPrevDate = ''
        for i in range(10):
            if date[0][i] != '-' and date[0][i] != ' ' and date[0][i] != ':':
                tempPrevDate += date[0][i]
        if int(prevDate) <= int(tempPrevDate):
            prevDate = tempPrevDate

    # get current date
    dateNow = str(datetime.datetime.today())[:19]
    dateNow_formatted = ''
    for i in range(10):
        if dateNow[i] != '-' and dateNow[i] != ' ' and dateNow[i] != ":":
            dateNow_formatted += dateNow[i]

    if ((int(dateNow_formatted) > int(prevDate) and datetime.datetime.today().weekday() == 0) or prevDate == '00000000000000'):
        # making week menu for the user
        # calorie ratio per meal is set here
        bfastcal = calories*0.30
        lunchCal = calories*0.35
        snackCal = calories*0.10
        dinnerCal = calories*0.25
        for meal_day in days:
            dayMenu = {}
            for mealType in mealTypes:
                meal_menu_filtered = {}
                key_li = []
                for foodItem in dbData:
                    calTBcompared = ""
                    if mealType == "breakfast":
                        calTBcompared = bfastcal
                    elif mealType == "lunch":
                        calTBcompared = lunchCal
                    elif mealType == "snack":
                        calTBcompared = snackCal
                    elif mealType == "dinner":
                        calTBcompared = dinnerCal
                    if int(dbData[foodItem]["cal"]) <= calTBcompared and (dbData[foodItem]["mealType"].casefold() == mealType or dbData[foodItem]["altMealType"].casefold() == mealType) and dbData[foodItem]["v/n"] == preference:
                        dbData[foodItem]["qty"] = round(
                            calTBcompared/int(dbData[foodItem]["cal"]), 0)
                        meal_menu_filtered.update({foodItem: dbData[foodItem]})
                for key in meal_menu_filtered:
                    key_li.append(key)
                allFoodItems_inMenu = []
                for i in meal_menu_final:
                    for j in meal_menu_final[i]:
                        for key in list(meal_menu_final[i][j].keys()):
                            allFoodItems_inMenu.append(key)

                rand_key = random.choice(key_li)
                while rand_key in allFoodItems_inMenu:
                    rand_key = random.choice(key_li)
                dayMenu.update(
                    {mealType: {rand_key: meal_menu_filtered[rand_key]}})
                meal_menu_final.update({meal_day: dayMenu})
        ...
        for dayKey in meal_menu_final:
            for mealKey in list(meal_menu_final[dayKey].keys()):
                foodItemKey = meal_menu_final[dayKey][mealKey][list(
                    meal_menu_final[dayKey][mealKey].keys())[0]]
                query = f"insert into menudata values('{username}','{dateNow}','{dayKey}','{mealKey}','{list(meal_menu_final[dayKey][mealKey].keys())[0]}','{foodItemKey['cal']}','{foodItemKey['unit']}','{foodItemKey['mealType']}','{foodItemKey['altMealType']}','{foodItemKey['v/n']}','{foodItemKey['qty']}');"
                cursor.execute(query)
                mydb.commit()
    ...

    def formatMealDeets(inputTup):
        inputLi = list(inputTup)
        outputTup = []
        for i in range(len(inputLi)):
            elem = inputLi[i]
            lenElem = len(str(elem))
            numSpacesPreceding = int((23-lenElem)/2)
            if i == 0:
                formattedElem = " "*numSpacesPreceding + \
                    str(elem) + " "*(23-lenElem-numSpacesPreceding)
                outputTup.append(formattedElem)

            elif i == 1:
                totalSpaces = 23-(len(elem[:-2]) + len(inputLi[i+1]) + 1)
                leftSpaces = int(round(totalSpaces/2, 0))
                rightSpaces = int(totalSpaces-leftSpaces)
                formattedElem = " " * \
                    (leftSpaces+1) + elem[:-2] + " " + \
                    inputLi[i+1] + " "*(rightSpaces-1)
                i += 1
                outputTup.append(formattedElem)

            elif i == 3:
                formattedElem = " "*numSpacesPreceding + \
                    str(elem) + " "*(23-lenElem-numSpacesPreceding-1)
                outputTup.append(formattedElem)
        return tuple(outputTup)

    cursor.execute(
        f"select dish, quantity, unit, cal from menudata where username='{username}' and day='{day}' and meal='breakfast';")
    breakfastDeets = formatMealDeets(cursor.fetchone())
    cursor.execute(
        f"select dish, quantity, unit, cal from menudata where username='{username}' and day='{day}' and meal='lunch';")
    lunchDeets = formatMealDeets(cursor.fetchone())
    cursor.execute(
        f"select dish, quantity, unit, cal from menudata where username='{username}' and day='{day}' and meal='snack';")
    snackDeets = formatMealDeets(cursor.fetchone())
    cursor.execute(
        f"select dish, quantity, unit, cal from menudata where username='{username}' and day='{day}' and meal='dinner';")
    dinnerDeets = formatMealDeets(cursor.fetchone())
    ...
    mealDetails.config(state=NORMAL)
    mealDetails.delete(1.0, END)
    mealDetails.insert(END, "{:<25} {:<0}".format(
        "", "Welcome To CalCheck\n\n"))
    mealDetails.insert(END, "{:<25} {:<0} {:<0}".format(
        "", f"{day}'s", "Diet Plan\n"))
    mealDetails.insert(
        END, "=======================+=======================+======================\n")
    mealDetails.insert(
        END, "                                Breakfast                             \n")
    mealDetails.insert(
        END, "=======================+=======================+======================\n")
    mealDetails.insert(
        END, "         Item                    Count                  Calories      \n")
    mealDetails.insert(
        END, "=======================+=======================+======================\n")
    mealDetails.insert(
        END, f"{breakfastDeets[0]}|{breakfastDeets[1]}|{breakfastDeets[2]}")
    mealDetails.insert(
        END, "=======================+=======================+======================\n\n")

    mealDetails.insert(
        END, "=======================+=======================+======================\n")
    mealDetails.insert(
        END, "                                Lunch                                 \n")
    mealDetails.insert(
        END, "=======================+=======================+======================\n")
    mealDetails.insert(
        END, "         Item                    Count                  Calories      \n")
    mealDetails.insert(
        END, "=======================+=======================+======================\n")
    mealDetails.insert(END, f"{lunchDeets[0]}|{lunchDeets[1]}|{lunchDeets[2]}")
    mealDetails.insert(
        END, "=======================+=======================+======================\n\n")

    mealDetails.insert(
        END, "=======================+=======================+======================\n")
    mealDetails.insert(
        END, "                                Snacks                                \n")
    mealDetails.insert(
        END, "=======================+=======================+======================\n")
    mealDetails.insert(
        END, "         Item                    Count                  Calories      \n")
    mealDetails.insert(
        END, "=======================+=======================+======================\n")
    mealDetails.insert(END, f"{snackDeets[0]}|{snackDeets[1]}|{snackDeets[2]}")
    mealDetails.insert(
        END, "=======================+=======================+======================\n\n")

    mealDetails.insert(
        END, "=======================+=======================+======================\n")
    mealDetails.insert(
        END, "                                Dinner                                \n")
    mealDetails.insert(
        END, "=======================+=======================+======================\n")
    mealDetails.insert(
        END, "         Item                    Count                  Calories      \n")
    mealDetails.insert(
        END, "=======================+=======================+======================\n")
    mealDetails.insert(
        END, f"{dinnerDeets[0]}|{dinnerDeets[1]}|{dinnerDeets[2]}")
    mealDetails.insert(
        END, "=======================+=======================+======================")
    mealDetails.config(state=DISABLED)


...

# function to create the layout for the home page


def createHomePage(uname='JohnDoe'):
    cursor.execute("use diettracker")
    global root
    global username
    username = uname
    root = Tk()
    root.resizable(False, False)
    window_height = 600
    window_width = 600
    root.title('Home')

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))

    root.geometry("{}x{}+{}+{}".format(window_width,
                  window_height, x_cordinate, y_cordinate))
    ...

    Button(root, borderwidth=1, height=1, width=9, text="Reset Menu", bg="teal",
           fg="white", command=refreshMenu).grid(row=0, column=0, sticky=W+E+N+S)
    Label(root, width=65, height=1, text=f"Welcome Back {uname.title()}", bg="orange", fg="white").grid(
        row=0, column=1, sticky=W+E+N+S)
    Button(root, borderwidth=1, height=1, width=9, text="Logout", bg="teal", fg="white",
           command=lambda: quitHome("logout")).grid(row=0, column=3, sticky=W+E+N+S)
    Button(root, borderwidth=1, height=3, width=17, text="Exit", bg="orange",
           fg="white", command=lambda: quitHome("exit")).place(x=457, y=535)
    ...
    global mealDetails
    mealDetails = Text(root, height=30, width=70,
                       bg="white", relief=RIDGE, borderwidth=2)
    mealDetails.place(x=17.5, y=38)
    ...
    global mon, tue, wed, thurs, fri, sat, sun
    mon = Button(root, borderwidth=1, height=3, width=7, text="Mon", bg="teal",
                 fg="white", command=lambda: createWeekMenu(monBg="red", day="Monday"))
    mon.place(x=17, y=535)
    tue = Button(root, borderwidth=1, height=3, width=7, text="Tue", bg="teal",
                 fg="white", command=lambda: createWeekMenu(tueBg="red", day="Tuesday"))
    tue.place(x=80, y=535)
    wed = Button(root, borderwidth=1, height=3, width=7, text="Wed", bg="teal",
                 fg="white", command=lambda: createWeekMenu(wedBg="red", day="Wednesday"))
    wed.place(x=143, y=535)
    thurs = Button(root, borderwidth=1, height=3, width=7, text="Thurs", bg="teal",
                   fg="white", command=lambda: createWeekMenu(thursBg="red", day="Thursday"))
    thurs.place(x=206, y=535)
    fri = Button(root, borderwidth=1, height=3, width=7, text="Fri", bg="teal",
                 fg="white", command=lambda: createWeekMenu(friBg="red", day="Friday"))
    fri.place(x=269, y=535)
    sat = Button(root, borderwidth=1, height=3, width=7, text="Sat", bg="teal",
                 fg="white", command=lambda: createWeekMenu(satBg="red", day="Saturday"))
    sat.place(x=331, y=535)
    sun = Button(root, borderwidth=1, height=3, width=7, text="Sun", bg="teal",
                 fg="white", command=lambda: createWeekMenu(sunBg="red", day="Sunday"))
    sun.place(x=394, y=535)
    ...
    if datetime.datetime.today().weekday() == 0:
        createWeekMenu(monBg="red", day="Monday")
    elif datetime.datetime.today().weekday() == 1:
        createWeekMenu(tueBg="red", day="Tuesday")
    elif datetime.datetime.today().weekday() == 2:
        createWeekMenu(wedBg="red", day="Wednesday")
    elif datetime.datetime.today().weekday() == 3:
        createWeekMenu(thursBg="red", day="Thursday")
    elif datetime.datetime.today().weekday() == 4:
        createWeekMenu(friBg="red", day="Friday")
    elif datetime.datetime.today().weekday() == 5:
        createWeekMenu(satBg="red", day="Saturday")
    elif datetime.datetime.today().weekday() == 6:
        createWeekMenu(sunBg="red", day="Sunday")

    ...
    root.mainloop()
