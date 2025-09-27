"""Conditionals, loops, comprehensions examples"""
# conditionals
x = 10
if x > 5:
    print("x>5")
elif x == 5:
    print("x==5")
else:
    print("x<5")

# loops
for i in range(5):
    print(i)

i = 0
while i < 3:
    print("while", i)
    i += 1

# comprehensions
squares = [i*i for i in range(10)]
print('squares:', squares)

# dict comprehension
square_map = {i: i*i for i in range(5)}
print('map:', square_map)
