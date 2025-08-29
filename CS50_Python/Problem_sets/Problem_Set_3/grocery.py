def main():
    items = {}
    while True:
        try:
            userItem = input().upper()
            if userItem in items:
                items[userItem]["amount"] += 1

            else:
                items[userItem] = {"item": userItem, "amount": 1}

        # Ctrl+D ends program
        except EOFError:
            # create a new dictionary, which is a sorted version of the first one
            sortedItems = dict(sorted(items.items()))
            for item in sortedItems:
                # formatting as problem required
                print(str(items[item]["amount"]) + " " + str(items[item]["item"]))
            break


main()
