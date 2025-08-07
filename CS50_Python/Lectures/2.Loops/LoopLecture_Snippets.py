# Loop lecture notes


# ==================================== #
# while

i = 3

while i != 0:
    print("loop")
    i = i - 1
    
print("")

while i < 3:
    print("loop2")
    i  += 1 # same as i = i + 1
    
print("")

#while True: #  Asks until 'break'
   # n = int(input("What is n?"))
   # if n > 0:
  #      break

# ==================================== #
# for

for i in [0,1,2]:
    print("forloop")

print("")

for i in range(3):
    print("forloop2")

print("")

# ==================================== #
# list
items = ["ItemOne","ItemTwo","ItemThree"]

for item in items:
    print(item)

print("")

for i in range(len(items)):
    print(i + 1, items[i] )

print("")

# ==================================== #
# dict

animalSizes = {
    "Dog": "Medium",
    "Cow": "Large",
    "Mouse": "Small",
    "Horse": "Large",
    "Rat": "Small",
    }

print(animalSizes)

print("")

for animal in animalSizes:
    print(animal, animalSizes[animal], sep=", ")
    
print("")
# ==================================== #
# other ways

print("multiplyloop\n" * 3, end="")


