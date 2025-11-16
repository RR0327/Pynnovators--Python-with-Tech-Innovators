# 2. Create variables of different datatypes (string, int, float, bool, list) and print each value with its datatype using type().

name = "Python"
age = 18
height = 5.9
is_student = True
colors = ["red", "blue", "green"]

print(name, type(name))
print(age, type(age))
print(height, type(height))
print(is_student, type(is_student))
print(colors, type(colors))

# Short way

text = "Python"
num = 10
price = 19.99
flag = True
items = [1, 2, 3]

for value in (text, num, price, flag, items):
    print(value, type(value))
