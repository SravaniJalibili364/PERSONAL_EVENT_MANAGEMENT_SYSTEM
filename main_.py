import mysql.connector as db
import datetime


datetime_object = datetime.datetime.now()

mydb = db.connect(
   host="localhost",
   user="root",
   db = "EMS"
 )

cur = mydb.cursor()

# Database Creation
#s = "CREATE DATABASE EMS"  
#cur.execute(s)
#cur.close()
#print("Database created!")

# For Event_table creation
#def event_table():
#  mydb = db.connect(
#   host="localhost",
#   user="root",
#   db = "EMS",
# )

#  cur = mydb.cursor()
#  s = ('''CREATE TABLE IF NOT EXISTS event_table(user_name varchar(100) not null,event_id primary key int(20) not null,
#         event_name varchar(100) not null,event_type varchar(100) not null,location varchar(100) not null,date timestamp not null);''')
#  cur.execute(s)  
# cur.close()
# mydb.close()
# print("Table Created!")

#event_table()


# For Showing what the events are there . 
def show_events():
  mydb = db.connect(host = "localhost",user = "root", db = "EMS")
  cur = mydb.cursor()
  cur.execute("select * from event_table")
  for i in cur:
    print(i)
  mydb.commit()

  print("these are events")


# For entering the new event
def create_event():
  print("create event")

  mydb = db.connect(
   host="localhost",
   user="root",
   db = "EMS",
 )

  cur = mydb.cursor()
  print("Enter details fro the event creation")
  user_name = input("Enter Your Name : ")
  event_id = int(input("Enter Event_ID : "))
  event_name = input("Enter Event Name : ")
  event_type = input("Enter which type of Event : ")
  location = input("Location of the Event : ")
  date = input("Time and Date of the Event : ")
  gifts_suggestion()
  gift = input("Enter Gift: ")
  cur.execute("""INSERT INTO event_table (user_name,event_id,event_name,event_type,location,date,Gift)VALUES (%s,%s,%s,%s,%s,%s,%s)""", (user_name,event_id,event_name,event_type,location,date,gift))
  mydb.commit()
  print("Event Created!")


# For updating the event
def update_event():
   mydb = db.connect(
   host="localhost",
   user="root",
   db = "EMS",
    )

   cur = mydb.cursor()
   print("ENTER DETAILS TO UPDATE")
   username = input("Enter updated Username : ")
   event_id = int(input("Enter updated Event_ID : "))
   event_name = input("Enter Updated Event Name : ")
   event_type = input("Enter Updated Event Type : ")
   location = input("Enter Updated Location of the Event : ")
   date = input("Enter Updated of the Event")
   event_id = int(input("Enter Existing Event_ID To Update"))
   
   cur.execute("""UPDATE event_table SET user_name = %s,event_id = %s,event_name = %s ,
              event_type = %s ,location = %s , date = %s WHERE event_id = %s""",(username,event_id,event_name,event_type,location,date,event_id))
   mydb.commit()
   print("Updated Event")


# For deleting the event  
def delete_event():
  mydb = db.connect(
  host="localhost",
  user="root",
  db = "EMS"
    )

  cur = mydb.cursor()
  event_id = int(input("Enter Event_ID to be deleted")) 
  cur.execute("DELETE FROM event_table where event_id = %s",(event_id,))
  mydb.commit()
  print("Event Deleted")
  


# By entering the person we can get events
def search_event_by_person():
    mydb = db.connect(
    host="localhost",
    user="root",
    db = "EMS"
     )

    cur = mydb.cursor()
    user_name = input("Enter Username to know the Events : ")
    cur.execute("select event_name from event_table where user_name = %s",(user_name,))
    for result in cur:
        print(result)
    mydb.commit()
    print("Got the event")

# By entering event type we can the events
def search_event_by_event():
   mydb = db.connect(
   host="localhost",
   user="root",
   db = "EMS",
    )
   
   cur = mydb.cursor()
   event_type = input("Enter Event Type to know the Events of that Event Type")  
   cur.execute("select event_name from event_table where event_type = %s",(event_type,))
   result = cur.fetchone()
   print(result)
   mydb.commit()
   print("This is the event")



# Upcoming events for the next seven days
def upcoming_events():
   mydb = db.connect(
   host="localhost",
   user="root",
   db = "EMS",
    )

   cur = mydb.cursor()
   #date = input()
   cur.execute("select event_name,date from event_table where date >= %s and date <= %s + INTERVAL 7 DAY",(datetime_object,datetime_object))
   for i in cur:
     print(i)
   mydb.commit()

   print("These are the upcoming events")

  
# Gift suggestions for the event to buy or suggest to get

def gifts_suggestion():
    event_type = input("Enter Event Type For Gifts Suggestions : ")
    if (event_type == "marriage"):
      print("Photo Frames,Dinner Sets,Personalized crafts")
    elif(event_type == "college_fest"):
      print("Prize Money")
    elif(event_type == "birthday"):
      print("Watches,Dress,Shoes,Jewerelly")
    elif(event_type == "family_function"):
      print("Home Appliances")
    elif(event_type == "anniversary"):
      print("Flowers,Food")
    elif(event_type == "friend_party"):
      print("Watch,Food,Gadjets")



ch=''
num=0
while ch != 8:
    print("\n")
    print("\t\t\t\t--------------------------------")
    print("\t\t\t\tPERSONAL EVENT MANAGEMENT SYSTEM")
    print("\t\t\t\t--------------------------------")
    print("\n")
    print("\tWelcome To Personal Event Mangement System Choose Your Option For An Event")
    print("\n")
    print("\t \tHere Are The Events For The Next Two dDays")
    cur.execute("select event_name,date from event_table where date >= %s and date <= %s + INTERVAL 2 DAY",(datetime_object,datetime_object))
    for i in cur:
        print("\t\t ",i)
    print("\n")
    print("\t1. SHOW EVENTS")
    print("\t2. CREATE EVENT")
    print("\t3. UPDATE_EVENT")
    print("\t4. DELETE EVENT")
    print("\t5. SEARCH EVENT BY NAME")
    print("\t6. SEARCH EVENT BY EVENT TYPE")
    print("\t7. UPCOMING EVENTS")
    print("\t8. Gifts Suggestion For Your Events")
    print("\t9. Exit")
    print("\tSelect Your Option (1-8) ")
    ch = int(input())

  
    if(ch == 1):
      show_events()
    elif(ch == 2):
      create_event()
    elif(ch == 3):
      update_event()
    elif(ch == 4):
      delete_event()
    elif(ch == 5):
      search_event_by_person()
    elif(ch == 6):
      search_event_by_event()
    elif(ch == 7):
      upcoming_events()
    elif(ch == 8):
      gifts_suggestion()
    elif(ch == 9):
      break
   





                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             