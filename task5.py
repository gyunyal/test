num1 = int(input("Enter a number: "))
num2 = int(input("Enter second number: "))
inp = input("Enter “a” if you want to Add “b” if you want to Subtract,  “c” to Divide, “d” to Multiply, “e”  for Exponentiation:  ")
if  inp == "a":
    res1 = num1 + num2
    print(res1)
elif inp == "b":
    res2 = num1-num2
    print(res2)
elif inp == "c":
    res3 = num1 / num2
    print(res3)
elif inp == "d":
    res4 = num1 * num2
    print(res4)
elif inp == "e":
    res5 = num1**num2
    print(res5)


