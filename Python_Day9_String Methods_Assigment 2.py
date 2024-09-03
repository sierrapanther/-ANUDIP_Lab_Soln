def remove_duplicate_words(input_string):
    words = input_string.split()
    result = []
    seen = set()

    for word in words:
        if word not in seen:
            seen.add(word)
            result.append(word)

    return ' '.join(result)

input_string = "String and String Function"

#Removing duplicate words
output_string = remove_duplicate_words(input_string)


print(output_string)
