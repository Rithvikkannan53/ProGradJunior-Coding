#Program to perform arithmetic operations

#Function for addition
def add(a,b):
    return a+b

#Function for subtraction
def sub(a,b):
    return a-b

#Function for multiplication
def mul(a,b):
    return a*b

#Function for division
def div(a,b):
    return a/b

#Function for modulous
def mod(a,b):
    return a%b

#Factorial function
def fact(n):
    if n==1:
        return n
    else:
        return n*fact(n-1)

num1 = int(input("Enter the 1st number : "))
num2 = int(input("Enter the 2nd number : "))

print("Addition")
print(num1, " + ",num2, " = ",add(num1,num2))

print("Subtraction")
print(num1, " - ",num2, " = ",sub(num1,num2))

print("Multiplication")
print(num1, " * ",num2, " = ",mul(num1,num2))

print("Division")
print(num1, " / ",num2, " = ",div(num1,num2))

print("Modulous")
print(num1, " % ",num2, " = ",mod(num1,num2))

num = int(input("Enter the Number : "))
print("Factorial of the Number: ",fact(num))
