# Common
fruits = ("Apples", "Oranges", "Grapes")

# Constructor
fruitsConst = tuple(("Apples", "Oranges", "Grapes"))

print(fruits, fruitsConst)

# Get
print(fruits[0])

# Cannot change
try:
    fruits[0] = "Pears"
except TypeError as e:
    print(e)

# Delete entire tuple
del fruitsConst



