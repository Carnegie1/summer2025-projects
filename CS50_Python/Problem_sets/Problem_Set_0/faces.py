def convert(userPhrase):
    userPhrase = userPhrase.replace(":)", "🙂")
    userPhrase = userPhrase.replace(":(", "🙁")
    return userPhrase


def main():
    userPhrase = input("Input: ")
    print(convert(userPhrase))

main()
