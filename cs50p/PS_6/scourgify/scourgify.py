import csv
import sys


def main():
    while True:
        try:
            if len(sys.argv) != 3:
                raise IndexError
            else:
                test = open(sys.argv[1])
                test.close

        except IndexError:
            if len(sys.argv) > 3:
                sys.exit("Too few command-line arguments")
            elif len(sys.argv) < 3:
                sys.exit("Too many command-line arguments")

        except FileNotFoundError:
            sys.exit(f"Could not read {sys.argv[1]}")

        else:
            rearrange()
            break


def rearrange():
    students = []

    with open(sys.argv[1]) as file:
        reader = csv.DictReader(file)
        for row in reader:
            student = row["name"].replace(" ", "")
            s_name, f_name = student.split(",")
            entry = {
                "first_name": f_name,
                "second_name": s_name,
                "house": row["house"],
            }
            students.append(entry)

    with open(sys.argv[2], "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
        writer.writeheader()
        for row in students:
            writer.writerow(
                {
                    "first": row["first_name"],
                    "last": row["second_name"],
                    "house": row["house"],
                }
            )


if __name__ == "__main__":
    main()