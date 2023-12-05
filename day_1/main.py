file = open("data.txt", "r")
dataArray = file.read().split("\n")
arraySize = len(dataArray)
dataArray.remove(dataArray[arraySize-1])
# print(len(dataArray))
intList = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
somme = 0
for line in dataArray:
    lineList = [*line]
    # print(lineList)
    searchInt = []
    for character in lineList:
        if character in intList:
            searchInt.append(character)
    twoDigit = int(searchInt[0]+searchInt[len(searchInt)-1])
    somme += twoDigit

print(somme)
