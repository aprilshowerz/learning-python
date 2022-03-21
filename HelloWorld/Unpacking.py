coordinates = (1, 2, 3)

# long way
# x = coordinates[0]
# y = coordinates[1]
# z = coordinates[2]
# z = x + y
# print(z)

# unpacking pulls the values from each position in the tuple above in line 1 and transfers it to the relative variables below.
x, y, z = coordinates
z = x + y
print(z)
