import calc
from calc import add,sub,mul,div

# get the value from the user

print("choose the operation to perform 1.addition 2.subtraction 3.multiplication 4.division")

# to choose which operation to perform
print("Enter the operation number:")
operation = int(input())

if (operation == 1):  # addition
    x = int(input("Enter the value of x:"))
    y = int(input("Enter the value of y:"))
    addition_answer = add(x, y)
    print(addition_answer)

elif (operation == 2):  # subtraction
    x = int(input("Enter the value of x"))
    y = int(input("Enter the value of y"))
    subtraction_answer = sub(x, y)
    print(subtraction_answer)

elif (operation == 3):  # multiplication
    x = int(input("Enter the value of x"))
    y = int(input("Enter the value of y"))
    multiplication_answer = mul(x, y)
    print(multiplication_answer)

elif (operation == 4):  # Division
    x = int(input("Enter the value of x"))
    y = int(input("Enter the value of y"))
    division_answer = div(x, y)
    print(division_answer)
   





