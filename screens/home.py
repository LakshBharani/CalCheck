from tkinter import *
import datetime

def updateMealDetails(day="Not Set",monBg="teal",tueBg="teal",wedBg="teal",thursBg="teal",friBg="teal",satBg="teal",sunBg="teal"):
    global mon,tue,wed,thurs,fri,sat,sun
    global mealDetails
    mon.config(bg=monBg)
    tue.config(bg=tueBg)
    wed.config(bg=wedBg)
    thurs.config(bg=thursBg)
    fri.config(bg=friBg)
    sat.config(bg=satBg)
    sun.config(bg=sunBg)

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
    root.title("Home")
    root.geometry("600x600")
    ...
    Button(root, borderwidth=1, height=1,width=9,text="More",bg="teal",fg="white",command='toggle_password').grid(row=0,column=0,sticky= W+E+N+S)
    Button(root, borderwidth=1, height=1,width=9,text="My Profile",bg="teal",fg="white",command='toggle_password').grid(row=0,column=3,sticky= W+E+N+S)
    Label(root,width=65,height=1, text=f"Welcome Back {uname}", bg="orange",fg="white").grid(row=0,column=1,sticky= W+E+N+S)
    ...
    global mealDetails
    mealDetails = Text(root, height = 20,width = 40,bg = "white")
    mealDetails.place(x=150,y=50)
    ...
    global mon,tue,wed,thurs,fri,sat,sun
    mon = Button(root, borderwidth=1, height=2,width=5,text="Mon",bg="teal",fg="white",command=lambda: updateMealDetails(monBg="red",day="Monday"))
    mon.place(x=155,y=400)
    tue = Button(root, borderwidth=1, height=2,width=5,text="Tue",bg="teal",fg="white",command=lambda: updateMealDetails(tueBg="red",day="Tuesday"))
    tue.place(x=200,y=400)
    wed = Button(root, borderwidth=1, height=2,width=5,text="Wed",bg="teal",fg="white",command=lambda: updateMealDetails(wedBg="red",day="Wednesday"))
    wed.place(x=245,y=400)
    thurs = Button(root, borderwidth=1, height=2,width=5,text="Thurs",bg="teal",fg="white",command=lambda: updateMealDetails(thursBg="red",day="Thursday"))
    thurs.place(x=290,y=400)
    fri = Button(root, borderwidth=1, height=2,width=5,text="Fri",bg="teal",fg="white",command=lambda: updateMealDetails(friBg="red",day="Friday"))
    fri.place(x=335,y=400)
    sat = Button(root, borderwidth=1, height=2,width=5,text="Sat",bg="teal",fg="white",command=lambda: updateMealDetails(satBg="red",day="Saturday"))
    sat.place(x=380,y=400)
    sun = Button(root, borderwidth=1, height=2,width=5,text="Sun",bg="teal",fg="white",command=lambda: updateMealDetails(sunBg="red",day="Sunday"))
    sun.place(x=425,y=400)
    ...
    if datetime.datetime.today().weekday() == 0:
        updateMealDetails(monBg="red",day="Monday")
    elif datetime.datetime.today().weekday() == 1:
        updateMealDetails(tueBg="red",day="Tuesday")
    elif datetime.datetime.today().weekday() == 2:
        updateMealDetails(wedBg="red",day="Wednesday")
    elif datetime.datetime.today().weekday() == 3:
        updateMealDetails(thursBg="red",day="Thursday")
    elif datetime.datetime.today().weekday() == 4:
        updateMealDetails(friBg="red",day="Friday")
    elif datetime.datetime.today().weekday() == 5:
        updateMealDetails(satBg="red",day="Saturday")
    elif datetime.datetime.today().weekday() == 6:
        updateMealDetails(sunBg="red",day="Sunday")

    ...
    root.mainloop()

# TODO -> Remove after design done
createHomePage()