def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    plate = list(s)
    # this code is a list comprehension, for me in this moment it seems kind of complex so i would rather use a for
    # numbers = [number for number in plate if number.isdigit()]
    after_digit = get_afdgt(plate)
    if (
        after_digit == []
        and 2 <= len(plate) <= 6
        and all(char.isalnum() for char in plate)
    ):
        return True
    elif (
        2 <= len(plate) <= 6
        and all(char.isalpha() for char in plate[:2])
        and all(char.isalnum() for char in plate)
        and after_digit[0] != "0"
        and all(char.isdigit() for char in after_digit)
    ):
        return True
    else:
        return False


# this function return the first digit in the list and every alphanumeric caracter after it
def get_afdgt(lst):
    list(lst)
    after_digit = []
    for i in range(len(lst)):
        if lst[i].isdigit():
            while i < len(lst):
                after_digit.append(lst[i])
                i += 1
            break
    return after_digit


if __name__ == "__main__":
    main()
