# Function to check if a string is a palindrome
def is_palindrome(s):
    #for uniformity
    s = s.replace(" ", "").lower()
    
    #Check if the string is equal to its reverse
    return s == s[::-1]

# Example usage
string = input("Enter a string: ")

if is_palindrome(string):
    print(f'"{string}" is a palindrome.')
else:
    print(f'"{string}" is not a palindrome.')
