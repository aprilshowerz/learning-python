# program gets 2 numbers from user, adds them together and returns answer to user.

#Get first number from user and assign to variable. alternate way: first_num = float(input("First: "))
first_num = input("First: ")

#Get second number from user and assign to variable. alternate way: second_num = float(input("Second: "))
second_num = input("Second: ")

#declare sum variable and compute sum. altenate way: answer = first_num + second_num
answer = float(first_num) + float(second_num)

#return answer to user.
print("Sum: " + str(answer))

