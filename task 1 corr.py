import re

file_path = 'task1_en.txt'
with open(file_path, 'r') as file:
    text = file.read()

words_followed_by_comma_pattern = r'\b\w+,\s*'
informatin_in_square_blackets = r'\(\d+\)'

words_followed_by_comma = re.findall(words_followed_by_comma_pattern, text)
informatin_in_square_blackets = re.findall(informatin_in_square_blackets, text)

formatted_words = [word.strip() for word in words_followed_by_comma]


print("Words followed by a comma:", formatted_words)
print("Information in square blackets: ", informatin_in_square_blackets)