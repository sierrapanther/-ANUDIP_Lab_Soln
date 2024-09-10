def count_words_in_file(file_name):
        
        with open(file_name, 'r') as file:
            content = file.read()
            words = content.split()  # Split the content into words based on spaces
            total_words = len(words)
            print(f"Total number of words: {total_words}")
   
count_words_in_file('ABC.txt')
