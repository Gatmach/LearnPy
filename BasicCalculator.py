'''
Basic calculator that requires a user to enter two numbers and the type of operator he or she wants to use
The program is implemented using if-else statements to determine the various conditions.
'''
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
    
