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
        assert (number_edges<=(number_nodes*(number_nodes- 1))/2)
        
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
            assert (len(dep_node_pot) >= num_dep_nodes)
            
            dep_nodes = r.sample(dep_node_pot, num_dep_nodes)

            ## Randomly pick dependent nodes from list of potential dep nodes
            if num_dep_nodes>0:
                dep_nodes = r.sample(dep_node_pot, num_dep_nodes)
                #Add dependent nodes to list of dep of node object
                for j in range(num_dep_nodes):
                    self.node_dict[node_order].set_dep_nodes(dep_nodes[j])
                actual_edges += num_dep_nodes
#                print('Number of edges %i' %actual_edges)
                
                    
            else:
                self.node_dict[node_order].dep_node=[]

        assert (len(self.node_dict) == self.total_nodes) #check all nodes created
        
        
        while number_edges > actual_edges:
            open_nodes=[]
            for key in self.node_dict.keys():
                #check which nodes have less dependents than potential dependents
                if len(self.node_dict[key].dep_node) < number_nodes-(key+1):
                    #Add all those nodes to a list
                    open_nodes.append(key)
                    
            # Pick a random entry from that list
            sel_node_index = r.randint(0, len(open_nodes)-1)
            sel_node=open_nodes[sel_node_index]
            dep_node_pot = list(range(sel_node+1, self.total_nodes))
            dep_node_pot_new=list(set(dep_node_pot) - set(self.node_dict[sel_node].dep_node))
            dep_nodes_new = r.sample(dep_node_pot_new, 1)
            self.node_dict[sel_node].set_dep_nodes(dep_nodes_new[0])
            actual_edges+=1
        while number_edges<actual_edges:
            pot_nodes=[]
            for key in self.node_dict.keys():
                if(len(self.node_dict[key].dep_node)>1):
                    pot_nodes.append(key)
            sel_node_index=r.randint(0, len(pot_nodes)-1)
            sel_node=pot_nodes[sel_node_index]
            
            del_node_index = r.randint(0, len(self.node_dict[sel_node].dep_node)-1)
            self.node_dict[sel_node].dep_node.pop(del_node_index)
            actual_edges-=1
                
        for key in self.node_dict.keys():
#            print('Name of node: %i' %key)
            for node in self.node_dict.keys():
                if key in self.node_dict[node].dep_node:
#                    print("Here are the dependent nodes of %i" %node)
#                    print(self.node_dict[node].dep_node)
                    self.node_dict[key].find_parents(node)
#                    print('Parents: %i' %self.node_dict[node])
    
    def add_node(self, name):
        self.node_dict.update({name:node(name)})
    
    def print_dep_nodes(self):
        #Iterate over node dictionary
        for key in self.node_dict.keys():
            print('Name of node: %i' %key)
            if len(self.node_dict[key].dep_node)>0:
                for dep in range(len(self.node_dict[key].dep_node)):
                    print('  Dependent node: %i' %self.node_dict[key].dep_node[dep])
            else: 
                print("  No dependent nodes")
    def print_parents(self):
        for key in self.node_dict.keys():
            print('Name of node: %i' % key)
            if(len(self.node_dict[key].parent)>0):
                for parent in range(len(self.node_dict[key].parent)):
                    print('  Parent: %i' %self.node_dict[key].parent[parent])
            else: 
                print("  No parents")
                


class node(object):
    
    def __init__(self, name):
        self.name = name
        self.dep_node = []
        self.parent=[]
        self.node_value=None

    def set_dep_nodes(self, dep_name):
        self.dep_node.append(dep_name)
    def find_parents(self, parent):
        self.parent.append(parent)

    def set_neighbor_downstream(self, neighbor_name):
        self.neighbor_downstream = neighbor_name

