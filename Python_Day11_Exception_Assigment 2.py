def get_integer():
    try:
        user_input = input("Please enter an integer: ")
        value = int(user_input)  
        print(f"You entered the integer: {value}")
    except ValueError:
        raise ValueError("Invalid input: Please enter a valid integer.")  

try:
    get_integer()
except ValueError as e:
    print(e)
