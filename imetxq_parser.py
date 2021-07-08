import csv
import os
import math

#change directory
os.chdir(r"C:\Users\bdsan\Documents\Imet data")
cwd = os.getcwd()

#create lists & dictionary
rawData = []
logEntry = 0
vD = { #value dictionary for indices, values labeled xq are pre-trimmed csv indices
 "saveDateTime" : 0,            #date+time when data was written to csv
 "comTime": "Not Applicable",   #the write time of the data to the csv
 "logEntryNumber": 1,
 "Pressure": 2,
 "temp": 3,
 "humidity": 4,
 "humidityTemp": 5,
 "logDate": 6,
 "logTime": 7,
 "longitude": 8,
 "latitude": 9,
 "altitude": 10,
 "satCount": 11,
 "xqPressureRaw" : 36,  #Air Pressure in mm Hg (Torr)splitList[i][vD["altitude"]]
 "xqTempRaw" : 37,      #Air temp in centigrade
 "xqHumidity" : 38,     #Relative Humidity
 "xqHumidityTemp": 39,  #no clue
 "xqLogDate" : 40,      #log date in format YYYY/MM/DD
 "xqLogTime" : 41,      #log time in HH:MM:SS (Zulu)
 "xqLongitude" : 42,    # xxx.xxxxxx
 "xqLatitude" : 43,     # xxx.xxxxxx
 "xqAltitude" : 44,     #in meters
 "xqSatCount" : 45      # number of connected GPS sats
 }
dictValues = [i + 2 for i in range(10)]
numValues = [1,2,3,4,5,8,9,10,11]

#open raw csv file and read it
file = open("20210708-test.csv", newline='\n')
rawList = file.readlines()
splitList = []
#print(len(rawList))

for i in range(len(rawList)): #split raw csv into individual lines
    splitList += rawList[i].split("', '")
del splitList[0] #delete csv definition line

for i in range(len(splitList)): #split each line into individual lists for each data number
    splitList[i] = splitList[i].split(",")
    del splitList[i][2:36] #delete the empty values

    splitList[i][1] = logEntry
    logEntry += 1


    for n in numValues: #convert specific strings to floats
        continue
        splitList[i][n] = float(splitList[i][n])
    splitList[i][vD["altitude"]] = math.floor(float(splitList[i][vD["altitude"]])) #altitude converted to integer


    for x in dictValues: #print logged values minus upload date/time
        print(splitList[i][x], end='  ')
    print()
