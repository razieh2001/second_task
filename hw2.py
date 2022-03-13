#Razieh kharaghani database HW2 python list and dictionary

users =[]
numbersOfUsers =int(input("Enter the number of users:"))

for x in range(0,numbersOfUsers):
  userName = input("Enter the user name:\n")
  userAge =  input("Enter the age of users:\n")
  users.append({'name':userName,'age' : userAge}) 

nameFinder = input("Enter the name you are looking for:\n")

check = False
for sub in users:
    if sub['name'] == nameFinder:
        check=True
        print(sub['age'])
 
if check == False :
 print("The name you entered doesnt exist")

