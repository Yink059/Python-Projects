import csv
import os

#change directory
os.chdir(r"C:\Users\bdsan\Documents\Imet data")
cwd = os.getcwd()

#create lists & dictionary

vDict = {
 "saveDateTime" : 0,
 "comTime": 1,
 "xqPressureRaw" : 36,
 "xqTempRaw" : 37,
 "xqHumidity" : 38,
 "xqHumidityTemp": 39,
 "xqLogDate" : 40,
 "xqLogTime" : 41,
 "xqLongitude" : 42,    # xxx.xxxx
 "xqLatitude" : 43,     # xxx.xxxx
 "xqAltitude" : 44,     #in meters
 "xqSatCount" : 45
 }



file = open("20210706-164825-00055359.csv", newline='')

rawList = file.readlines()

logData = []

for i in range(len(rawList)):
    logData += rawList[i].split(",")

    print((rawList[i].split(","))[vDict["xqLogTime"]]+ " "+ (rawList[i].split(","))[vDict["xqAltitude"]])
