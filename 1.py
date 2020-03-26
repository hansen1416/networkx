import networkx as nx

# Read data from the dataset, and create graph G_fb
G_fb = nx.read_edgelist("facebook_combined.txt", create_using = nx.Graph(), nodetype=int)

# Show the number of edges in G_fb, 88234
print("edges = " + str(G_fb.number_of_edges()))

# Show number of nodes in G_fb, 4039
print("nodes = " + str(G_fb.number_of_nodes()))

# print(list(G_fb.nodes))
# print(nx.degree(G_fb,3401))

total_edges = G_fb.number_of_edges()
total_nodes = G_fb.number_of_nodes()
# maximum possible edges, 8154741
complete_edges = int(total_nodes * (total_nodes - 1) / 2)
# 0.010819963503439287
edge_probab = total_edges / complete_edges
# 0.6055467186200876
# nx.average_clustering(G_fb)

# print(nx.clustering(G_fb))

G_er = nx.erdos_renyi_graph(total_nodes, edge_probab)

# print(G_er.number_of_nodes(), G_er.number_of_edges())

# 0.01079858842743829
# print(nx.average_clustering(G_er))


betCent = nx.betweenness_centrality(G_fb, normalized=True, endpoints=True)
top10 = sorted(betCent, key=betCent.get, reverse=True)[:10]
# [107, 1684, 3437, 1912, 1085, 0, 698, 567, 58, 428
print(top10)
