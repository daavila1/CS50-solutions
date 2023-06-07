import random


def main():
    level = get_level()
    correct_answers = 10
    for i in range(10):
        numb_1 = generate_integer(level)
        numb_2 = generate_integer(level)
        numb_3 = numb_1 + numb_2

        for trys in range(3):
            try:
                result = int(input(f"{numb_1} + {numb_2} = "))
                if result != numb_3:
                    raise ValueError

            except ValueError:
                if trys == 2:
                    print("EEE")
                    print(f"{numb_1} + {numb_2} = {numb_3}")
                    correct_answers -= 1
                else:
                    print("EEE")
                    pass
            else:
                break


    print(f"Score: {correct_answers}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level not in [1,2,3]:
                raise ValueError

        except ValueError:
            pass

        else:
            return level


def generate_integer(level):
    if level == 1:
        min_numb = 0
    else:
        min_numb = int(pow(10, level - 1))

    max_numb = int(pow(10, level) - 1)
    return random.randint(min_numb, max_numb)


if __name__ == "__main__":
    main()
