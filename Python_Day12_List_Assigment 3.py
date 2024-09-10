def find_duplicates(numbers):
    duplicates = [] 
    seen = set()    

    for number in numbers:
        if number in seen and number not in duplicates:
            duplicates.append(number)  
        seen.add(number)               
    return duplicates

numbers = [1, 2, 3, 4, 2, 5, 6, 3, 7, 8, 1]
duplicates = find_duplicates(numbers)
print(f"Duplicate values are: {duplicates}")
