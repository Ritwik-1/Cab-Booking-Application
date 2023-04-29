import mysql.connector
import random
from datetime import datetime
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root@user",
  database = "cabbooking"
)

mycursor = mydb.cursor()

print("Welcome Driver :-")
print()

while(True):

    print("Press 1 for login")
    print("Press 2 for SignUP")

    ans = int(input("Enter : "))

    if(ans == 1):
        while(True):
            name = input("Enter your full name : ")
            phone = int(input("Enter your phone number : "))
            mycursor.execute("SELECT * FROM DRIVER")
            myresult = mycursor.fetchall()
            flag = 0
            for i in myresult:
                if((i[2] + " " + i[3] == name) and (i[5] == phone)):
                    print("Hello "+name+"!")
                    print("Welcome to the Application !")
                    print()
                    print()

                    print("")

                    flag = 1
                    break
            if(flag == 0):
                print("Wrong Details!")
                print()
                print("Press 1 to go back:-")

                ch = input("Your choice : ")
                if(ch == "1"):
                    break
            else:
                break
    elif(ans == 2):
        FirstName = input("Enter first name : ")
        LastName = input("Enter Last name : ")
        Contact = int(input("Enter Contact number : "))
        Gender = input("Gender : ")
        L_no = input("Enter your License No. : ")
        address = input("Enter address : ")
        Password = input("Enter your password : ")

        random_float1 = random.uniform(1.0, 100.0)
        random_float2 = random.uniform(1.0, 100.0)
        sql = ''' INSERT INTO DRIVER(DRIVER_ID,VEHICLE_REG_NO,FIRST_NAME,LAST_NAME,GENDER,CONTACT_NO,DRIVER_PASSWORD,DRIVER_RATING,AVAILABILITY,LICENSE_NO,TRIP_COUNT,LOCATION_X,LOCATION_Y,ADDRESS) 
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)''' 
        
        val = (None,None,FirstName,LastName,Gender,Contact,Password,0,1,L_no,0,random_float1,random_float2,address)

        mycursor.execute(sql,val)

        mydb.commit()

        print("You have succesfully registered !")

        print("Please Register your vehicle now :-")
        print()
        V_reg = input("Enter your vehicle's reg. no : ")
        V_name = input("Enter vehicle name : ")
        AC = bool(input("Enter True for AC , False for Non-AC : "))
        Electric = bool(input("Enter True if electric vehicle , False otherwise : "))
        Fuel_Type = bool(input("Enter True for Petrol, False otherwise"))
        Pollution_cert = input("Enter pollution certificate no. : ")
        Vehicle_type = input("Enter your vehicle type(Hatchback/sedan/SUV) : ")
        Luggage_carrier = bool(input("Enter True if vehicle has luggage carrier , else False : "))
        Boot_space = int(input("Enter boot space of car : "))
        seating_capacity = int(input("Enter seating capacity of car : "))

        sql = ''' INSERT INTO VEHICLE(VEHICLE_REG_NO,VEHICLE_NAME,AC,ELECTRIC_VEHICLE,FUEL_TYPE,POLLUTION_CERT_NO,VEHICLE_TYPE,LUGGAGE_CARRIER,BOOT_SPACE,SEATING_CAP) 
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)''' 
        
        val = (V_reg,V_name,AC,Electric,Fuel_Type,Pollution_cert,Vehicle_type,Luggage_carrier,Boot_space,seating_capacity)

        mycursor.execute(sql,val)

        mydb.commit()

        mycursor.execute(f"UPDATE DRIVER SET VEHICLE_REG_NO = '65' WHERE FIRST_NAME = 'Kotlin' ")

        mycursor.execute("SELECT * FROM DRIVER")

        myresult = mycursor.fetchall()

        for i in myresult:
            if(i[1] == FirstName):
                print(i)
        
    print("Type 1 if you want to exit the Application :-")
    ch = input("Do you wish to exit application : ")
    if(ch == "1"):
        break

# create a signup in this and then wallet mai money add karna : transac
# find 4 transactions and implement directly 

