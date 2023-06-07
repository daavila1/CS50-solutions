import inflect
import sys

p = inflect.engine()


def main():
    lst_names = p.join(gt_names())
    print("Adieu, adieu, to", lst_names)


def gt_names():
    names = []
    while True:
        try:
            name = input("Name: ").title()

        except EOFError:
            print()
            return names

        else:
            names.append(name)


main()


# JOIN WORDS INTO A LIST:

# mylist = p.join(("apple", "banana", "carrot"))
# "apple, banana, and carrot"

# mylist = p.join(("apple", "banana"))
# "apple and banana"

# mylist = p.join(("apple", "banana", "carrot"), final_sep="")
# "apple, banana and carrot"
