input("Enter three numbers")
num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))
num3 = int(input("Enter third number:"))
print(f"The value of num1 is {num1}, and it is of the type {type(num1)}.")
print(f"The value of num2 is {num2}, and it is of the type {type(num2)}.")
print(f"The value of num3 is {num3}, and it is of the type {type(num3)}.")
print(f"The sum of num1 and num2 is {num1 + num2}.")
print(f"The sum of all three numbers is {num1 + num2 + num3}.")
result = (num1+ num2) * num3
print(f"The result of (num1 + num2) * num3 is {result}.")
num1 < num2
num2 > num3
num3 < num1
print(f"Is num1 less than num2? {num1 < num2}")