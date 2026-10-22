# CONDITIONALS IN PYTHON
# comparison operators: ==, !=, <, >, <=, >=
# logical operators: and, or, not
# control flow: if, elif, else

# Boolean refresher:
# always return either True or False
print(3 == 2) 
print("Hello" == "Hi there")
print(7 != 4)
print(4 > 5)

# if
num = 12
if num == 10: #only runs if condition is true
    print("Your num is equal to 10")
    print(10 + num)

# if else
num = 5
if num <= 12:
    print("Your num is less than or equal to 12")
else:
    print("Your num is greater than 12")

# if elif else
temperature = 32
if temperature > 95:
    print("It's hot!")
elif temperature >= 60:
    print("It's nice")
else:
    print("It's cold")


print()

x = 2
y = 20

if x == y:
    print("x is equal to y")
elif x > y:
    print("x is greater than y")
elif x < y:
    print("x is less than y")
else:
    print("Error")

# Logical operators: and
# Both sides of the 'and' must be true, otherwise it's false.
age = 16
has_permission = True

if age >= 16 and has_permission:
    print("You can drive")
else:
    print("You can't drive")

# Logical operators: 'or' and 'not'

day = "Monday"

if day == "Saturday" or day == "Sunday":
    print("It's the weekend!")
else:
    print("It's the weekday")

print("--- Using 'is' and 'not' --- ")
# 'is not' is the same as !=
if day is not "Monday":
    print("It's not Monday, thankfully")

    
# Challenge 1: Movie Admission
# Ask the user for their age. 
# If under 13, “You can watch PG or G movies.”
# If 13–17, “You can watch PG-13 movies.”
# If 18+, “You can watch any movie.”
# Example output:
# Enter your age: 15
# You can watch PG-13 movies.

age = input("What is your age? ")
age_int = int(age)
if age_int < 13:
    print("You can watch PG or G movies.")
elif age_int >= 13 and age_int < 18:
    print("You can watch PG-13 movies.")
else:
    print("You can watch any movie.")

# Challenge 2: Leap Year
# Rules:
#   - Years divisible by 4 are leap years...
#   - ...unless they're divisible by 100, then they're NOT leap years...
#   - ...unless they're also divisible by 400, then they ARE leap years.
# Example output:
# Enter a year: 1900
# 1900 is not a leap year.
# (Test: 2024 -> leap, 1900 -> not, 2000 -> leap)

year = input("Enter a year: ")
year_int = int(year)
if year_int % 4 == 0:
    print(f"{year_int} is a leap year.")
elif year_int % 100 == 0:
    print(f"{year_int} is not a leap year.")
elif year_int % 100 == 0 or year_int % 400 == 0:
    print(f"{year_int} is not a leap year.")
else:
    print(f"{year_int} is not a leap year.")
