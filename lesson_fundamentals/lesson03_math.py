#KEY CONCEPTS: math operators: +, -, *, /, //, %, **

add = 7 + 2
print("Sum", add)

subtract = 43 - 4
print("Difference:", subtract)

multiply = 7 * 2
print("Product:", multiply)

float_divide = 10 / 3
print("Float division:", float_divide)

integer_divide = 7 // 2
print("Integer division:", integer_divide)

mod = 7 % 2
print("Modulus: ", mod)

exponent = 7 ** 2
print("Exponent", exponent)

# PEMDAS (parentheses, exponents, multiplication/division, addition/subtraction)

result1 = (2 + 3) * 4
print("Result 1:", result1)

result2 = 2 ** 3 * 4
print("Result 2:", result2)

result3 = 5 + 2 ** 3 * (4 - 1)
print("Result 3:", result3)

# Challenge 1: Rectangle Area  
# Calculate the area of a rectangle with a width of 8 and a height of 5.  
# Create separate variables for width, height, and result. Print result. 

width = 8
height = 5
result = width * height
print("Area:", result)

# Challenge 2: Circle Area  
# Use the formula πr² to calculate the area of a circle with radius 7. (Use 3.14 for π.)  

radius = 7
π = 3.14
result = (π * 7) ** 2
print("Area:", result)

# Challenge 3: Shopping Total  
# A book costs $12.99 and a notebook costs $3.50.  
# Calculate the total cost for 3 books and 4 notebooks.  

book = 12.99
notebook = 3.50
total_cost = 3 * book + 4 * notebook
print(f"Book: ${book}  \nNotebook: ${notebook} \nTotal cost: ${total_cost}")

# Challenge 4: Even or Odd  
# Use the modulus operator to check if the number 57 is even or odd. 

number = 57
type = number % 2
if type > 0:
    print("Odd")
else:
    print("Even")