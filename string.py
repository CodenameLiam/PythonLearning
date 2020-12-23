# Concat
name = "Liam"
age = 21

# Arguments by position
print("Hello, my name is {name} and I am {age}".format(name=name, age=age))

# F-Strings
print(f"Hello, my name is {name} and I am {age}")

# String methods
s = "and cap this"

# Capitalise
print(s.capitalize())

# Upper
print(s.upper())

# Replace
print(s.replace("cap", "BLAP"))

# Messing around with ternary operators
print(s[1:len(s)] + ((s[0] + "bag") if s[0] in ['a', 'e', 'i', 'o', 'u'] else (s[0] + "ay")))