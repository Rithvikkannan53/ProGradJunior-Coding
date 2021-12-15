class Calculator:
    def add(self,a,b):
        return a+b

    def subtract(self,a,b):
        return a-b

    def multiply(self,a,b):
        return a*b

    def divide(self,a,b):
        return a/b

mycalcus = Calculator()

while True:

    print("1:Add")
    print("2:Subtraction")
    print("3:Multiplication")
    print("4:Division")
    print("5:Exit")

    choice = int(input("Select the number :"))

    if choice in (1,2,3,4,5):
        if(choice == 5):
            break

        a = int(input("Enter the 1st number:"))
        b = int(input("Enter the 2nd number:"))
        if(choice == 1):
            print("The answer is :",mycalcus.add(a,b))

        elif(choice == 2):
            print("The answer is :",mycalcus.subtract(a,b))

        elif(choice == 3):
            print("The answer is :",mycalcus.multiply(a,b))

        elif(choice == 4):
            print("The answer is :",mycalcus.divide(a,b))

        else:
            print("Invalid Input")
            

            
            
            
