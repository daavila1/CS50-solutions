def main():
    format_date()

def format_date():
    while True:
        try:
            date = input("Date: ").title()
            date = date.replace("/"," ")
            m, d, y = date.split()
            d = d.replace(",","")
            if all(char.isalpha() for char in m) and date.find(",") == -1:
                raise ValueError
            elif all(char.isalpha() for char in m):
                m = months[m]
            else:
                m = int(m)
            d = int(d)
            y = int(y)
            if d > 31 or m > 12:
                raise ValueError

        except ValueError:
            pass

        else:
            return print(f"{y}-{m:02}-{d:02}")

#ValueError

months = {
    "January":1,
    "February":2,
    "March":3,
    "April":4,
    "May":5,
    "June":6,
    "July":7,
    "August":8,
    "September":9,
    "October":10,
    "November":11,
    "December":12
}

main()