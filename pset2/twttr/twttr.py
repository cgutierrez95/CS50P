text = input('Your text: ')
vowels = ['A','E','I','O','U','a','e','i','o','u']

for vowel in vowels:
    text = text.replace(vowel, "")

print(text)