
# if you use one value, it returns values from 0 to 4. (since it starts at 0)
numbers = range(5)
for number in numbers:
    print(number)

# alternative way if you don't need to declare a separate variable. returns 0,1,2,3,4
for number in range(5):
    print(number)

# just a spacer to separate the loops.
print("space")


# if you use 2 values, it goes from the starting value to ending position. Starts at 5 and goes until the 10th spot which is 9 since the first position is 0. (5,6,7,8,9)
numbers = range(5, 10)
for number in numbers:
    print(number)

# just a spacer to separate the loops.
print("space")

# if you use 3 values, the first is the starting value, it goes until the 2nd value's position and steps using the 3rd value. (counts by 2's in this case) 5,7,9
numbers = range(5, 10, 2)
for number in numbers:
    print(number)


