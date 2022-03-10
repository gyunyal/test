def add(a,b):
    return a+b
def substract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if b == 0:
        print("Cannot divide by zero")
    else:
        return a / b

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    operator=input("Select operator 1, 2, 3, 4:  ")
    if operator in ("1", "2", "3", "4"):
        num1=float(input("Enter one number:  "))
        num2=float(input("Enter second number:  "))

        if operator == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif operator == '2':
            print(num1, "-", num2, "=", substract(num1, num2))

        elif operator == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif operator == '4':
            print(num1, "/", num2, "=", divide(num1, num2))

        next_calculation = input("Let's do next calculation? (y/n): ")
        if next_calculation == "n":

            break

    else:
        print("Invalid Input")
