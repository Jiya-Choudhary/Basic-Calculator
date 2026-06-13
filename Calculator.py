print("Basic Calculator")
Num1 = int(input("Enter first number: "))
Num2 = int(input("Enter second number: "))
Operation = input("Enter operation (+, -, *, /, OFF): ")
while True:
 if Operation == "+":
    print("Result:", Num1 + Num2)
    Operation = input("Enter operation (+, -, *, /, OFF): ")
    if Operation == "OFF":
       print("OFF")
       break
    else:
       Num1 = int(input("Enter first number: "))
       Num2 = int(input("Enter second number: "))
 elif Operation == "-":
    print("Result:", Num1 - Num2)
    Operation = input("Enter operation (+, -, *, /, OFF): ")
    if Operation == "OFF":
       print("OFF")
       break
    else:
       Num1 = int(input("Enter first number: "))
       Num2 = int(input("Enter second number: "))
 elif Operation == "*":
    print("Result:", Num1 * Num2)
    Operation = input("Enter operation (+, -, *, /, OFF): ")
    if Operation == "OFF":
       print("OFF")
       break
    else:
       Num1 = int(input("Enter first number: "))
       Num2 = int(input("Enter second number: "))
 elif Operation == "/":
    if Num2 == 0:
        print("Not Possible")
        Operation = input("Enter operation (+, -, *, /, OFF): ")
        if Operation == "OFF":
         print("OFF")
         break
        else:
         Num1 = int(input("Enter first number: "))
         Num2 = int(input("Enter second number: "))
    else:
        print("Result:", Num1 / Num2)
        Operation = input("Enter operation (+, -, *, /, OFF): ")
        if Operation == "OFF":
         print("OFF")
         break
        else:
         Num1 = int(input("Enter first number: "))
         Num2 = int(input("Enter second number: "))
 else:
    print("Invalid")
    break