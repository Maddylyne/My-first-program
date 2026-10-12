number = int(input("Enter a number: "))
print(f"The value of number is {number}, and it is of the type {type(number)}.")
if number > 0:
    print(f"The number {number} is positive.")
elif number < 0:
    print(f"The number {number} is negative.")
else:
    print(f"The number {number} is zero.")
age = int(input("Enter your age: "))
if age >= 18:
    print(f"You are {age} years old, and you are an adult.")
else:
    print(f"You are {age} years old, and you are a minor.")
number = int(input("Enter a number between 1 and 3: "))
if number == 1:
    print(f"You WIN!")
elif number == 2:
    print(f"You TIE!")
elif number == 3:
    print(f"You LOSE!")
else: 
    print(f"Invalid input. Please enter a number between 1 and 3.")