from pyfiglet import Figlet
import sys
import random

def main():

    f = Figlet()
    listOfFonts = f.getFonts()
    fontType = None
    if len(sys.argv) == 3:
        #checks if command line inputs are correct
        if( (sys.argv[1] == "-f" or sys.argv[1] == "--font") and  (sys.argv[2] in listOfFonts) ):
            fontType = "given"
            f.setFont(font=sys.argv[2])

    #font is random if there are no command line inputs
    elif len(sys.argv) == 1:
        fontType = "random"
        f.setFont(font=(random.choice(listOfFonts)))

    #FontType is only set with a correct input
    if fontType is None:
      sys.exit("Invalid usage")

    userInput = input("Input: ")
    print(f.renderText(userInput))

main()

