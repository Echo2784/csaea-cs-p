# Python functions are simply blocks of code that can be reused. 
# To run a function, you *call* the function by writing its name, followed by parenthesis, and any arguments that it needs.

# https://www.w3schools.com/python/python_functions.asp


def say_hi():
    print("Hi")

def say_bye():
    print("Bye")

say_hi() # calling the fuction 
say_bye()
say_hi()
say_hi()
say_bye()

# Functions more commonly RETURN values, not merely print
# We can pass an ARGUMENT into a function's PARAMETER

def express_this(e): # e is called a PARAMETER, which is a placeholder for an ARGUMENT 
    return e

expression = express_this(3 + 2)# the mathmatical expression here is the ARGUMENT, the actual value that will be used by a functions PARAMETER

print(expression)

def greeter(name):
    return f"Hi {name}"

first = greeter("Jojo")
second = greeter("Bizbo")
third = greeter("Hoppy")

print(first, second, third)

def remainder(a,b):
    return a % b

result = remainder(10,9)
print(result)

def is_far(distance):
    if distance >= 100:
        return "That's far"
    if distance < 100 and distance > 20:
        return "That's not too far"
    if distance < 20:
        return "Hey that's pretty close by!"

result = is_far(10)
print(result)

#call is_far() on four different distances, and print the result
one = is_far(120)
two = is_far(63)
three = is_far(2)
four = is_far(1000000)

print(one, two, three, four)

# I want to create a function that takes in a number and doubles it, then adds it to a list.
# The function should also take in a number of times that we should double the number
# Write a function named doubler(num, times) that has TWO parameters: 
# First parameter:  the number i want doubled
# Second paramater: how many times the loop should run 

#Example output:
# doubler(1, 5)
# # result should be [2, 4, 8, 16, 32]

num = 1
times = 5
def doubler(num, times):
    result_list = []
    for i in range(times):
        num *= 2
        result_list.append(num)
    return result_list
output_list = doubler(num, times)
print(output_list)

# For Challenges 1 - 3, first write pseudocode, then solve in code.
 
# Challenge 1. 
# Make a calculator with 4 procedures that accept two arguments each. 
# 1) add any two numbers and print the result
# 2) subtract any two numbers and print the result
# 3) divide any two numbers and print the result
# 4) multiply any two numbers and print the result 

def adder(a, b):
    return(a + b)

sum = adder(5,10)
print(sum)

def subtractor(a, b):
    return(a - b)

difference = subtractor(5,10)
print(difference)

def multiplier(a, b):
    return(a * b)

product = multiplier(5,10)
print(product)

def divider(a, b):
    return(a / b)

quotient = divider(5,10)
print(quotient)

# Challenge 2
# Make a function called average that:
# 1) accepts five numbers
# 2) returns the average
# 3) print the returned value outside the function

def average(a, b, c, d, e):
    return((a + b + c + d + e) / 5)

result = average(5,10,15,20,25)
print(result)

# Challenge 3
# Make a function called is_even that:
# 1) accepts one number
# 2) prints "Even" if the number is even
# 3) prints "Odd" if the number is odd

def number(a):
    return(a)
type_of_number = number(56)
if type_of_number % 2 > 0:
    print("Odd")
else:
    print("Even")

# Challenge 4
# Use the pseudocode below to write code:
# Make a function called "analyze_word" that counts how many vowels and consonants are in a word
# Tools: uses a for loop, IF/THEN statement, "aeiou".

# The function analyze_word accepts one argument, a single word (string):
# Initialize two variables:
# vowelCount set to 0
# consonantCount set to 0
# Use a loop to iterate through each character in the word.
# Inside the loop, use an IF/ELSE statement:
# If the character is a vowel (a, e, i, o, u), increment vowelCount.
# Otherwise, increment consonantCount.
# After the loop ends: 
# 	return a f-string that states how many vowels and how many consonants are in the word.

# Call the function with a sample one-word string and print the returned result outside the function


def analyze_word(letter):
    vowelCount = 0
    consonantCount = 0
    for i in letter:
        if i in "aeiou":
            vowelCount += 1
        elif i in "bcdfghjklmnpqrstvwxyz":
            consonantCount += 1
    return vowelCount, consonantCount

vowelCount, consonantCount = analyze_word("pineapple")
print(f"Vowel Count: {vowelCount}")
print(f"Consonant Count: {consonantCount}")
