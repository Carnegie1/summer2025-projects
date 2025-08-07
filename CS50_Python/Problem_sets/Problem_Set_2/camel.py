# Converts a variable in camelCase to snake_case
def main():
    camelCase = input("CamelCase: ")

    print("snake_case: " + snakeCamelConvert(camelCase))


def snakeCamelConvert(camelCase):
    snake = camelCase[0]

    for i in camelCase[1:]:
     if i.isupper():
         snake = snake + "_" + i
     else:
       snake = snake + i

    return(snake.lower())

main()
