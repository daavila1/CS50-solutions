from tabulate import tabulate
import csv
import sys


def main():
    while True:
        try:
            if len(sys.argv) != 2:
                raise IndexError
            else:
                if sys.argv[1].endswith(".csv"):
                    file = sys.argv[1]
                    menu = open(file)
                    menu.close
                else:
                    sys.exit("Not a CSV file")

        except IndexError:
            if len(sys.argv) < 2:
                sys.exit("Too few command-line arguments")
            elif len(sys.argv) > 2:
                sys.exit("Too many command-line arguments")

        except FileNotFoundError:
            sys.exit("File does not exist")

        else:
            print(tabulate((tabulate_menu(file)), headers = "firstrow", tablefmt = "grid"))
            break



def tabulate_menu(pizza_type):
    menu = []
    with open (pizza_type) as file:
        reader = csv.reader(file)
        for name, size, price in reader:
            menu.append({"name": name, "size": size, "pice": price})

    return menu


if __name__ == "__main__":
    main()