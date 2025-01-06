# Parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating.")

# Child class
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Inherit properties from the parent class
        self.breed = breed

    def bark(self):
        print(f"{self.name} is barking. It's a {self.breed}!")

# Example usage
dog = Dog("Buddy", "Golden Retriever")
dog.eat()  # Method from the parent class
dog.bark()  # Method from the child class