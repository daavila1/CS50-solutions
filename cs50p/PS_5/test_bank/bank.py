def main():
    greeting = input ("Greating: ")
    print(f"${value(greeting)}")


def value(text):
    text = text.lower().strip()
    first_letter = text[0]
    first_word = text [0:5]

    if first_word == "hello":
        return 0
    elif first_letter == "h":
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
