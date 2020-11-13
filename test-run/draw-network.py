import networkx as nx
import matplotlib.pyplot as plt

# Erstellen und Zeichnen des Netzwerks:
network = nx.read_edgelist("testdata-graph.txt",
                           delimiter = ' ', 
                           create_using = nx.DiGraph, 
                           nodetype = int)

nx.draw(network)

# Berechnen der Out-Degrees (Ergebniswerte sind komisch!!)
network_outdegree = nx.out_degree_centrality(network)
network_outdegree
