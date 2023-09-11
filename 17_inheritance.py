# Base class (parent class)
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass  # This method is intended to be overridden by subclasses

    def eat(self):
        print(f"{self.name} is eating.")

# Subclass (child class)
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

# Subclass (child class)
class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

# Create instances of the subclasses
dog = Dog("Buddy")
cat = Cat("Whiskers")

# Call methods on instances
print(dog.speak())  # Output: Buddy says Woof!
print(cat.speak())  # Output: Whiskers says Meow!

# Call the inherited method from the base class
dog.eat()  # Output: Buddy is eating.
cat.eat()  # Output: Whiskers is eating.
