#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24, 2019

@author: anna
"""

from DAG import DAG

nodes = 5
edges = 9


g = DAG(nodes, edges)
g.print_dep_nodes()
g.print_parents()
