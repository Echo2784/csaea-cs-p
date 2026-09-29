bill = 50
tip = bill * 0.2
total = bill + tip
print(f"Tip: ${tip}")
print(f"Total: ${total}")


import math
 
students = 23
slices_per_student = 2
slices_per_pizza = 8
student_slices = students * slices_per_student 
total_pizzas = student_slices / slices_per_pizza 
total_slices = slices_per_pizza * (math.ceil(total_pizzas))
extra_slices = total_slices - student_slices
print(f"Order {(math.ceil(total_pizzas))} pizzas")
print(f"Extra slices: {extra_slices}")


fahrenheit = 212
# C = (F - 32) * 5 / 9
celcius = ((fahrenheit) - 32) * 5 / 9
print(f"{fahrenheit} F is {celcius} C")

score = 84
# 90+ is A, 80+ is B, 70+ is C, 60+ is D, anything lower is F

if (score) >= 90:
    print("A")
elif (score) >= 80:
    print("B")
elif (score) >= 70:
    print("C")
elif (score) >= 60:
    print("D")
else:
    print("F")

password = "csaea2026"
attempt = "CSAEA2026"
 
if attempt == password:
    print("Access granted")
else:
    print("Access denied")

height = 48
age = 8
has_adult = True

if height >= 48 and age >= 10:
    print("You may ride!")
elif height < 48:
    print("You may not ride.")
elif age <= 10 and has_adult == True:
    print("You may ride!")
else:
    print("You may not ride.")

first = "Ada"
last = "Lovelace"
school = "CSAEA"
 
print(f"Hello, my name is {first + last} from {school}") 

cart = [12, 5, 30, 8]
total = 0
for c in cart:
    total += c
print(f"Items: {(len(cart))}")
print(f"Total: ${total}")

start = 10
for i in range (start, 0, -1):
    print(i) 
print("\nLiftoff!")

number = 7
times_table = []
for r in range (1 , 11):
    times_table = number * r
    print(f"7 x {r} = {times_table}")
