from encodings import utf_8
from operator import contains
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

def jsonWork(english, russian):
    #перевірка файлів
    if sum(1 for line in english) == sum(1 for line in russian):
        result = []

        #заповнення словника
        i = 0
        for engLine in english:
            tempList = [english[i], russian[i]]
            result.append(tempList)
            i = i + 1

        #резервне збереження існуючих данних з data.json
        tempData = 0
        if os.path.getsize("data.json") != 0:
            with open('data.json', encoding='utf-8') as data:
                tempData = json.load(data)

        #загрузка отриманих даних в data.json.
        with open('data.json', 'w', encoding='utf-8') as data:
            if tempData == 0:
                json.dump(result, data, ensure_ascii=False, indent=4)
            else:
                for line in tempData:
                    result.append(line)
                json.dump(result, data, ensure_ascii=False, indent=4)
    return ""

#finalRussian = cuting(russian)
#finalEnglish = cuting(english)
#jsonWork(finalEnglish, finalRussian)

with open('data.json', encoding='utf-8') as data:
    data = json.load(data)
    
    for line in english:
        if line != "":
            for dictLine in data:
                if dictLine[0] != "" and dictLine[0] in line:
                    result = line.replace(dictLine[0], dictLine[1])
                    print(result)
                    break

english.close
russian.close