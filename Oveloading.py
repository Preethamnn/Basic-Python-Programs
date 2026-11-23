# Method Overloading:
# Using the same method name with different numbers of arguments.
# Python does not support true method overloading, so we use default arguments.

class Calculator:

    # Same method can accept 1, 2, or 3 arguments
    def add(self, a, b=0, c=0):
        print("Sum =", a + b + c)


# Create object
obj = Calculator()

# Call with one argument
obj.add(10)

# Call with two arguments
obj.add(10, 20)

# Call with three arguments
obj.add(10, 20, 30)
