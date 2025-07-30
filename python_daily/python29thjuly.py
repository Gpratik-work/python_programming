# Day 3:

# Check if a number is even or odd
# num=int(input("Enter your number:\n"))
# if num %2==0:
#     print("number is even")
# else:
#     print("number is odd")

# Find the largest of three numbers
# a=[100,200,300,120,320,321]
# a.sort()
# print(a[-3:])

# a=int(input("Enter your first number:\n"))
# b=int(input("Enter your scond number:\n"))
# c=int(input("Enter your third number:\n"))    

# def find_largest(a,b,c):
#     if a>=b and a>=c:
#         return a
#     elif b>=a and b>=c:
#         return b
#     else:
#         return c

# Simple Calculator
num1=int(input("Enter your first number:\n"))
num2=int(input("Enter your socnd number:\n"))
def calculator(num1,num2):
    operation=input("Enter your operation:(+,-,/,*):\n")
    if operation=="+":
        return num1+num2
    elif operation=="-":
        return num1-num2
    elif operation =="*":
        return num1*num2
    elif operation=="/":
        return num1/num2
    else:
        print("Invalid Operation")
print(calculator(num1,num2))