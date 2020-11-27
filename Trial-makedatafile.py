#-------------------------------------------------------------------------------
# Name:        Trial-data filemaker
# Purpose:     - add month data in one file "synop.csv"
#              - keep just one town and write in the file "synop-town.csv"
#
# Author:      Patrick
#
# Created:     25/11/2020
# Copyright:   (c) Patrick 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#read a data file and put data in a string : oneStringData
file = open("E:/synop.202001.csv", "r")
oneStringData = file.read()
file.close()
file = open("E:/synop.csv", "w")
file.write(oneStringData)
file.close()

file = open("E:/synop.202002.csv", "r")
stringData = file.read()
file.close()
file = open("E:/synop.csv", "a")
file.write(stringData)
file.close()

file = open("E:/synop.202003.csv", "r")
stringData = file.read()
file.close()
file = open("E:/synop.csv", "a")
file.write(stringData)
file.close()

file = open("E:/synop.202004.csv", "r")
stringData = file.read()
file.close()
file = open("E:/synop.csv", "a")
file.write(stringData)
file.close()

file = open("E:/synop.202005.csv", "r")
stringData = file.read()
file.close()
file = open("E:/synop.csv", "a")
file.write(stringData)
file.close()

file = open("E:/synop.202006.csv", "r")
stringData = file.read()
file.close()
file = open("E:/synop.csv", "a")
file.write(stringData)
file.close()

file = open("E:/synop.202007.csv", "r")
stringData = file.read()
file.close()
file = open("E:/synop.csv", "a")
file.write(stringData)
file.close()

file = open("E:/synop.202008.csv", "r")
stringData = file.read()
file.close()
file = open("E:/synop.csv", "a")
file.write(stringData)
file.close()

file = open("E:/synop.202009.csv", "r")
stringData = file.read()
file.close()
file = open("E:/synop.csv", "a")
file.write(stringData)
file.close()

file = open("E:/synop.202010.csv", "r")
stringData = file.read()
file.close()
file = open("E:/synop.csv", "a")
file.write(stringData)
file.close()

#read a data file and put data in a string : oneStringData
file = open("E:/synop.csv", "r")
oneStringData = file.read()
file.close()

#split string in list of lines : franceData
franceDataList = oneStringData.split("\n")

#erase lists without stationnumber start : townData; Here 07630 for Toulouse-Blagnac
stationNumber = "07630"
townDataList = list()
for i in franceDataList:
    if i[:5] == stationNumber:
        townDataList.append(i)
print(townDataList)

#make a string with list of town data
townDataText="\n".join(townDataList)
print(townDataText)

#write data to synop-town.csv
try:
    file = open("E:/synop-town.csv", "w")
    file.write(townDataText)
    file.close()
except:
    print("error")

print("End")