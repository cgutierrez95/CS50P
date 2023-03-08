x, y, z = input('Expression: ').split(" ")
x = float(x)
z = float(z)

if y == '+':
    print(x + z)

if y == '-':
    print(x - z)

if y == '*':
    print(x * z)

if y == '/':
    print(x / z)

    #print(float(f'{float2:.2f}'))
    #print("%.2f" % x)