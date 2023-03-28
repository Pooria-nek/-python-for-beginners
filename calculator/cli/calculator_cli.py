# its just a simple calculator program 

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