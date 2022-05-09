class addUserComponent():
  
  def newUser():
    
    name = input("Enter Name: ")
    email = input("Enter Email: ")
    phone = input("Enter Phone Number: ")
    time_of_arrival = input("Enter Time of Arrival: ")

    user = ("" + "USER |" + str(name) + "," + str(email) + "," + str(phone) + "," + str(time_of_arrival) + "\n")

    file = open("database.csv", "a")
    file.write(user)
    file.close()

    print("User Added Successfully!")