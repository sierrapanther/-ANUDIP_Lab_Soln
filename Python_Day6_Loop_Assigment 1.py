def is_palindrome(number):
    #Convert the number to a string
    num_str = str(number)
    
    #Check if the string is the same forwards and backwards
    if num_str == num_str[::-1]:
        return True
    else:
        return False

# Test the function
number = int(input("Enter a number: "))
if is_palindrome(number):
    print(f"{number} is a palindrome.")
else:
    print(f"{number} is not a palindrome.")
