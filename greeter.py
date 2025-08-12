class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f'Hello {self.name}!')

p = Person('John')
p.greet()