def main():
    camel = input("camelCase: ")
    snake = camel_to_snake(camel)
    print()

def camel_to_snake(camel):
    print("snake_case: ", end="")
    for letter in camel:
        if letter.isupper():
            print("_",letter.lower(), end="", sep="")
        else:
            print(letter, end="", sep="")

main()