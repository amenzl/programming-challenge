#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24, 2019

@author: anna
"""
import random as r

class DAG(object):

    def __init__(self, number_nodes, number_edges):
        self.total_nodes = number_nodes #create member variable to hold number of nodes
        self.total_edges = number_edges #create member variable to hold number of edges
        self.node_dict = {} #create member list of all node objects
        
        
        node_order_list=r.sample(range(number_nodes), number_edges)
        #Create dictionary of nodes with their order number
        dict(zip(total_nodes), node_order_list))

        #create nodes
        for i in range(self.total_nodes):
            
            node_order=node_order_list[i]
            max_dep_node=number_nodes-node_order
            num_dep_nodes=r.randint(range(max_dep_node),1)
            ##Subset node_order such that only nodes with higher order can be dependent nodes
            for j in range(num_dep_nodes):
                ##pick specified number of nodes with an order number higher than itself
                ## Add these nodes as list to node_dict for that node
            self.add_node(i) #here add node with its dependent nodes

        assert (node_dict.len() == self.total_nodes) #check all nodes created
            
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

