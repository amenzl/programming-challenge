#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24, 2019

@author: anna
"""

from DAG import DAG
import copy as c
import pandas as pd
import random as r
import time

total_nodes = 5
total_edges = 5


g = DAG(total_nodes, total_edges)

g.print_dep_nodes()
g.print_parents()
t=g.select_target()

# print(g.find_path(1,4))

list_data=[]
for i in range(1000):
    list_data.append(c.deepcopy(g.return_node_value_dict()))
#print(list_data)

data = {}
for d in list_data:
    for k, v in d.items(): 
        data.setdefault(k, []).append(v)

df=pd.DataFrame.from_dict(data)
#Select a random target
nodes=sorted(g.node_dict.keys())
target=r.randint(0, len(nodes))
df=df.rename(columns={target: "Target"})




export_csv = df.to_csv(r'first_rand_df.csv', index = None, header=True)

for j in range(100):
    g = DAG(total_nodes, total_edges)
    loop_time = time.time()
    print(j)
    list_data=[]
    graph_time = time.time()
    for i in range(1000):
        list_data.append(c.deepcopy(g.return_node_value_dict()))
#print(list_data)
#print(pd.DataFrame(list_data))
    print("took {} s to run graph".format(time.time()-graph_time))
    df_time = time.time()
    df=pd.DataFrame.from_dict(list_data)
    #Select a random target
    nodes=sorted(g.node_dict.keys())
    target=g.select_target()
    print(target)
    df=df.rename(columns={target: "Target"})
#    print(df)
    print("took {} s to create df".format(time.time()-df_time))

    export_time = time.time()
    export_csv = df.to_csv(r'rand_df'+str(j)+'.csv', index = None, header=True)
    print("took {} to export".format(time.time()-export_time))

    print("took {} s total".format(time.time()-loop_time))
    

    

"""





