
import hashlib


def main():
    str1 = "String to Be encoded "

    text = input(str1)
    textUtf8 = text.encode("utf-8")

    hash = hashlib.md5(textUtf8)
    hexa = hash.hexdigest()

    print(text)

    print(f"The Text Is {text}")

    print(hexa)

    return


main()
