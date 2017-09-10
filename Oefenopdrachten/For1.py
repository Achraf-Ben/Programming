sentence = input('Please enter a sentence: ')
no_spaces = ''

for letter in sentence:
    if letter != ' ':
        no_spaces += letter

print("You sentence with spaces removed:")
print(no_spaces)