# Function with defaults
def howdy(s = "Default"):
    print(s)

howdy("This is my string")
howdy()

# Return values
def getSum(num1, num2):
    total = num1 + num2
    return total

print(getSum(1, 2))

# Lambda
lamdaSum = lambda num1, num2 : num1 + num2

print(lamdaSum(10, 25))