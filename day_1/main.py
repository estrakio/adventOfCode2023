import re
file = open("data.txt", "r")
dataArray = file.read().split("\n")
arraySize = len(dataArray)
dataArray.remove(dataArray[arraySize-1])
# print(len(dataArray))

# FIRST STAR
# intList = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# result = 0
# for line in dataArray:
#     lineList = [*line]
#     # print(lineList)
#     searchInt = []
pattern = re.compile("(one|two|three|four|five|six|seven|eight|nine|1|2|3|4|5|6|7|8|9)")
stringArray = {
    "oneight": ["1", "8"],
    "twone": ["2", "1"],
    "threeight": ["3", "8"],
    "fiveight": ["5", "8"],
    "sevenine": ["7", "9"],
    "eightwo": ["8", "2"],
    "eighthree": ["8", "3"],
    "nineight": ["9", "8"],
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"

}
somme = 0
for line in dataArray:
    foundList = pattern.findall(line)
    # print(len(foundList))
    # print(foundList)
    # print(line)
    first = foundList[0]
    second = foundList[len(foundList) - 1]
    if first in stringArray:
        first = stringArray[first]
    if second in stringArray:
        second = stringArray[second]
    value = int(first + second)
    somme += value

print(somme)
