import sys


def main():
    while True:
        try:
            file = sys.argv[1]
            if len(sys.argv) != 2:
                raise IndexError

            elif not file.endswith(".py"):
                sys.exit("Not a Python file")

            else:
                verify_file(file)

        except IndexError:
            if len(sys.argv) < 2:
                sys.exit("Too few command-line arguments")
            elif len(sys.argv) > 2:
                sys.exit("Too many command-line arguments")

        except FileNotFoundError:
            sys.exit("File does not exist")

        else:
            print(count_lines(file))
            break


def verify_file(name):
    file = open(name)
    file.close


def count_lines(name):
    lines = 0
    with open(name) as file:
        for line in file:
            if line.strip().startswith("#") or not line.strip():
                pass
            else:
                lines += 1
    return lines


if __name__ == "__main__":
    main()

# IndexError
# File not found error
