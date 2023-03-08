import sys, os
from PIL import Image, ImageOps

args = list(sys.argv)
ext = ('jpeg', 'jpg', 'png')

if len(args) > 3:
    sys.exit('Too many command-line arguments')

if len(args) < 3:
    sys.exit('Too few command-line arguments')

if not args[1].endswith(ext) or not args[2].endswith(ext):
    sys.exit('Not a supported file')

if os.path.splitext(args[1])[1] != os.path.splitext(args[2])[1]:
    sys.exit('different extensions')

try:
    with Image.open(args[1]) as input:
        with Image.open('shirt.png') as shirt:
            input = ImageOps.fit(input, shirt.size)
            input.paste(shirt, shirt)
            input.save(args[2])

except FileNotFoundError:
    sys.exit('file does not exist')