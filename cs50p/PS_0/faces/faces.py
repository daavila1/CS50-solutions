def main():
    text = str(input())
    convert(text)

def convert(tofaces):
    text=tofaces.replace(":)","🙂").replace(":(","🙁")
    return print(text)

main()