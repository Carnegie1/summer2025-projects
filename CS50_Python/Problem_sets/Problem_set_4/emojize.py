import emoji
def main():
    userInput = input("Input: ")

    #without using the second parameter, the incorrect emoji list is used for the requirements
    print("Output: " + emoji.emojize(userInput, language='alias'))
main()
