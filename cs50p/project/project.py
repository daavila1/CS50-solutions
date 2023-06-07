import re
import random


def main():
    chars = {
        "letters": "abcdefghijklmnopqrstuvwxyz",
        "numbers": "1234567890",
        "symbols": "@()[]{}*@,;/-_¿?.¡!$<#>&+%=",
        "lenght": 12,
    }
    while True:
        try:
            password_type = input("Auto generate password? Yes/No ").lower()
            typ = get_type(password_type)

        except ValueError:
            print("Invalid input")

        else:
            match typ:
                case "yes":
                    print("Password: ", end="")
                    print(
                        *generate(
                            chars["letters"],
                            chars["numbers"],
                            chars["symbols"],
                            chars["lenght"],
                        ),
                        sep="",
                    )
                    break

                case "no":
                    i = 0
                    while i <= 3:
                        try:
                            char = get_parameter(i)

                        except ValueError:
                            print(f"Invalid input, only {parameters[i]}")
                            pass

                        else:
                            parameters = ["letters", "numbers", "symbols", "lenght"]
                            chars[parameters[i]] = char
                            i += 1

                    print("Password: ", end="")

                    print(
                        *generate(
                            chars["letters"],
                            chars["numbers"],
                            chars["symbols"],
                            int(chars["lenght"]),
                        ),
                        sep="",
                    )
                    break


def get_type(t):
    if _ := re.search(r"^yes|no$", t):
        return t
    else:
        raise ValueError


def generate(alpha, numbs, symb, leng):
    alpha_upper = alpha.upper()
    base = alpha + alpha_upper + numbs + symb
    return random.sample(base, leng)


def get_parameter(i):
    parameters = ["letters", "numbers", "symbols", "lenght"]
    char_i = input(f"Prefered {parameters[i]}: ")
    match i:
        case 0:
            if _ := re.search(r"^[a-zA-Z]+$", char_i):
                return char_i
            else:
                raise ValueError

        case 1 | 3:
            if _ := re.search(r"^[0-9]+$", char_i):
                return char_i
            else:
                raise ValueError

        case 2:
            if _ := re.search(r"^[@()[\]{}*,;/\-_¿\?\.¡!$<#>&\+%=]+$", char_i):
                return char_i
            else:
                raise ValueError


if __name__ == "__main__":
    main()