# 6. Create a global variable and modify it inside a function using the global keyword. Print the value before and after calling the function.

count = 0


def change_value():
    global count
    count = 1


print("Before calling function:", count)
change_value()
print("After calling function:", count)

# Standard way

counter = 0


def update_counter():
    global counter
    counter += 1  # modifying global variable


print("Before function call:", counter)
update_counter()
print("After function call:", counter)
