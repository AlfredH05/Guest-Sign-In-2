class addCarComponent():
  
  def newCar():
    
    name = input("Enter Name: ")
    registration = input("Enter Car Registration: ")

    user = ("" + "CAR |" + str(name) + "," + str(registration) + "\n")

    file = open("database.csv", "a")
    file.write(user)
    file.close()

    print("Car Added Successfully!")