# Weather-prediction
Building AI course project

# Project Title

Final project for the Building AI course

## Summary

Predict temperature for the next day.


## Background

When i was young weather predictions are made with local informations : temperature, wind, pressure...and the memory of the same arrangement.
"When the sun is red at nightfall, no clouds the next day..."
The idea of this project is to found period with "identicals temperatures" of the previous days before the day to predict.
If predictions are not too bad...we'll accord some credits to ancients weather's men.


## How is it used?
This project can be used by person who have a connected thermometer. 
Evry 3 hours temperature is added to data, compute nearest temperature period and predict next day temperature.

Here is the code to isolate data from my town for year 2020
```
-------------------------------------------------------------------------------
Name:        Trial-data filemaker
Purpose:     - add month data in one file "synop.csv"
              - keep just one town and write in the file "synop-town.csv"
 Author:      Patrick

 Created:     25/11/2020
 Copyright:   (c) Patrick 2020
 Licence:     <your licence>
-------------------------------------------------------------------------------

read a data file and put data in a string : oneStringData
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
```

Here is the code to test...
```
-------------------------------------------------------------------------------
 Name:        Trial
 Purpose:     - compute the smallest distance between temperature during a period
                before the day to predict and all periods in the data.
              - temperature during day to predict are "the same.." as the day
                after the "smallest distance period" in the data.
              - with datas we can verify predictions

 Author:      Patrick

 Created:     25/11/2020
 Copyright:   (c) Patrick 2020
 Licence:     <your licence>
-------------------------------------------------------------------------------
read a data file and put data in a string : oneStringData
file = open("E:/synop-town.csv", "r")
oneStringData = file.read()
file.close()

split string in list of lines : townDataList
townDataList = oneStringData.split("\n")

split lines in list of data
townData = list()
for i in townDataList:
    townData.append(i.split(";"))

-------------------------------------
day to predict and period test width
daytopredict = "20200926000000"     #it's 2020 september 26
periodTestWidth = 24                #8 data for 1 day, 16 for 2 days, 24 for 3 days ...
-------------------------------------

found index of daytopredict
indexdaytopredict = 0
j = 0
for j, date in enumerate(townData):
    if date[1] == daytopredict :
        indexdaytopredict = j

compute smallest distance from a period to previous period : smallestDistance
distance on temperature only...for now
smallestDistance = 10000
indexdaythesame = 0
for indexdaytotest in range(periodTestWidth, indexdaytopredict-periodTestWidth, periodTestWidth):
    try:
        distance = 0
        for j in range(periodTestWidth):
            jdistance = abs(float((townData[indexdaytotest - j])[7])-float((townData[indexdaytopredict - j])[7]))
            distance = distance + jdistance
        if distance < smallestDistance:
            smallestDistance = distance
            indexdaythesame = indexdaytotest
    except:
        continue

test : is forescat temperature "good" ?
print("#diplay temperature during periodTestWidth befor day to predict")
print("indexdaytopredict = ", indexdaytopredict, "day = ", (townData[indexdaytopredict])[1])
for j in range(periodTestWidth):
    print("temperature atÂ  ",3*j, "h = ", (float((townData[indexdaytopredict - periodTestWidth + j])[7])-273.16))

print("#display temperature during periodTestWidth befor day the same")
print("indexdaythesame = ", indexdaythesame, "day = ", (townData[indexdaythesame])[1])
print("smallest distance", smallestDistance)
for j in range(periodTestWidth):
    print("temperature atÂ  ",3*j, "h = ", (float((townData[indexdaythesame - periodTestWidth + j])[7])-273.16))

print("#Display real temperature during daytopredict")
print("indexdaytopredict = ", indexdaytopredict, "day = ", (townData[indexdaytopredict])[1])
for j in range(8):
    print("temperature atÂ  ",3*j, "h = ", (float((townData[indexdaytopredict - periodTestWidth + j])[7])-273.16))

print("#display temperature of the day the same")
print("indexdaythesame = ",indexdaythesame, "day = ", (townData[indexdaythesame])[1])
for j in range(8):
    print("temperature atÂ  ",3*j, "h = ", (float((townData[indexdaythesame - periodTestWidth + j])[7])-273.16))
```

## Data sources and AI methods

Datas used are given by French "météo France" at : "donneespubliques.meteofrance.fr"
https://donneespubliques.meteofrance.fr/?fond=produit&id_produit=90&id_rubrique=32
Files contain 40 weather parameters measured evry 3 hours from 1996 to 2020.
Nearest neighborg method is used to found the nearest period of temperatures.
Distance is calculate with temperatures differences only.

## Challenges

With only temperature parameter... predictions will be "predictions".

## What next?
Pressure, wind direction can be added to improve the model.



## Acknowledgments

Data from "météo France" are public. Evrybody can use it.
