import pandas as p
import re

with open('day-1\input.txt') as f:
    lines = f.readlines()

# list = []
# concatList = []
# sum =0
# for line in lines:
#     list.append(re.findall("[0-9]",line))

# for i in range(0,1000):
#     concatList.append(list[i][0] + list[i][-1])
#     sum += int(concatList[i])
# P2
list = []
concatList = []
replaceList=[]
sum =0

numbersToReplace = {"one": "1","two": "2","three": "3","four": "4","five": "5","six": "6","seven": "7","eight": "8","nine": "9"}
span = []
index= 0

for key in numbersToReplace.keys():
    index= 0
    charToReplace = numbersToReplace[key]
    for line in lines:
        index += 1
        if key in line:
            search = re.search(key, line)
            span.append([index, charToReplace, search.span()[0], search.span()[1]])


for i in range(len(lines)):
    for j in range(len(span)):
        if span[j][0] == i + 1 :
            newLine = line[:span[j][2]] + "" +str(span[j][1])+ "" + line[span[j][2]:]
            print(newLine)
        
    # print(newLine)
# for i in range(len(span)):
#     replaceList.append(line[:span[i][2]] + " " + line[span[i][2]:])

# print(replaceList)

# for line in lines:
    
#     list.append(re.findall("[0-9]", line))

# for i in range(0,1000):
#     concatList.append(list[i][0] + list[i][-1])
#     sum += int(concatList[i])
# print(sum)
