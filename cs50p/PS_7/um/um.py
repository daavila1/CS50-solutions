import re

def main():
    print(count(input("Text: ")))


def count(s):
    m = s.lower()
    matches = re.findall(r"\bum\b", m)
    return len(matches)


if __name__ == "__main__":
    main()

#Um... what are regular expressions 1 not 0
#Um, thanks, um, regular expressions make sense now. 2 not 1
#Um? Mum? Is this that album where, um, umm, the clumsy alums play drums?