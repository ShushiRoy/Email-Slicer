import psycopg2
import re

    
try:
    #Main connection to the database
    connection = psycopg2.connect(user = "postgres",password = "password",host = "127.0.0.1",port = "15432", database = "Email Slicer")
    cursor = connection.cursor()


    #User Input for an email
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

        
#Handles for any error that comes from connecting to the database
except (Exception, psycopg2.Error) as error :
    print ("Error while connecting to PostgreSQL", error)


#Closing database connection
finally:    
    if(connection):
        cursor.close()
        connection.close()
    

