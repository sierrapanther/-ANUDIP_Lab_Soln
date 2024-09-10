def divide_numbers(numerator, denominator):
    try:
        result = numerator / denominator
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
        result = None
    return result

numerator = 12
denominator = 0

result = divide_numbers(numerator, denominator)
if result is not None:
    print(f"The result is: {result}")
