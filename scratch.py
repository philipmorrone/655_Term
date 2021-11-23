import csv
from operator import itemgetter
import networkx as nx


with open('quakers_nodelist.csv', 'r') as nodecsv: # Open the file
    nodereader = csv.reader(nodecsv) # Read the csv
    nodes = [n for n in nodereader][1:]

node_names = [n[0] for n in nodes] # Get a list of only the node names

with open('quakers_edgelist.csv', 'r') as edgecsv: # Open the file
    edgereader = csv.reader(edgecsv) # Read the csv
    edges = [tuple(e) for e in edgereader][1:] # Retrieve the data

print(len(node_names))

print(len(edges))

G = nx.Graph()
G.add_nodes_from(node_names)
G.add_edges_from(edges)

print(nx.info(G))

degree_dict = dict(G.degree(G.nodes()))
sorted_degree = sorted(degree_dict.items(), key=itemgetter(1), reverse=True)

print("Top 20 nodes by degree:")
for d in sorted_degree[:20]:
    print(d)

nx.write_gexf(G, "test11.gexf")

#afsafdsf


