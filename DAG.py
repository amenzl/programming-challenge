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
        self.actual_edges = 0
        
        assert (number_edges >= (number_nodes-1)) #check this is a possible graph
        
        #Create a list with a randomly generated order number for nodes
        node_order_list = r.sample(range(number_nodes), number_nodes)
        
        #create nodes
        actual_edges=0
        for i in range(self.total_nodes):
            #Determine node order for current node
            node_order=node_order_list[i]
            #Add node 
            self.add_node(node_order)
            #Randomly determine how many dependent nodes current node will have
            if node_order < (number_nodes-1):
                #Determine maximum number of dependent nodes for this node
                max_dep_node=number_nodes-(node_order+1)
                
                num_dep_nodes = r.randint(1, max_dep_node)
            else: 
                num_dep_nodes = 0
            

            dep_node_pot = list(range(node_order+1, self.total_nodes))
            
            ## Randomly pick dependent nodes from list of potential dep nodes
            print('name of node: %i' %node_order)
            print('number of potential nodes: %i' % len(dep_node_pot))
            print('number of dependent nodes: %i' % num_dep_nodes)
            assert (len(dep_node_pot) >= num_dep_nodes)
            
            dep_nodes = r.sample(dep_node_pot, num_dep_nodes)

            ## Randomly pick dependent nodes from list of potential dep nodes
            if num_dep_nodes>0:
                dep_nodes = r.sample(dep_node_pot, num_dep_nodes)
                #Add dependent nodes to list of dep of node object
                for j in range(num_dep_nodes):
                    self.node_dict[node_order].set_dep_nodes(dep_nodes[j])
                    actual_edges += num_dep_nodes
                    print('Number of edges %i' %actual_edges)
                    
            else:
                self.node_dict[node_order].dep_node=[]

        assert (len(self.node_dict) == self.total_nodes) #check all nodes created
        
        open_nodes=[]
        while number_edges > actual_edges:
            for key in self.node_dict.keys():
                #check which nodes have less dependents than potential dependents
                if len(self.node_dict[key].dep_node) < number_nodes-(key+1):
                    #Add all those nodes to a list
                    open_nodes.append(key)
                     # Pick a random entry from that list
            sel_node = r.randint(1, len(open_nodes)+1)
            print("open nodes %i" %open_nodes[sel_node])
                    
            
            
#            and add a node
            
#            add a dependent
#        if number_edge<= actual_edges:
#                remove a dependent
            
        #create edges
#        for j in range(self.total_edges):
            #TODO: need to ensure this is done acyclically; clever ordering/topology needed
#            self.add_edge()
    
    def add_node(self, name):
        self.node_dict.update({name:node(name)})
    
    def print_dep_nodes(self):
        #ITerat over node dictionary
        for key in self.node_dict.keys():
            print('Name of node: %i' %key)
            if len(self.node_dict[key].dep_node)>0:
                for dep in range(len(self.node_dict[key].dep_node)):
                    print('Dependent nodes:%i' %self.node_dict[key].dep_node[dep])
            else: 
                print("No dependent nodes")
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
        self.parent=0

    def set_dep_nodes(self, dep_name):
        self.dep_node.append(dep_name)

    def set_neighbor_downstream(self, neighbor_name):
        self.neighbor_downstream = neighbor_name

nodes = 5
edges = 13


g = DAG(nodes, edges)
g.print_dep_nodes()
