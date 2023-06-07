def main():
    text = input("Input: ")
    text = list(text)
    vowels = ["a","e","i","o","u","A","E","I","O","U"]
    ntext = t_without_v(text, vowels)
    print()

def t_without_v(text, vowels):
    
    for i in range(len(text)):
        for j in range(len(vowels)):
            if text[i] == vowels[j]:
                text[i] = ""

    for letter in text:
        print(letter, end="", sep="")

main()

