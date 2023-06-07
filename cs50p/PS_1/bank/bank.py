def main():
    greating = input ("Greating: ").lower().strip()
    first = first_l(greating)
    all = first_word(greating)
    verify(first,all)

def first_l(x):
    x=x[0]
    return x

def first_word(x):
    x=x[0:5]
    return x

def verify(f,a):
    if a == "hello":
        return print("$0")
    elif f == "h":
        return print ("$20")
    else:
        return print("$100")


main()