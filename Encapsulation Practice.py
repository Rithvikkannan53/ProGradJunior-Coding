class Employee:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def display(self):
        print("The Employee Details:")
        print("Name:",self.name)
        print("Age:",self.age)

emp = Employee("Joe",28)
emp.display()
print(emp.name)

