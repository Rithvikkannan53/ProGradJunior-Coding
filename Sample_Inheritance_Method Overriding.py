class Parent:
    def __init__(self,):
        self.value = "This is the Parent Class"

    def show(self):
        print(self.value)

def Child(Parent):
    def __init__(self):
        self.value = "This is the Child Class"

    def show(self):
        print(self.value)

c = Child()
p = Parent()

c.show()
p.show()
