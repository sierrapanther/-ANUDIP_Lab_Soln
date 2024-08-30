def factorial(number):
    result = 1  # Initialize result
    while number > 0:
        result *= number  # Multiply result by the current number
        number -= 1  # Decrease the number by 1
    return result

number = int(input("Enter a number: "))
if number >= 0:
    print(f"The factorial of {number} is {factorial(number)}.")
else:
    print("Factorial is not defined for negative numbers.")
