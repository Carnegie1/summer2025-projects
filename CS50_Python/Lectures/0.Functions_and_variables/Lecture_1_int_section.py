# --- LECTURE ONE --- int section

#Note: Input always takes a string value
x = input("What is the value of x?")

y = input("What is the value of y?")


#Casting x and y to ints, to avoid '+' string concatenation
# Note: int could've been casted each time on 'input' also
z = int(x) + int(y)

# 'float' is the equivalent of a double in java, a 64 bits, not 32.
z = float(x) / float(y)

# Round function, second parameter is the number of digits to found to.
print(round(z,4))



