def main():
    answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything?")
    # Removes whitespace and converts all letters to lowercase
    print(isCorrect(answer.casefold().strip()))

def isCorrect(response):
    match response:
        case "42" | "forty-two" | "forty two":
            return("Yes")

        case _:
            return("No")


main();
