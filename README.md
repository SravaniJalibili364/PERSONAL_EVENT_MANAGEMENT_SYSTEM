# PERSONAL_EVENT_MANAGEMENT_SYSTEM
 
 
 
# Description about the project
    Personal Event Management System it will help for you track your your family's and friend's marriages ,birthday parties , anniversaries . So that you can't miss the miss the event.User Interface is a command line bases interface using Python. 
    
    
# Features of the project
    First Notifiesthe upcoming two days events.

1. SHOW EVENTS
2. CREATE EVENTS
3. UPDATE_EVENT
4. DELETE EVENTS
5. SEARCH EVENT BY NAME
6. SEARCH EVENT BY EVENT TYPE
7. UPCOMING EVENTS
8. Gifts Suggestion For Your Events
9. Exit


# Software Requirements for the Project
1. Visual Studio Code 
2. MySql version 8.0.26
3. Python 3.8.10 
    
# Project Execution
    For this project , In the visual studio first we need to import mysql connector from mysql module and also we have to import datetime module.
    A connection with the MySQL server can be established using either the mysql.connector.connect() method.
    
    We need to connect python code to the  database
     import mysql.connector as db
     mydb = db.connect(
     host="localhost",
     user="root",
     db = "EMS"
     )
     cur = mydb.cursor()
     
   After connected to the database , Using given options, we can select the feature of the event ,so that the function called .In that function the particular query executed in the mysql connector.
   
   And finally we can exit from the system.
   
  
   This project will help you for the event planning and it will remindes you for the upcoming events.
   
   
   
