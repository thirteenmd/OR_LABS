# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 09:38:40 2017

@author: Andreea
"""

import networkx as nx
#import datetime
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
        for t in range(len(stations[i][j])):
            stations[i][j][t] = stations[i][j][t][:-1]
#we delete the first coloumn of the timetable (the number of the troleybus) and the comas

print(stations[0])





"""
#ADD EDGES THAT PASS TROUGH TE NODES (TROLEYBUSES THAT PASS TROUGH THE STATION)
n = G.nodes()
t_dict = {}

for i in range(len(n)):
    troleybuses = []
    
    file_name = n[i]+".txt"
    f = open(file_name,"r")
    
    lines = list(f)
    
    for line in lines:
        m = 0
        number = ""
        
        while(line[m] != ")"):
            number = number + line[m]
            m = m + 1
        
        troleybuses.append(number)
    #makes the list of troleybuses tat pass through the station
        
    t_dict[n[i]] = troleybuses
    

for item in t_dict:
    print(item,"   ",t_dict[item])
"""
