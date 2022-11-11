# Write a python program to read four numbers from user and find biggest among them
number1=input("Enter a number:")
number2=input("Enter a number:")
number3=input("Enter a number:")
number4=input("Enter a number:")
print(number1)
print(number2)
print(number3)
print(number4)

if number1>number2 and number1>number3 and  number1>number4:
    print("Number 1 is the biggest number")
elif  number2>number3 and  number2>number4:
    print("Number 2 is the biggest number")
elif  number3>number4:
    print("Number 3 is the biggest number")
else:
    print("Number 4 is the biggest number")


