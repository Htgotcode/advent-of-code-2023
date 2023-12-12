import pandas as p
import re

with open('day-1\input-paige.txt') as f:
    lines = f.readlines()

list = []
concatList = []
sum =0
for line in lines:
    list.append(re.findall("[0-9]",line))

for i in range(0,1000):
    concatList.append(list[i][0] + list[i][-1])
    sum += int(concatList[i])
# P2
list = []
concatList = []
sum =0

for line in lines:
    line = re.findall()
    #line = re.sub("one", "1", line)
    #line = re.sub("two", "2", line)
    #line = re.sub("three", "3", line)
    #line = re.sub("four", "4", line)
    #line = re.sub("five", "5", line)
    #line = re.sub("six", "6", line)
    #line = re.sub("seven", "7", line)
    #line = re.sub("eight", "8", line)
    #line = re.sub("nine","9", line)
    #list.append(re.findall("[0-9]", line))

for i in range(0,1000):
    concatList.append(list[i][0] + list[i][-1])
    sum += int(concatList[i])
print(sum)

# one,two,three,four,five,six,seven,eight,nine
