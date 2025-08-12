class Person:
    def __init__(self, name, age, country):
        self.name = name
        self.age = age
        self.country = country

    def greet(self):
        print(f'Hello {self.name}!')

p = Person('John', 24, 'United Kingdom')
p.greet()