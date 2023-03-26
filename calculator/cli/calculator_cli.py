# its just a calculator program 

# a function for add two number
def add(x, y):
    return x + y

# a function for subtract two number
def subtract(x, y):
    return x - y

# a function for multiply two number
def multiply(x, y):
    return x * y

# a function for divide two number
def divide(x, y):
    return x / y

# a function for power two number
def power(x, y):
    return x ** y

print("+ - * / ^")
opration = str(input("select opration: "))

num1 = float(input("enter first number: "))
num2 = float(input("enter second number: "))

if opration == '+':
    print(num1, opration, num2, "=", num1 + num2)

elif opration == '-':
    print(num1, opration, num2, "=", num1 - num2)

elif opration == '*':
    print(num1, opration, num2, "=", num1 * num2)

elif opration == '/':
    print(num1, opration, num2, "=", num1 / num2)

elif opration == '^':
    print(num1, opration, num2, "=", num1 ** num2)

else :
    print("opration or other inputs are invalid")