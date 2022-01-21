class India:
    def capital(self):
        print("New Delhi is the capital of India")

    def language(self):
        print("English, Tamil, Marathi, Telugu, Kannada, Malayalam")

class USA:
        def capital(self):
            print("Washington, D.C is the capital of USA")

        def language(self):
            print("English")

        def display(self):
            print("Welcome to India")

ind = India()
usa = USA()

for country in (ind,usa):
    country.capital()
    country.language()
    country.display()
