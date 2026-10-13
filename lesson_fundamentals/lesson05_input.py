# USER INPUT IN PYTHON
#print("<PROMPT>")
print()

name = input("Enter your name: ")
print(f"Hello {name}")

print(type(name))

age = input("Enter your age: ")
print(f"Your age is {age}")

print(type(age))

age_converted = int(age)
print(type(age_converted))

height = float(input("Enter your height: "))
print(f"You are {height} meters tall")
print(height + 1)

# Challenge 1: Favorite Color
# Ask the user for their favorite color and print out a message using it.

favorite_color = input("Enter your favorite color: ")
print(f"Your favorite color is {favorite_color}")

# Challenge 2: Adding Two Numbers
# Ask the user for two numbers, add them together, and print the result.

number1 = input("Enter a number: ")
number2 = input("Enter another number: ")
number1_converted = int(number1)
number2_converted = int(number2)
sum = number1_converted + number2_converted
print(f"The sum of the two numbers is {sum}")

# Challenge 3: Circle Area from User Input
# Ask the user for the diameter of a circle, then calculate and print the area.
# pi radius squared 

diameter = input("Enter a diameter: ")
diameter_converted = int(diameter)
radius = diameter_converted / 2
pi = 3.14
area = (radius * pi) ** 2
print(f"The area is {area}")


# Challenge 4: Custom Die Roll
# Ask the user to enter how many sides the die should have.
# Then simulate rolling the die once and print the result.
import random

custom_die_roll = input("Enter an amout of sides for a die: ")
custom_die_roll_int = int(custom_die_roll)
print(f"The die lands on", random.randint(1,custom_die_roll_int))