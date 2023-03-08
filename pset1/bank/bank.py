greet = input('Your greeting: ').lower()
if 'hello' in greet:
    print('$0')
elif'h' == greet[0] and 'hello' not in greet:
    print('$20')
else:
    print('$100')