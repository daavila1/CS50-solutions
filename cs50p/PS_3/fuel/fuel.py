def main():
    gt_fuel()

def gt_fuel():
    while True:
        try:
            fraction = input("Fraction: ")
            x, y = map(int, fraction.split("/"))
            fuel = x/y*100
            if x > y:
                raise ValueError
        except (ValueError, ZeroDivisionError):
            pass
        else:
            if fuel <= 1:
                return print("E")
            elif fuel >= 99:
                return print("F")
            else:
                return print(f"{fuel:.0f}%")

main()