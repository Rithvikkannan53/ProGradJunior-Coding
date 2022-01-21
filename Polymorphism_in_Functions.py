class Tomato:
    def type(self):
        print("Tomato is a vegetable")

    def color(self):
        print("Tomato is red in color")

class Apple:
    def type(self):
        print("Apple is a fruit")

    def color(self):
        print("Apple is red in color")

def func(obj):
    obj.type()
    obj.color()

tom = Tomato()
app = Apple()
func(tom)
func(app)
