from encodings import utf_8
from queue import Empty
import string
import json
import os

english = open('putEnglishHere.txt', 'r', encoding="utf_8")
russian = open('russian.txt', 'r', encoding="utf_8")

emojis = [':SCN1: ', ':SCN2: ', ':SCN3: ', ':SCN4: ', ':SCN5: ', ':SCN6: ', '<:SCN1:769757680335192065> ', '<:SCN2:769757680327196692> ', '<:SCN3:769757680285515807> ', '<:SCN4:769757680423796756> ', '<:SCN5:769757680435724308> ', '<:SCN6:769757680360357898> ', '\n', ' :SC:', ' :SQ:', "]"]

def cuting(file):
    cutedText = []
    for line in file:
        for emoji in emojis:
            line = line.replace(emoji, "")
        lineList = line.split(" [")
        cutedText.append(lineList[0])
    return cutedText

finalRussian = cuting(russian)
finalEnglish = cuting(english)

result = []

i = 0
for engLine in finalEnglish:
    tempList = [finalEnglish[i], finalRussian[i]]
    result.append(tempList)
    i = i + 1

tempData = 0
if os.path.getsize("data.json") != 0:
    with open('data.json', encoding='utf-8') as data:
        tempData = json.load(data)

with open('data.json', 'w', encoding='utf-8') as data:
    if tempData == 0:
        json.dump(result, data, ensure_ascii=False, indent=4)
    else:
        for line in tempData:
            result.append(line)
        json.dump(result, data, ensure_ascii=False, indent=4)



english.close
russian.close