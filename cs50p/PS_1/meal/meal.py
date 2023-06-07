def main():
    time = input("What time is it? ").lower().strip()
    time = convert(time)
    mealclass(time)

def convert(h):
    if h.find("a.m.") > 0:
        t, f = h.split(" ")
        hours, seconds = t.split(":")
        return float(f"{float(hours) + float(seconds)/60:.2f}")

    elif h.find("p.m.") > 0:
        t, f = h.split(" ")
        hours, seconds = t.split(":")
        return float(f"{(float(hours)+12) + float(seconds)/60:.2f}")

    else:
        hours, seconds = h.split(":")
        return float(f"{float(hours) + float(seconds)/60:.2f}")

def mealclass(t):
    if 7 <= t <= 8:
        return print("breakfast time")
    elif 12 <= t <=13:
        return print("lunch time")
    elif 18 <= t <=19:
        return print ("dinner time")
    else:
        return print ("")


if __name__ == "__main__":
    main()