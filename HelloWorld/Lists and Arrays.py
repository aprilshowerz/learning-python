# Arrays start with 0 as the first position.

# prints name in the 4th position.
names = ["John", "Bob", "Mosh", "Sam", "April"]
print(names[4])

# prints the first 4 names. Positions 0, 1, 2, 3.
print(names[0:4])

# no counting, just prints for how many items there are. Easier way
numbers = [1, 2, 3, 4, 5]
for item in numbers:
    print(item)


# while i is less than the length of numbers print. Harder way.
i = 0
while i < len(numbers):
    print(numbers[i])
    i = i + 1

