User_name = input("Enter your NAME: ")  #Name of user
User_age = int(input("Enter your AGE: "))  #Age of user

if(User_age>18): #age checking
    print(f"{User_name} is eligible to vote")
else:
    print(f"{User_name} is not eligible to vote")

