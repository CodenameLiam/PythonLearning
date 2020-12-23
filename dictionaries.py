# Common
person = {
    "firstName" : "Liam",
    "lastName" : "Percy",
    "age" : 21
}

# Constructor
person2 = dict(firstName="Jane", lastName="Dane", age=34)

print(person, type(person), person2, type(person2))

# Get
print(person["firstName"])
print(person.get("lastName"))

# Add key-value
person["phone"] = "0412345678"
print(person)

# Get keys
print(person.keys())

# Get values
print(person.values())

# Get items
print(person.items())

# Copy dictionary
person3 = person.copy()
print(person3)

person3["city"] = "Brisbane"
print(person, person3)

# Reference dictionary
person4 = person
person4["gender"] = "Male"
print(person, person4)

# Remove item
del(person["age"])
person.pop("phone")
print(person)

# Length
print(len(person))

# Clear
person.clear()
print(person)

# Array of dictionaries
people = [
    person2,
    person3
]

print(people, type(people))

# Get
print(people[0]["firstName"])