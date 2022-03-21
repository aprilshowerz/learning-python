# tuples are used when you want to make sure they are not accidentally changed.
# tuples are unchangeable. They are enclosed in parenthesis. Arrays are enclosed in brackets.

numbers = (1, 2, 3, 3)
# this tries to change the item in the first position 1 to a 10. Gives error becase you can't change a tuple.
# numbers[0] = 10

# counts how many occurences of 3 in the sequence.
numbers.count(3)

# shows the first occurence of 3 in the sequence.
numbers.index(3)

