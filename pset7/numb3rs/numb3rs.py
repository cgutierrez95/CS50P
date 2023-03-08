def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    try:
        a, b, c, d = ip.split('.')
    except:
        return False

    ip_segments = [int(a), int(b), int(c), int(d)]

    for i in ip_segments:
        if i < 0 or i > 255:
            return False
    return True

if __name__ == "__main__":
    main()