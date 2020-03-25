import networkx as nx

# Read data from the dataset, and create graph G_fb
G_fb = nx.read_edgelist("facebook_combined.txt", create_using = nx.Graph(), nodetype=int)

# Show the number of edges in G_fb
print("edges = " + str(G_fb.number_of_edges()))

# Show number of nodes in G_fb
print("nodes = " + str(G_fb.number_of_nodes()))

# print(list(G_fb.nodes))
# print(nx.degree(G_fb,3401))

total_edges = G_fb.number_of_edges()
total_nodes = G_fb.number_of_nodes()

complete_edges = int(total_nodes * (total_nodes - 1) / 2)

edge_probab = total_edges / complete_edges

print(edge_probab, complete_edges)

# print(nx.average_clustering(G_fb))
