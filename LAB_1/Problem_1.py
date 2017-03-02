# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 09:38:40 2017

@author: Andreea
"""

import networkx as nx
G = nx.Graph()

#ADD NODES TO THE GRAPH (STATIONS)
#for the first problem we will analyse only the data from 3 stations

G.add_node("asem")
#G.add_node("casa_presei")
#G.add_node("central_typography")
G.add_node("circul")
#G.add_node("eminescu")
#G.add_node("kiev")
#G.add_node("kogalniceanu")
#G.add_node("licurici")
#G.add_node("mihai_eminescu_theatre")
#G.add_node("puskin")
G.add_node("stefan_cel_mare")
#G.add_node("vladimirescu")

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



