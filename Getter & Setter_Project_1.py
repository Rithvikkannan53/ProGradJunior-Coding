class Student:
    def __init__(self,name,age):
        self.name = name
        self.__age = age

    #getter method
    def get_age(self):
        return self.__age

    #setter method
    def set_age(self,age):
        self.__age = age

stud = Student("Rithvik",14)

#retrieving the getter method
print("Name : ",stud.name,stud.get_age())

#retrieving the setter method
stud.set_age(24)
print("Name : ",stud.name,stud.get_age())
