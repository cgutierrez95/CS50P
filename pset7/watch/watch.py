import re
import sys

def main():
    print(parse(input("HTML: ")))

def parse(s):

    if 'youtube' not in s:
        return

    if not re.search(r"<iframe(.)*><\/iframe>", s):
        return

    address = re.search(r"(http(s)*:\/\/(www\.)*youtube\.com\/embed\/)([a-z_A-Z_0-9]+)", s)

    if address:
        address = address.groups()
        short_link = 'https://youtu.be/' + address[3]
    return short_link

if __name__ == "__main__":
    main()