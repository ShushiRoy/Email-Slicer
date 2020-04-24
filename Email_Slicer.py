import psycopg2
import re

    
try:
    #Main connection to the database
    connection = psycopg2.connect(user = "YOUR USERNAME",password = "YOUR PASSWORD",host = "YOUR HOST IP ADDRESS",port = "YOUR PORT NUMBER", database = "YOUR DATABASE NAME")
    cursor = connection.cursor()


    #Checks if user wants to see the list in the table, or if they wish to enter a new email to add to the list
    user= str(input("Please state if you want to enter an email (type 'email') or see the entire list (type 'list'): "))

    #Shows the entire list in the table
    if user=='list':
        cursor.execute("select * from information")
        result = cursor.fetchall()
        for row in result:
            print("Username =", row[0], )
            print("Domain =", row[1], "\n")

    #User enters a new email address to add to the list        
    elif user == 'email':        
        email= str(input("Please enter your email address: "))


        #Check to see if the user input is a valid email address
        if "@" in email:
            username=email.split("@")[0]
            domain=email.split("@")[1]


            #Insert Data into the PostgreSQL Table
            cursor.execute("insert into information values ('" + username + "','" + domain + "')")
            connection.commit()
            print("Data has been stored")

        #If the user input is not a valud email address, show user message saying so
        elif "@" not in email:
            print("Not a valid email")
    else:
        print('Enter a valid input')

        
#Handles for any error that comes from connecting to the database
except (Exception, psycopg2.Error) as error :
    print ("Error while connecting to PostgreSQL", error)


#Closing database connection
finally:    
    if(connection):
        cursor.close()
        connection.close()
    


