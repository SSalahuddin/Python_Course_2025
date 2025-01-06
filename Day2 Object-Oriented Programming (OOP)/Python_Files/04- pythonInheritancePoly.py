class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f'Hello, my name is {self.name} and I am {self.age} years old.')

class Employee(Person):
    def __init__(self, name, age, job_title):
        super().__init__(name, age)
        self.job_title = job_title

    def greet(self):
        print(f'Hello, I am {self.name}, a {self.job_title}.')

# Demonstrating polymorphism
person = Person('Ali Ahmad', 30)
employee = Employee('Sajjad Awan', 28, 'Engineer')

for individual in (person, employee):
    individual.greet()