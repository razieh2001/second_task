#Razieh kharaghani database HW2 python list and dictionary

users =[]
numbersOfUsers =int(input("Enter the number of users:"))

for x in range(0,numbersOfUsers):
  userName = input("Enter the user name:\n")
  userAge =  input("Enter the age of users:\n")
  users.append({'name':userName,'age' : userAge}) 

nameFinder = input("Enter the name you are looking for:\n")

check = 0
res = None
for sub in users:
    if sub['name'] == nameFinder:
        res = sub 
        check+=1
        print(res['age'])
 
if check == 0 :
 print("The name you entered doesnt exist")

