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
        
        #Create a list with a randomly generated order number for nodes
        node_order_list=r.sample(range(number_nodes), number_edges)


        #create nodes
        for i in range(self.total_nodes):
            #Determine node order for current node
            node_order=node_order_list[i]
            #Determine maximum number of dependent nodes for this node
            max_dep_node=number_nodes-(node_order+1)
            #Add node 
            self.add_node(node_order)
            #Randomly determine how many dependent nodes current node will have
            num_dep_nodes=r.randint(0, max_dep_node)
            ##Subset node_order such that only nodes with higher order can be dependent nodes
            

            dep_node_pot=list(range(node_order+1, self.total_nodes))
            ## Randomly pick dependent nodes from list of potential dep nodes
            print('number of potential nodes: %i' % len(dep_node_pot))
            print('number of dependent nodes: %i' % num_dep_nodes)
            assert (len(dep_node_pot) >= num_dep_nodes)
            dep_nodes=r.sample(dep_node_pot, num_dep_nodes)
            

        assert (len(self.node_dict) == self.total_nodes) #check all nodes created
            
        #create edges
#        for j in range(self.total_edges):
            #TODO: need to ensure this is done acyclically; clever ordering/topology needed
#            self.add_edge()
    
    def add_node(self, name):
        self.node_dict.update({name:node(name)})
    
    def print_dep_nodes(self):
        #ITerat over node dictionary
        for key in self.node_dict.keys():
            print(key)
            for dep in self.node_dict.keys()[key].dep_node:
                print(self.node_dict.keys()[key].dep_node[dep])
#        print(node)
        #get dependent nodes and print them
    
    
#    def add_edge(self, node_one, node_two):
#    #TODO:
#        node_one.set_neighbor_upstream(node_two.name)
#        node_two.set_neighbor_downstream(node_one.name)


class node(object):
    
    def __init__(self, name):
        self.name = name
        self.dep_node = []
#        self.neighbor_downstream = None

    def set_dep_nodes(self, dep_name):
        self.dep_node.append(dep_name)

    def set_neighbor_downstream(self, neighbor_name):
        self.neighbor_downstream = neighbor_name

nodes = 20
edges = 20

g = DAG(nodes, edges)
g.print_dep_nodes()
