import mysql.connector
import random
import datetime
import time

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root@user",
  database = "cabbooking"
)

mycursor = mydb.cursor()

print("Welcome to swift CabBooking Service :-")
print()

while(True):

    print("Press 1 for login")
    print("Press 2 for SignUP")

    ans = int(input("Enter : "))

    if(ans == 1):
        while(True):
            name = input("Enter your full name (space seperated): ")
            phone = int(input("Enter your phone number : "))
            mycursor.execute("SELECT * FROM CUSTOMER")
            myresult = mycursor.fetchall()
            flag = 0
            for i in myresult:
                if((i[1] + " " + i[2] == name) and (i[3] == phone)):
                    customer_id = i[0]
                    wallet = i[5]
                    print("Hello "+name+"!")
                    print("Welcome to the Application !")
                    print()
                    print()
                    while(True):
                        print('''
                        Press 1 to view balance
                        Press 2 to Book a ride 
                        Press 3 to view your past rides
                        Press 4 to add balance
                        Press 5 to Logout''')
                        choice = int(input("Enter your choice : "))
                        if(choice == 1):
                            print("Your balance is : ",wallet)
                        elif(choice == 2):
                            source = input("Enter the source address : ")
                            dest = input("Enter the destination address : ")

                            mycursor.execute("SELECT * FROM DRIVER")

                            drivers = mycursor.fetchall()

                            print()
                            print("Available Drivers :-")

                            sql = "SELECT DRIVER_ID,CONTACT_NO,VEHICLE_NAME,FIRST_NAME,LAST_NAME FROM DRIVER,VEHICLE WHERE DRIVER.VEHICLE_REG_NO = VEHICLE.VEHICLE_REG_NO AND DRIVER.AVAILABILITY = TRUE"
                            mycursor.execute(sql)
                            result = mycursor.fetchall()

                            available_drivers = result
                            count = 0
                            for i in available_drivers:
                                if(count == 5):
                                    break
                                count+=1
                                print()
                                print("Name : ",i[3]+" "+i[4])
                                print("Contact No : ",i[1])
                                print("Car name : ",i[2])

                            print()

                            est_pay = random.uniform(1.0, 100.0)

                            print("Estimated ride payment : Rs.",est_pay)
                            if(est_pay > wallet):
                                print("You don't have sufficient please add balance")
                                continue

                            driver_selected = input("Select the driver (Enter driver full name, space seperated) : ")
                            for i in available_drivers:
                                if(i[3]+" "+i[4] == driver_selected):
                                    selected_driver_id = i[0]
                                    selected_driver_vehicle = i[2]
                            
                            confirm = int(input("Enter 1 to start the ride : "))

                            sql = '''INSERT into RIDE_DETAILS(DRIVER_ID,CUSTOMER_ID,SOURCE_ADDRESS,DESTINATION_ADDRESS,RIDE_START_DATE,RIDE_END_DATE,RIDE_START_TIME,RIDE_END_TIME,COMPLETION_STATUS,PAYMENT_AMOUNT,CUSTOMER_FEEDBACK,DRIVER_FEEDBACK,RATING_BY_CUST,RATING_BY_DRIVER) 
                            values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) '''

                            now = datetime.datetime.now()
                            current_time = now.strftime("%H:%M:%S")

                            val = (selected_driver_id,customer_id,source,dest,datetime.date.today(),None,current_time,None,0,0,None,None,0,0)

                            mycursor.execute(sql,val)

                            print("The ride has started successfully!")

        
                            print()
                            print("Ride ongoing")
                            print()
                            time.sleep(5)
                            
                            print()
                            print("The ride has ended successfully!")
                            
                            sql = "UPDATE DRIVER SET AVAILABILITY = 1 WHERE DRIVER_ID = %s"
                            val = (selected_driver_id,)
                            mycursor.execute(sql,val)
                            mydb.commit()

                            sql = "UPDATE RIDE_DETAILS SET COMPLETION_STATUS = 1 WHERE DRIVER_ID = %s"
                            val = (selected_driver_id,)
                            mycursor.execute(sql,val)
                            mydb.commit()

                            feedback = input("Enter your feedback for ride : ")
                            driver_rating = int(input("Enter rating for driver(1-5) : "))
                            sql = "UPDATE RIDE_DETAILS SET CUSTOMER_FEEDBACK = %s ,RATING_BY_CUST = %s WHERE DRIVER_ID = %s"
                            val = (feedback,driver_rating,selected_driver_id)
                            mycursor.execute(sql,val)
                            mydb.commit()

                            sql = "UPDATE DRIVER SET DRIVER_RATING = %s WHERE DRIVER_ID = %s"
                            val = (driver_rating,selected_driver_id)
                            mycursor.execute(sql,val)
                            mydb.commit()

                            sql = "UPDATE RIDE_DETAILS SET RIDE_END_DATE = %s WHERE DRIVER_ID = %s"
                            val = (datetime.date.today(),selected_driver_id)
                            mycursor.execute(sql,val)
                            mydb.commit()

                            now = datetime.datetime.now()
                            current_time = now.strftime("%H:%M:%S")

                            sql = "UPDATE RIDE_DETAILS SET RIDE_END_TIME = %s WHERE DRIVER_ID = %s"
                            val = (current_time,selected_driver_id)
                            mycursor.execute(sql,val)
                            mydb.commit()
                            

                            print("Payment amount : Rs.",est_pay)

                            sql = "UPDATE RIDE_DETAILS SET PAYMENT_AMOUNT = %s WHERE DRIVER_ID = %s"
                            val = (est_pay,selected_driver_id)
                            mycursor.execute(sql,val)
                            mydb.commit()
                            
                            p = input("Enter 'paynow' to make payment : ")


                            sql = "UPDATE CUSTOMER SET WALLET = WALLET-%s WHERE CUSTOMER_ID = %s"
                            val = (est_pay,customer_id)
                            mycursor.execute(sql,val)
                            mydb.commit()

                            sql = "SELECT WALLET FROM CUSTOMER WHERE CUSTOMER_ID = %s"
                            mycursor.execute(sql,(customer_id,))
                            result = mycursor.fetchone()

                            print("Payment is complete , thank you for using our service!")

                            wallet = result[0]
                            print("Available balance : Rs.",result[0])
                        elif(choice == 3):
                            sql = "SELECT CUSTOMER_ID,SOURCE_ADDRESS,DESTINATION_ADDRESS,RIDE_START_DATE,RIDE_END_DATE,RIDE_START_TIME,RIDE_END_TIME,PAYMENT_AMOUNT FROM RIDE_DETAILS WHERE CUSTOMER_ID = %s"
                            val = (customer_id,)

                            mycursor.execute(sql,val)

                            result = mycursor.fetchall()

                            print("There are ",len(result)," rides you have done:-")
                            print()
                            for i in result:
                                print("Customer Id : ",i[0])
                                print("source : ",i[1])
                                print("Destination : ",i[2])
                                print("Ride start Date : ",i[3])
                                print("Ride End Date : ",i[4])
                                print("Ride start time : ",i[5])
                                print("Ride end time : ",i[6])
                                print("Payment amount : Rs.",i[7])
                                print()
                        elif(choice == 4):
                            balance = float(input("Enter the amount you want to add : "))
                            sql = "UPDATE CUSTOMER SET WALLET = WALLET + %s WHERE CUSTOMER_ID = %s"
                            val = (balance,customer_id)

                            mycursor.execute(sql,val)
                            mydb.commit()
                            print("Balance updated successfully !")

                            sql = "SELECT WALLET FROM CUSTOMER WHERE CUSTOMER_ID = %s"
                            val = (customer_id,)
                            mycursor.execute(sql,val)
                            result = mycursor.fetchone()
                            wallet = result[0]
                            print("New Balance : Rs.",result[0])
                            print()
                        elif(choice == 5):
                            break
                        flag = 1
            if(flag == 0):
                print("Wrong Details!")
                print()
            else:
                break
    elif(ans == 2):
        FirstName = input("Enter first name : ")
        LastName = input("Enter Last name : ")
        Contact = int(input("Enter Contact number : "))
        wallet = float(input("Enter the amount to be kept in wallet : "))
        address = input("Enter address : ")
        EmergencyContact = int(input("Enter Emergency Contact number : "))
        Password = input("Enter your password : ")

        random_float1 = random.uniform(1.0, 100.0)
        random_float2 = random.uniform(1.0, 100.0)

        sql = ''' INSERT INTO CUSTOMER (CUSTOMER_ID,FIRST_NAME,LAST_NAME,CONTACT_NO,CUST_PASSWORD,WALLET,LOCATION_X,LOCATION_Y,CUST_RATING,ADDRESS,EMERGENCY_CONTACT) 
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)''' 
        
        val = (None,FirstName,LastName,Contact,Password,wallet,0,random_float1,random_float2,address,EmergencyContact)

        mycursor.execute(sql,val)

        mydb.commit()

        mycursor.execute("SELECT * FROM CUSTOMER")

        myresult = mycursor.fetchall()

        for i in myresult:
            if(i[1] == FirstName):
                print(i)
    print("Type 1 if you want to exit the Application :-")
    ch = input("Do you wish to exit application : ")
    if(ch == "1"):
        break