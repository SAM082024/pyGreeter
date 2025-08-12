class Person:
    def __init__(self, name, age, country):
        self.name = name
        self.age = age
        self.country = country

    def greet(self):
        print(f'Hello {self.name}!')

    def intro(self):
        print(f'You are {self.age} years old, and live in {self.country}!')
p = Person('John', 24, 'United Kingdom')
p.greet()
p.intro()