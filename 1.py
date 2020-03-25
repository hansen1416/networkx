import networkx as nx

# Read data from the dataset, and create graph G_fb
G_fb = nx.read_edgelist("facebook_combined.txt", create_using = nx.Graph(), nodetype=int)

# Show the number of edges in G_fb
print("edges = " + str(G_fb.number_of_edges()))

# Show number of nodes in G_fb
print("nodes = " + str(G_fb.number_of_nodes()))

# print(G.number_of_nodes(), G.number_of_edges(), list(G.nodes))