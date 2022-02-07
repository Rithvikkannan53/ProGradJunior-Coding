class Parent:
    def __init__(self,text):
        self.message = text

    def printmessage(self):
            print(self.message)

class Child(Parent):
    def __init__(self,text):
        super().__init__(text)

x = Child("Hello, and welcome")
x.printmessage()
