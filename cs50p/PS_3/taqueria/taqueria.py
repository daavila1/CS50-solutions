def main():
    order()
    print()

def order():
    total = float(0)
    while True:
        try:
            item = input("Item: ").title()
            if item in menu:
                subtotal = float(menu[item])
            else:
                raise ValueError

        except (ValueError):
            pass

        except (EOFError):
            return print(end="")

        else:
            total = total + subtotal
            print(f"Total: ${total:.2f}")

menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}


main()
