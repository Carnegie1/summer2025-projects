# importing 'random' library - imports everything from the library
import random
import statistics
import sys
import requests
import json


# chooses a specific function from a libary.
# This means you can just use 'choice' rather than needing 'random.choice'
# However this means we can no longer create our own 'choice' method
from random import choice


# Using methods from random
coin = random.choice(["heads", "tails"])
print(coin)

number = random.randint(1,10)
print(number)

numbers = ["one","two","three"]
random.shuffle(numbers)

for nums in numbers:
    print(nums)

    
# Using methods from statistics
print("Mean:" + str(statistics.mean([100,90,80,34,56,33,12,23])))



#Using items from sys and requests
try:
    print("The first word you typed after calling the program: " + sys.argv[1])
except IndexError:
    sys.exit("too few arguments")

print(
    json.dumps(request.get
               ('httep://itunes.apple/search?entity=song&limit=1&term="weezer"')))
