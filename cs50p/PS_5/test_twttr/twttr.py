def main():
    text = input("Input: ")
    print(shorten(text))


def shorten(text):
    text = list(text)
    vowels = ["a","e","i","o","u","A","E","I","O","U"]
    for i in range(len(text)):
        for j in range(len(vowels)):
            if text[i] == vowels[j]:
                text[i] = ""

    return "".join(text)


if __name__ == "__main__":
    main()
