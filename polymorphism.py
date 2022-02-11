class India:
    def language(self):
        print("Hindi")

    def capital(self):
        print("Delhi")

class USA:
    def language(self):
        print("English")

    def capital(self):
        print("New York")

obj_india = India()
obj_usa = USA()

for country in (obj_india, obj_usa):
    country.language()
    country.capital()