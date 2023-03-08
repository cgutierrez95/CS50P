from pyfiglet import Figlet
import sys

args = list(sys.argv)

if len(args) == 1:
    figlet = Figlet()
    s = input("Input: ")
    print(figlet.renderText(s))

if len(args) == 2:
    sys.exit('Error')

if len(args) == 3:
    if args[1] != '-f' and args[1] != 'font':
        sys.exit('Error')
if len(args) == 3:
    f = args[2]
    figlet = Figlet()
    fonts = figlet.getFonts()

    if f in fonts:
        figlet.setFont(font=f)
    else:
        sys.exit('Error')

    s = input("Input: ")
    print(figlet.renderText(s))

