from function import *

while True:

    print("what do you want to do?")
    print("1 Addition")
    print("1 Subtraction")
    print("1 Multiplication")
    print("1 Division")

    choice = input("Enter Your Choice : ")

    if choice == 'Q' or choice == 'q':
        break

    num1 = float(input("Enter Number 1 : "))
    num2 = float(input("Enter Number 2 : "))

    if choice == '1':
        addition(num1,num2)
    elif choice == '2':
        subtraction(num1,num2)
    elif choice == '3':
        multiplication(num1,num2)
    elif choice == '4':
        division(num1,num2)
    else:
        print("invaid Choice")