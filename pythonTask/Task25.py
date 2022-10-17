# Task 25
#
# Create a class called Utilities
# Create a static method called print_name which accepts a parameter, and prints out the parameter.
# Invoke the static method print_name()


class Utilities:
    def add(num1, num2):
        return num1 + num2


Utilities.add = (Utilities.add)
print("200 + 300 =", Utilities.add(200, 300))

