import math  
f = False
t = True  
nums = [34, 52, 3, 64, 32]

print(7 // 2, 7 % 2, -7 // 2)
print(int(-5.9), math.floor(-5.9))
print("5" * 3, "5" + "5")
print(2 ** 4, math.pow(2, 4))
print(True + True + True)
print(0.1 + 0.2 == 0.3)
print("Zebra" < "apple")
print(not f or t and f)
print(nums[-len(nums)])
for i in range(10, 0, -3):
    print(i)
x = 5
while x < 10:
    x += 2
    print(x)