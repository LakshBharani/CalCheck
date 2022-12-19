from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import auth.auth_handler as auth_handler


def createWelcomePage():
    global root
    root = Tk()
    root.resizable(False, False)
    window_height = 600
    window_width = 600
    root.title('Welcome')
    root.configure(background='white')

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))

    root.geometry("{}x{}+{}+{}".format(window_width,
                  window_height, x_cordinate, y_cordinate))
    ...
    Label(root, text="Welcome To", fg="green",
          font=("", 30), background="white").place(x=202, y=37)
    image = Image.open("assets/logo.jpg")
    logo_resized = image.resize((120, 120))
    logo = ImageTk.PhotoImage(logo_resized)
    Label(root, text="CalCheck", fg="green",
          font=("", 30), background="white").place(x=225, y=230)
    Label(root, image=logo, borderwidth=0).place(x=250, y=97)
    Label(root, text="Tracking calories and macro-nutrients helps in understanding the eating patterns and habits of an individual, making it easier to monitor diet behaviors. It is also an incredibly helpful way to keep track of your fitness and nutrition goals to achieve your intended physique.\n\nWe at CalCheck help you keep track of your daily meals without compromising on your calorie requirement.",
          font=("", 15), wraplengt=540, background="white").place(x=30, y=300)
    ...
    Button(root, borderwidth=1, height=3, width=72, text="LETS GO", bg="orange",
           fg="black", font=("", 10), command=gotoNextPage).place(x=7, y=530)
    ...
    root.mainloop()


def gotoNextPage():
    root.destroy()
    auth_handler.loginScreen()
