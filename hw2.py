#Razieh kharaghani database HW2 python list and dictionary

users ={}

numbersOfUsers =int(input("Enter the number of users:"))

for x in range(0,numbersOfUsers):
  userName = input("Enter the user name:\n")
  userAge =  input("Enter the age of users:\n")
  users.update({userName : userAge})
  

nameFinder = input("Enter the name you are looking for:\n")

for key, value in users.items():
 if key == nameFinder:
   print("The age of this user is:\n",value)
 elif key !=nameFinder:
   print("This name doesnt exist")
