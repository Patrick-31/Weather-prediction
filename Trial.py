#-------------------------------------------------------------------------------
# Name:        Trial
# Purpose:     - compute the smallest distance between temperature during a period
#                before the day to predict and all periods in the data.
#              - temperature during day to predict are "the same.." as the day
#                after the "smallest distance period" in the data.
#              - with datas we can verify predictions
#
# Author:      Patrick
#
# Created:     25/11/2020
# Copyright:   (c) Patrick 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#read a data file and put data in a string : oneStringData
file = open("E:/synop-town.csv", "r")
oneStringData = file.read()
file.close()

#split string in list of lines : townDataList
townDataList = oneStringData.split("\n")

#split lines in list of data
townData = list()
for i in townDataList:
    townData.append(i.split(";"))

#-------------------------------------
#day to predict and period test width
daytopredict = "20200926000000"    #it's 2020 september 26
periodTestWidth = 24                #distance for 8 data for 1 day, 16 for 2 days...
#-------------------------------------

#found index of daytopredict
indexdaytopredict = 0
j = 0
for j, date in enumerate(townData):
    if date[1] == daytopredict :
        indexdaytopredict = j

#compute smallest distance from a period to previous period : smallestDistance
#distance on temperature only...for now
smallestDistance = 10000
indexdaythesame = 0
for indexdaytotest in range(periodTestWidth, indexdaytopredict-periodTestWidth, periodTestWidth):
    try:
        distance = 0
        for j in range(periodTestWidth):
            jdistance = abs(float((townData[indexdaytotest - j])[7])-float((townData[indexdaytopredict - j])[7]))
            distance = distance + jdistance
#        print(distance)
        if distance < smallestDistance:
            smallestDistance = distance
            indexdaythesame = indexdaytotest
    except:
#        print("continue")
        continue

#test : is forescat temperature "good" ?
print("#diplay temperature during periodTestWidth befor day to predict")
print("indexdaytopredict = ", indexdaytopredict, "day = ", (townData[indexdaytopredict])[1])
for j in range(periodTestWidth):
    print("temperature atÂ  ",3*j, "h = ", (float((townData[indexdaytopredict - periodTestWidth + j])[7])-273.16))

print("#display temperature during periodTestWidth befor day the same")
print("indexdaythesame = ", indexdaythesame, "day = ", (townData[indexdaythesame])[1])
print("smallest distance", smallestDistance)
for j in range(periodTestWidth):
    print("temperature atÂ  ",3*j, "h = ", (float((townData[indexdaythesame - periodTestWidth + j])[7])-273.16))

#print("#Display real temperature during daytopredict")
print("indexdaytopredict = ", indexdaytopredict, "day = ", (townData[indexdaytopredict])[1])
for j in range(8):
    print("temperature atÂ  ",3*j, "h = ", (float((townData[indexdaytopredict - periodTestWidth + j])[7])-273.16))

print("#display temperature of the day the same")
print("indexdaythesame = ",indexdaythesame, "day = ", (townData[indexdaythesame])[1])
for j in range(8):
    print("temperature atÂ  ",3*j, "h = ", (float((townData[indexdaythesame - periodTestWidth + j])[7])-273.16))
