def find_largest_and_smallest(numbers):
    if not numbers: 
        return None, None
    
    largest = numbers[0]
    smallest = numbers[0]

    for number in numbers[1:]:
        if number > largest:
            largest = number
        if number < smallest:
            smallest = number

    return largest, smallest

numbers = [3, 1, 4, 1, 5, 9, -2, 7]
largest, smallest = find_largest_and_smallest(numbers)
print(f"The largest number is: {largest}")
print(f"The smallest number is: {smallest}")
