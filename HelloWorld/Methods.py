#Showing how methods work.

#upper method prints variable as uppercase letters.doesn't change variable.
course = "Python for Beginners"
print(course.upper())
#lower method prints variable as lowercase letters. doesn't change variable.
print(course.lower())

#find returns first index (12345678.....) of "n" in variable. first n is in 5th place so 5 is returned.
print(course.find("n"))

#replace method: (replace for with 4.)
print(course.replace("for", "4"))

# searches in variable course's string for Python and returns a boolean value true or false.
print("Python" in course)


