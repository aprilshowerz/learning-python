# how to use and create dictionaries.

customer = {
    "name": "John Smith",
    "age": 30,
    "is_verified": True
}

# prints value stored in key "name"
print(customer["name"])

# or if you use this method, it returns a value of none if the key doesn't exist instead of an error.
print(customer.get("name"))

# attempts to get key "birthdate" which does not exist, so it returns the second value by default.
print(customer.get("birthdate", "Jan 1 1980"))

# update key value for "name" to Jack Smith.
customer["name"] = "Jack Smith"
print(customer.get("name"))

# add a key and value to dictionary
customer["birthdate"] = "Dec 18, 1977"

# return new key that was just added.
print(customer.get("birthdate"))

