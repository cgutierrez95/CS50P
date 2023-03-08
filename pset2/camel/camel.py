word = input('Word: ')
new_word = ''
for letter in word:
    if letter.isupper():
        new_word = new_word + '_'
    new_word = new_word + letter.lower()

print(new_word)