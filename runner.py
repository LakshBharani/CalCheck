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
    cursor.execute("create table menudata (username varchar(255), date varchar(255), day varchar(255), meal varchar(255), dish varchar(255), cal varchar(255), unit varchar(255), mealtype varchar(255), altmealtype varchar(255), preference varchar(255), quantity varchar(255))")
except:
    print("Menudata exists")
try:
    cursor.execute("create table userdata(username varchar(255) primary key not null, password varchar(255) not null, phoneNo varchar(255) not null, gender varchar(1) not null, height integer not null, weight integer not null, age integer not null)")
except:
    print("Userdata exists")

# run after checking if table and db exists
import auth.auth_handler as auth_handler
auth_handler.loginScreen()
