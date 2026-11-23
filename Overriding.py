# Method Overriding:
# Child class provides its own implementation
# of a method already defined in the parent class.

# Parent class
class Animal:

    # Parent method
    def sound(self):
        print("Animal makes sound")


# Child class inherits Animal
class Dog(Animal):

    # Child overrides the parent's sound() method
    def sound(self):
        print("Dog barks")


# Create object of child class
d = Dog()

# Calls the overridden method
d.sound()
