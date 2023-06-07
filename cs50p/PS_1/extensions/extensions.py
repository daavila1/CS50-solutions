def main ():
    file = input("File name: ").lower().strip()
    file_type(file)



def file_type(x):
    if x.rfind(".gif", len(x) - 4 , len(x)) > 0:
        return print("image/gif")

    elif x.rfind(".jpg", len(x) - 4 , len(x)) > 0 or x.find(".jpeg", len(x) - 4 , len(x)) > 0:
        return print("image/jpeg")

    elif 0 < x.rfind(".png", len(x) - 4 , len(x)) > 0:
        return print("image/png")

    elif 0 < x.rfind(".pdf", len(x) - 4 , len(x)) > 0:
        return print("application/pdf")

    elif 0 < x.rfind(".txt", len(x) - 4 , len(x)) > 0:
        return print("text/plain")

    elif 0 < x.rfind(".zip", len(x) - 4 , len(x)) > 0:
        return print("application/zip")

    else:
        return print("application/octet-stream")

main()