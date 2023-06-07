import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if matches := re.search(
        r"^((?:[0-9]|1[0-2])(?:\:[0-5][0-9])?) (AM|PM) to ((?:[0-9]|1[0-2])(?:\:[0-5][0-9])?) (AM|PM)$",
        s,
        re.IGNORECASE,
    ):
        start = float(matches.group(1).replace(":", "."))
        if matches.group(2).lower() == "am" and start == 12:
            start = 0
        end = float(matches.group(3).replace(":", "."))
        if matches.group(4).lower() == "pm" and end == 12:
            end = 0
    else:
        raise ValueError

    if matches.group(2).lower() == "am" and matches.group(4).lower() == "pm":
        end += 12

    elif matches.group(2).lower() == "pm" and matches.group(4).lower() == "am":
        start += 12

    elif matches.group(2).lower() == "pm" and matches.group(4).lower() == "pm":
        start += 12
        end += 12

    else:
        start
        end

    return (f"{start:05.2f} to {end:05.2f}").replace(".", ":")


if __name__ == "__main__":
    main()
