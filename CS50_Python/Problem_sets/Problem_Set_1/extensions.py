def main():

    userFile = input("File name: ")

    print(calculateMediaType(userFile.casefold().strip()))


def calculateMediaType(givenFile):
    fileType = givenFile.split(".")[-1] #Splits the string and only takes the last word after .
    fileName = givenFile.split(".")[0]

    match fileType:
        case "gif" | "jpeg" | "png":
            fileType = "image/" + fileType
        case "jpg":
            fileType = "image/jpeg"
        case "pdf" | "application" | "zip" :
             fileType = "application/" + fileType
        case "txt":
            fileType = "text/" + fileName
        case _:
            fileType = "application/octet-stream"


    return fileType


main()
