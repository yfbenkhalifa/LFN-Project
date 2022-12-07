import os
import networkx as nx
from utilities import Utilities as utils
from rdflib import Graph, Literal, RDF, URIRef, Namespace

class Dataset:
    dataframes = {}
    graph = None
    namespaces = {}
    sources = []
    def __init__(self):
        self.initGraph()
    
    def initGraph(self):
        self.graph = nx.Graph()
        
    
    def initGraph(self, nodes : list):
        self.graph = nx.Graph()
        if len(nodes) > 0:  
            self.graph.add_nodes_from(nodes)
        else:
            print('Error: Empty node list')
            
    def initGraph(self, nodes):
        self.graph = nx.Graph()
        if type(nodes) is list:
            self.addNodes(nodes)
        self.addNodes(nodes)
            
    def initGraph(self, graph : nx.Grap):
        self.graph.add_nodes_from(graph)
        
    def addNodes(self, nodes : list):
        if len(nodes) > 0:  
            self.graph.add_nodes_from(nodes)
        else:
            print('Error: Empty node list')
            
    def addNodes(self, nodes: tuple , positions : dict):
        if nodes.count() > 0:  
            self.graph.add_nodes_from(nodes)
        else:
            print('Error: Empty node list')
            
    def addDataset(self, filePath, name=''):
        df = utils.creteDataframe(filePath)
        utils.cleanDataframe(df)
        if df is None:
            print('Error: File not found or not valid')
        else:
            if self.dataframes.get(name) is None:
                self.dataframes[name] = df
            else: 
                self.dataframes[name].append(df)
            print('Added ' + filePath + ' to dataset') 
            
    def addDatasets(self, files):
        for file in files:
            self.addDataset(file)
            
    
                
                