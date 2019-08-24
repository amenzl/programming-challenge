#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24, 2019

@author: anna
"""

class DAG(object):

    def __init__(self, number_nodes, number_edges):
        self.total_nodes = number_nodes #create member variable to hold number of nodes
        self.total_edges = number_edges #create member variable to hold number of edges
        self.node_list =[] #create member list of all node objects
        
        #create nodes
        for i in range(self.total_nodes):
            self.add_node(i)

        assert (node_list.len() == self.total_nodes) #check all nodes created
            
        #create edges
        for j in range(self.total_edges):
            #TODO: need to ensure this is done acyclically; clever ordering/topology needed
            self.add_edge()
    
    def add_node(self, name):
        add_node.append(node(name))
    
    def add_edge(self, node_one, node_two):
    #TODO:
        node_one.set_neighbor_upstream(node_two.name)
        node_two.set_neighbor_downstream(node_one.name)


class node(object):
    
    def __init__(self, name):
        self.name = name
        self.neighbor_upstream = None
        self.neighbor_downstream = None

    def set_neighbor_upstream(self, neighbor_name):
        self.neighbor_upstream = neighbor_name

    def set_neighbor_downstream(self, neighbor_name):
        self.neighbor_downstream = neighbor_name

