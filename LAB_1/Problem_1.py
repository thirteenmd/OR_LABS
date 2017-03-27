# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 09:38:40 2017

@author: Andreea
"""

import networkx as nx
import datetime
G = nx.Graph()

#ADD NODES TO THE GRAPH (STATIONS)
#for the first problem we will analyse only the data from 3 stations

stationsName = ['stefan_cel_mare','asem','circul']
G.add_nodes_from(stationsName)
n = G.nodes()
stations = []

for i in range(len(n)): 
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

#we analyse the first station - stefan cel mare
temp = stations[0]

scm = [] #stefam cel mare station
increment = datetime.timedelta(seconds = 60) #variable will be used to increment the time
time_difference = datetime.timedelta(seconds = 180) #variable used to preserve the time difference between stationss

for i in range(len(temp)):
    line = []
    for j in range(len(temp[i])):
        line.append(datetime.datetime.strptime(temp[i][j], '%H:%M').time())
    scm.append(line)

"""
print()
print()
for i in range(len(scm)):
    line = []
    for j in range(len(scm[i])):
        print((datetime.datetime.combine(datetime.date(1,1,1),scm[i][j]) + increment).time())
"""

def findSameTime(station, t1, t2):
    return set(station[t1]).intersection(station[t2])
    #function returns the arrival times of trolleybuses t1 and t2 that coincide 




















