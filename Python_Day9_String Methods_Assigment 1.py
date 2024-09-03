def count_elements(input_string):
    chars = digits = symbols = 0

    for char in input_string:
        if char.isalpha():
            chars += 1
        elif char.isdigit():
            digits += 1
        else:
            symbols += 1

    return chars, digits, symbols

input_string = "P@#yn26at^&i5ve"

#Counting elements
chars, digits, symbols = count_elements(input_string)

print(f"Chars = {chars}")
print(f"Digits = {digits}")
print(f"Symbols = {symbols}")
