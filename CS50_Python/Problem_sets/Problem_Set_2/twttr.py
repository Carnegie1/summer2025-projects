def main():
    userInput = input("Input: ")
    print(removeVowels(userInput))


#Removes vowels from an inputted string
def removeVowels(userInput):

  tweet = ""
  for i in userInput:
        if i.lower() in ("a", "e", "i", "o", "u"):
            tweet = tweet
        else:
            tweet = tweet + i


  return(tweet)


main()
