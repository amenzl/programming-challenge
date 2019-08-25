#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24, 2019

@author: anna
"""

from DAG import DAG
import copy as c
import pandas as pd

nodes = 5
nodes = 20
edges = 20


g = DAG(nodes, edges)
#g.print_dep_nodes()
#g.print_parents()
list_data=[]
for i in range(1000):
    list_data.append(c.deepcopy(g.return_node_value_dict()))
#print(list_data)

data = {}
for d in list_data:
    for k, v in d.items():  # d.items() in Python 3+
        data.setdefault(k, []).append(v)

print(pd.DataFrame.from_dict(data))
#print(data)
