def main():
    while True:
        fraction = input("Fraction: ")
        try:
            fuel = convert(fraction)
        except (ValueError, ZeroDivisionError):
            pass
        else:
            print(gauge(fuel))
            break


def convert(fraction):
    x, y = map(int, fraction.split("/"))
    fuel = x / y * 100
    if x > y:
        raise ValueError
    else:
        return round(fuel)


def gauge(fuel):
    if fuel <= 1:
        return "E"
    elif fuel >= 99:
        return "F"
    else:
        return f"{fuel:.0f}%"


if __name__ == "__main__":
    main()
