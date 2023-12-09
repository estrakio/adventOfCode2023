file = open("data.txt", "r")
dataArray = file.read().split("\n")
arraySize = len(dataArray)
dataArray.remove(dataArray[arraySize - 1])

# Part 2
res = 0
gameMaxValues = []
for line in dataArray:
    # Séparer les parties dans une liste :
    roundList = line.split(":")[1].split(";")
    blue = 0
    red = 0
    green = 0
    # Séparer les couleurs entres elles :
    for round in roundList:
        round = round.strip()
        colorList = round.split(" ")
        # print(colorList)
        for i in range(len(colorList)):
            colorList[i] = colorList[i].strip(',')
            # Récupèrer la valeur de chaque couleur :
            if colorList[i] == "red" and int(colorList[i - 1]) > red:
                red = int(colorList[i - 1])
            elif colorList[i] == "green" and int(colorList[i - 1]) > green:
                green = int(colorList[i - 1])
            elif colorList[i] == "blue" and int(colorList[i - 1]) > blue:
                blue = int(colorList[i - 1])
    gameMaxValues.append(int(red) * int(green) * int(blue))
res += sum(gameMaxValues)


print(res)
