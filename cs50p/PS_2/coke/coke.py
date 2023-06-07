def main():
    due = int(50)
    while due <= int(50):
        coin = get_coin(due)
        due = due - coin
        if due > 0:
            print("Amount Due: ", due)
        elif due <= 0:
            print("Change Owed: ", abs(due))
            break

def get_coin(due):
    while True:
        coin = int(input("Insert Coin: " ))
        if coin == 5 or coin == 10 or coin == 25:
            return int(coin)
        else:
            print("Amount Due: ", due)
            
main()