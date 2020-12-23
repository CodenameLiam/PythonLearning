# Common
numbers  = [1, 2, 3, 4, 5]

# Constructor
numbersConstructor = list((1, 2, 3, 4, 5))

# Functions
fruits = ["Apples", "Oranges", "Grapes", "Pears"]

# Value
print(fruits[1])

# Length
print(len(fruits))

# Append
fruits.append("Mangos")
print(fruits)

# Remove
# Value
fruits.remove("Grapes")
print(fruits)

# Position
fruits.pop(1)
print(fruits)

# Insert
fruits.insert(2, "Strawberries")
print(fruits)

# Change
fruits[0] = "Blueberries"

# Reverse
fruits.reverse
print(fruits)

# Sort
fruits.sort()
print(fruits)

# Reverse sort
fruits.sort(reverse=True)
print(fruits)

# Length sort
fruits.sort(key=len)
print(fruits)

# Second character sort
fruits.sort(key=lambda sndChar: sndChar[1])
print(fruits)