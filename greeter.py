class Person:
    def __init__(self, name, age, country):
        self.name = name
        self.age = age
        self.country = country

    def greet(self):
        print(f'Hello {self.name}!')

    def intro(self):
        print(f'You are {self.age} years old, and live in {self.country}!')

# creates a new instance of person (class) with the parameters name, age and country
p = Person('John', 24, 'United Kingdom')

# calls the greet function from the person instance
p.greet()

# calls the intro function from the person instance
p.intro()