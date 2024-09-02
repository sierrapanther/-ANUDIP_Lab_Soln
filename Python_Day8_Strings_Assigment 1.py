from collections import Counter
import re

string = "To change the overall look of your document. To change the look available in the gallery"

# Convert the string to lowercase and remove punctuation
string = re.sub(r'[^\w\s]', '', string.lower())

# Split the string into words
words = string.split()

# Count the occurrences of each word using Counter
word_count = Counter(words)

# Display the word counts
for word, count in word_count.items():
    print(f"'{word}': {count}")
