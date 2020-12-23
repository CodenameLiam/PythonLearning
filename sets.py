# Common
fruits = {"Apples", "Oranges", "Mango"}

# Constructor
fruitsConst = set(("Apples", "Oranges", "Mango"))

print(fruits, fruitsConst)

# Change if value in set
print("Apples" in fruits)

# Add value
fruits.add("Grape")
print(fruits)

# Remove value
fruits.remove("Grape")
print(fruits)

# Clear set
fruitsConst.clear()
print(fruitsConst)

# No duplicates
fruits.add("Apples")
print(fruits)