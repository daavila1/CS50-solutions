def main():
    expr = input ("Expression: ")
    x,y,z = expr.split(" ")
    calculator(x,y,z)


def calculator(a,b,c):

    match b:
        case "+":
            return print(float(f"{int(a) + int(c):.2f}"))

        case "-":
            return print(float(f"{int(a) - int(c):.2f}"))

        case "*":
            return print(float(f"{int(a) * int(c):.2f}"))

        case "/":
            return print(float(f"{int(a) / int(c):.2f}"))


main()

