import emoji


def main():
    prompt = input("Input: ")
    if prompt.find("_") != -1:
        print(emoji.emojize(f"Output: {prompt}"))
    else:
        print(emoji.emojize(f"Output: {prompt}", language="alias"))


main()
