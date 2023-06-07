import re

def main():
    print(parse(input("HTML: ").strip()))


def parse(s):
    if matches := re.search(r"^.+https?://(?:www\.)?youtube\.com/embed/([a-zA-Z0-9]+).+$", s, re.IGNORECASE):
        return f"https://youtu.be/{matches.group(1)}"


if __name__ == "__main__":
    main()