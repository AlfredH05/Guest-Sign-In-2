from components.menuText import menuTextClass
from components.addCar import addCarComponent
from components.addUser import addUserComponent


menu = True

def menu():
  menuTextClass.menuText()
  t = int(input("Enter Your Selection: "))
  if t == 1:
    addUserComponent.newUser()
  if t == 2:
    addCarComponent.newCar()
  if t == 3:
    quit()

while True:
  menu()