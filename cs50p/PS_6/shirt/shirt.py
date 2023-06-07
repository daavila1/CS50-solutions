from PIL import ImageOps
from PIL import Image
import sys
from os.path import splitext


def main():
    while True:
        input_file = splitext(sys.argv[1])
        output_file = splitext(sys.argv[2])
        try:
            if len(sys.argv) != 3:
                raise IndexError
            elif input_file[1] != output_file[1]:
                sys.exit("Input and output have different extensions")
            else:
                Image.open(sys.argv[1])

        except IndexError:
            if len(sys.argv) < 3:
                sys.exit("Too few command-line arguments")
            elif len(sys.argv) > 3:
                sys.exit("Too many command-line arguments")

        except FileNotFoundError:
            if (input_file[1] != [".jpg", ".png", ".jpge"]
            or output_file[1] != [".jpg",".png",".jpge"]):
                sys.exit("Invalid Input")

        else:
            resize()
            break


def resize():
    shirt = Image.open("shirt.png")
    image = Image.open(sys.argv[1])
    size = shirt.size
    resize = ImageOps.fit(image, size, bleed=0.0, centering=(0.5, 0.5))
    resize.paste(shirt, shirt)
    resize.save(sys.argv[2])


if __name__ == "__main__":
    main()