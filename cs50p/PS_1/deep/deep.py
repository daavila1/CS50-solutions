def main():
    question = input("What is the Great Question of Life, the Universe and Everything " ).strip().lower()
    Y_N (question)

def Y_N (n):
    match n:
        case "42" | "forty two" | "forty-two":
            return print ("Yes")
        case _:
            return print ("No")

main()