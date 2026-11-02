#Write a program to create two classes for two different countries 
#that consist of three methods to display the following information of
# respective country - capital, language and type of country. 
# Then, use Polymorphism to create a common interface for both classes.

class India:
    def __init__(self, capital, language, type_of_country):
        self.capital = capital
        self.language = language
        self.type_of_country = type_of_country
    def capital(self):
        print(f"The capital of India is {self.capital}")
    def language(self):
        print(f"The official languages of India are {self.language}")
    def type_of_country(self):
        print(f"India is a {self.type_of_country}")

class Canada:
    def __init__(self, capital, language, type_of_country):
        self.capital = capital
        self.language = language
        self.type_of_country = type_of_country
    def capital(self):
        print(f"The capital of Canada is {self.capital}")
    def language(self):
        print(f"The official languages of Canada are {self.language}")
    def type_of_country(self):
        print(f"Canada is a {self.type_of_country}")

