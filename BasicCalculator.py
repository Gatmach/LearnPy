# Basic calculator that adds two numbers
# num1 = float(input("Entet a number: "))
# num2 = float(input("Enter anther number: "))
# answer = num1 + num2
# print(answer)


# Building a basic calculator that performs basic calculations on two numbers
# Initial points
num1 = float(input("Entet a number: "))
num2 = float(input("Enter another number: "))
operator = input("Enter an operator (+, - , *, /, %) ")
if operator == '+':
    print(num1 + num2)
elif operator == '-':
    print(num1 - num2)
elif operator == '*':
    print(num1 * num2)
elif operator == '/':   
    print(round((num1 / num2),3))
elif operator == '%':
    if num1 % num2 == 1:
        results = num1 % num2
        print(results)
    else:
        print('Invalid')
else:
    print('Invalid operator..')
    
