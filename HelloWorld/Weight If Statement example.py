# get weight info from user.
weight = input("Weight: ")

# get unit of measurement type.
unit = input("(K)g or (L)bs: ")

if unit == "L" or unit == "l":
    print("Weight in Lbs: " + weight)
elif unit == "W" or unit == "w":
    print("Weight in Kg: " + weight)
else:
    print("That's not a valid choice. Try again")