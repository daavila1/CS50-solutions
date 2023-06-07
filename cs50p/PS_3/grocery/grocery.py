def main():
    order = gt_order()
    srted_order = sorted(order)
    for item in srted_order:
        if item in order:
            print(order[item], item, sep = " ")
        else:
            break

def gt_order():
    pre_order = []
    order = {}
    while True:
        try:
            item = input().upper()
        except EOFError:
            return order
        else:
            pre_order.append(item)
            order[item] = pre_order.count(item)

main()