def main():
    answer = input("Greeting: ")
    # Removes whitespace and converts all letters to lowercase
    print(moneyCalc(answer.casefold().strip()))

def moneyCalc(response):
    if(response.find("hello") != -1): #If hello is found
        return("$0")
    elif(response.find("h") == 0): # iF h is the first letter
        return("$20")
    else:
        return("$100")

main()
