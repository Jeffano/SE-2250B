print("Enter The First Number:")
num1 = int(input())

print("Enter an Operation: + , - , x , / ")
operation = input()

print("Enter The Second Number:")
num2 = int(input())

if operation == "+":
    print (num1 + num1)
elif operation == "-":
    print(num1 - num2)
elif operation == "x":
    print(num1 * num2)
elif operation == "/":
    print(num1/num2)