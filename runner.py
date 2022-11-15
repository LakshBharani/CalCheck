# run code from here -->
import mysql.connector
# mysql database connector
mydb = mysql.connector.connect(
  host="localhost",
  user="laksh",
  password="root",
)
cursor = mydb.cursor(buffered=True)
# make sure data base and tables are created
try:
    cursor.execute("create database diettracker")
    cursor.execute("use diettracker")
except:
    cursor.execute("use diettracker")
try:
    cursor.execute("create table menudata (Username varchar(255), Date varchar(255), Day varchar(255), Meal varchar(255), \
            Dish varchar(255), Cal varchar(255), Unit varchar(255), Mealtype varchar(255), Altmealtype varchar(255), \
            Preference varchar(255), Quantity varchar(255))")
except:
    print("Menudata exists")
try:
    cursor.execute("create table userdata(Username varchar(255) primary key not null, Password varchar(255) not null, \
            PhoneNo varchar(255) not null, Gender varchar(1) not null, Height integer not null, Weight integer not null, \
            Age integer not null)")
except:
    print("Userdata exists")

# run after checking if table and db exists
import auth.auth_handler as auth_handler
auth_handler.loginScreen()
