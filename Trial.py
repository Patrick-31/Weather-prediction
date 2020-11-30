#-------------------------------------------------------------------------------
# Name:        Trial
# Purpose:     - compute the smallest distance between temperature,
#                pressure and humidity during a period before
#                the day to predict and all periods in the data.
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
daytopredict = "20200607000000"    #it's 2020 june 07
periodTestWidth = 16               #period test length 8 for 1 day 16 for 2 days
#-------------------------------------

#found index of daytopredict
indexdaytopredict = 0
j = 0
for j, date in enumerate(townData):
    if date[1] == daytopredict :
        indexdaytopredict = j

#compute smallest distance from a period to previous period : smallestDistance
smallestDistance = 10000
indexdaythesame = 0
for indexdaytotest in range(periodTestWidth, indexdaytopredict-periodTestWidth, 8):
    try:   #for missing data
        distance = 0
        for j in range(periodTestWidth):
            jdistance = abs(float((townData[indexdaytotest - j])[7])-float((townData[indexdaytopredict - j])[7]))
            distance = distance + jdistance
        if distance < smallestDistance:
            smallestDistance = distance
            indexdaythesame = indexdaytotest
            print(indexdaythesame,(townData[indexdaythesame])[1], smallestDistance)
    except:
        continue

#test : is forescat temperature "good" ?
print("indexdaytopredict = ", indexdaytopredict, "day = ", (townData[indexdaytopredict])[1])
print("indexdaythesame = ", indexdaythesame, "day = ", (townData[indexdaythesame])[1])
print("smallest distance", smallestDistance)
predictionLength =  16   # 8 for 1 day, 16 for 2 days
print("For {} days  Pred Temp  Real Temp".format(predictionLength))

tmeanError = 0
missingData = 0
for j in range(predictionLength):
    try:
        print("at {:>3}h {:10.1f} {:10.1f} ".format(3*j,(float((townData[indexdaythesame + j])[7])-273.16),(float((townData[indexdaytopredict + j])[7])-273.16)))
        tmeanError = tmeanError + abs((float((townData[indexdaythesame + j])[7])-273.16) -(float((townData[indexdaytopredict + j])[7])-273.16))
    except:
        tmeanError = tmeanError
        missingData += 1
tmeanError = tmeanError/(predictionLength - missingData)
print("Absolute mean error = {:.2f} degre C".format(tmeanError))