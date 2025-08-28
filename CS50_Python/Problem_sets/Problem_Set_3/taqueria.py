def main():
    totalPrice = 0.00
    # do until EOFError
    while True:
        try:
            userInput = input("Item: ").title()
            if userInput in items:
                # Adds the price of the inputted item to the total
                totalPrice = totalPrice + items[userInput]
                # format to have 2 decimal places
                print("$" + str(format(totalPrice, ".2f")))
        except EOFError:
            break

# Dictionary
items= {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
    }



main()
