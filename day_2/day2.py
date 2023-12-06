file = open("data.txt", "r")
dataArray = file.read().split("\n")
arraySize = len(dataArray)
dataArray.remove(dataArray[arraySize - 1])


# Part 1
def isPossible(red, green, blue):
    maxRed = 12
    maxGreen = 13
    maxBlue = 14
    if maxRed >= red and maxGreen >= green and maxBlue >= blue:
        return True
    else:
        return False

somme = 0
for line in dataArray:
    # Séparer l'id de la  partie du reste:
    id = line.split(":")[0].split(" ")[1]

    # Séparer les parties dans une liste :
    roundList = line.split(":")[1].split(";")
    blue, red, green = 0, 0, 0

    # Séparer les couleurs entres elles :
    for round in roundList:
        round = round.strip()
        colorList = round.split(" ")
        print(colorList)
        for i in range(len(colorList)):

            # Récupèrer la valeur de chaque couleur :
            if colorList[i] == "red" and int(colorList[i - 1]) > red:
                    red = int(colorList[i - 1])
            elif colorList[i] == "green" and int(colorList[i - 1]) > green:
                    green = int(colorList[i - 1])
            elif colorList[i] == "blue" and int(colorList[i - 1]) > blue:
                    blue = int(colorList[i - 1])


    # Vérifier si la partie est possible :
    if isPossible(red, green, blue):
        somme += int(id)
print(somme)
