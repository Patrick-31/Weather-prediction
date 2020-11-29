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
daytopredict = "20200714000000"    #it's 2020 march 07
periodTestWidth = 2               #period test length in day
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
tcoefficient = 1
pcoefficient = 0.0001
hcoefficient = 0
for indexdaytotest in range(periodTestWidth*8, indexdaytopredict-periodTestWidth, periodTestWidth):
    try:
        distance = 0
        for j in range(periodTestWidth*8):
            jdistance = abs(float((townData[indexdaytotest - j])[7])-float((townData[indexdaytopredict - j])[7]))*tcoefficient + abs(float((townData[indexdaytotest - j])[20])-float((townData[indexdaytopredict - j])[9]))*pcoefficient + abs(float((townData[indexdaytotest - j])[20])-float((townData[indexdaytopredict - j])[9]))*hcoefficient
            distance = distance + jdistance
        if distance < smallestDistance:
            smallestDistance = distance
            indexdaythesame = indexdaytotest
    except:
        continue

#test : is forescat temperature "good" ?
print("indexdaytopredict = ", indexdaytopredict, "day = ", (townData[indexdaytopredict])[1])
print("indexdaythesame = ", indexdaythesame, "day = ", (townData[indexdaythesame])[1])
print("smallest distance", smallestDistance)
predictionLength =  3
print("For {} days  Pred T°C   Real T°C   Pred %H    Real %H    Pred Rmm    Real Rmm".format(predictionLength))

tmeanError = 0
hmeanError = 0
missingData = 0
for j in range(predictionLength * 8):
    try:
        print("at {:>3}h {:10.1f} {:10.1f} {:10.1f} {:10.1f} {:10.1f} {:10.1f} ".format(3*j,(float((townData[indexdaythesame - periodTestWidth*8 + j])[7])-273.16),(float((townData[indexdaytopredict - periodTestWidth*8 + j])[7])-273.16), (float((townData[indexdaythesame - periodTestWidth*8 + j])[9])), (float((townData[indexdaytopredict - periodTestWidth*8 + j])[9])), (float((townData[indexdaythesame - periodTestWidth*8 + j])[31])), (float((townData[indexdaytopredict - periodTestWidth*8 + j])[31]))))
        tmeanError = tmeanError + abs((float((townData[indexdaythesame - periodTestWidth*8 + j])[7])-273.16) -(float((townData[indexdaytopredict - periodTestWidth*8 + j])[7])-273.16))
        hmeanError = hmeanError + abs((float((townData[indexdaythesame - periodTestWidth*8 + j])[9])) -(float((townData[indexdaytopredict - periodTestWidth*8 + j])[9])))
    except:
        tmeanError = tmeanError
        hmeanError = hmeanError
        missingData += 1
tmeanError = tmeanError/(8 * predictionLength - missingData)
hmeanError = hmeanError/(8 * predictionLength - missingData)
print("Absolute mean error = {:.2f}°C  {:.1f}%H".format(tmeanError, hmeanError))