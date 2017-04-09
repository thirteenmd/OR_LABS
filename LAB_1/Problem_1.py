# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 09:38:40 2017

@author: Andreea
"""

import datetime

#for the first problem we will analyse only the data from 3 stations

stationsName = ['stefan_cel_mare','asem','circul']
n = len(stationsName)
stations = []

for i in range(n): 
    with open(stationsName[i]+".txt") as dataFile:
        stations.append([line.split() for line in dataFile])
#we load the timetables of each station intro the list "stations"

for i in range(len(stations)):
    for j in range(len(stations[i])):
        stations[i][j].reverse()
        stations[i][j].pop()
        stations[i][j].reverse()
        for t in range(len(stations[i][j])-1):
            stations[i][j][t] = stations[i][j][t][:-1]
#we delete the first coloumn of the timetable (the number of the trolleybus) and the comas

scm = [] #stefam cel mare station
asem = [] #asem station
circul = [] #circul station

increment = datetime.timedelta(seconds = 60) #variable will be used to increment the time, used for shifting the arrival time
timeDifference = datetime.timedelta(seconds = 180) #variable used to preserve the time difference between stationss

def appendStation(i, station):
    temp = stations[i]
    for i in range(len(temp)):
        line = []
        for j in range(len(temp[i])):
            line.append(datetime.datetime.strptime(temp[i][j], '%H:%M').time())
        station.append(line)

appendStation(0, scm)
appendStation(1, asem)
appendStation(2, circul)
    
def findSameTime(station, t1, t2):
    return set(station[t1]).intersection(station[t2])
    #function returns the arrival times of trolleybuses t1 and t2 that coincide 

def shift(timetable):
    for i in range(len(timetable)):
        timetable[i] = (datetime.datetime.combine(datetime.date(1,1,1),timetable[i]) + increment).time()
#function that does the time shifting on a troleybus line

def shiftTrolleybus(station, t1, t2):
    if(station[t1][0] < station[t2][0]):
        shift(station[t2])
    else:
        shift(station[t1])
#function that decides which trolleybus line to shift when there are 2 coinciding times

def allignStationsForward(stationOk, stationToAllign):
    for i in range(len(stationOk)):
        for j in range(len(stationOk[i])):
            newTime = (datetime.datetime.combine(datetime.date(1,1,1),stationOk[i][j]) + timeDifference).time()
            stationToAllign[i][j] = newTime
#function to change the arrival time of one station according to the arrival time to the other station by adding the time difference


"""
def allignStationsBackward(stationOk, stationToAllign):
    timeDifference = datetime.timedelta(seconds = -180)
    for i in range(stationOk):
        for j in range(stationOk[i]):
            newTime = (datetime.datetime.combine(datetime.date(1,1,1),stationOk[i][j]) + timeDifference).time()
            stationToAllign[i][j] = newTime
#function to change the arrival time of one station according to the arrival time to the other station by substracting the time difference to be used in Problem2

"""
def printStation(station):
    for i in range(len(station)):
        trolleybusLine = []
        for j in range(len(station[i])):
            trolleybusLine.append(str(station[i][j]))
        print(trolleybusLine)
#fuction to display tha timetable of the station

print("Stefan cel mare station before shifting:")
printStation(scm)

for z in range(2):
    for i in range(len(scm)):
        for j in range(len(scm)): #we verify every possible pair of trolleybuses which arrival time may collide
            if(j != i):
                #print("Cheking lines ", i," and ",j)
                intersect = findSameTime(scm, i, j)
                #print("Intersection is ",intersect)
                while(len(intersect) > 0):
                    """                    
                    print("Found same arrival times in station's timetable, lines", i, " and ", j,":")
                    print(intersect)
                    print("Station timetable before shifting:")
                    printStation(scm)
                    """
                    shiftTrolleybus(scm, i, j)
                    """
                    print("Station timetable after shifting:")
                    printStation(scm)
                    """
                    intersect = findSameTime(scm, i, j)

print("Stefan cel mare station after shifting:")
printStation(scm)

print("ASEM station before shifting:")
printStation(asem)

print("ASEM station after shifting:")
allignStationsForward(scm, asem)
printStation(asem)

print("Circul station before shifting:")
printStation(circul)

print("Circul station after shifting:")
allignStationsForward(asem, circul)
printStation(circul)











