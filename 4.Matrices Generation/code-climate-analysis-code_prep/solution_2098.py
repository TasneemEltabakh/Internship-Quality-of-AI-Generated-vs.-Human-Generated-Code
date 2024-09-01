# importing the required module
import networkx as nx


# making a simple graph with 1 node.
G = nx.path_graph(10)


# saving graph created above in gexf format
nx.write_gexf(G, "geeksforgeeks.gexf")