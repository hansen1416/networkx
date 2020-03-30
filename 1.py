import networkx as nx
import functools as ft

# The facebook_combined SNAP dataset combines the edges of 10 Facebook ego networks. 
# Recall that an ego network in a social network graph is the induced subgraph 
# on a designated vertex (the ego network center)  and all its neighbours. 
# In other words, an ego network is constructed by picking a user and taking all her/his friends 
# and friendship relations among them. 
# In an ego network, any vertex is directly connected to the center. 
# Thus, in our dataset any vertex is directly connected to at least one of the 10 ego network centers. 
# ("At least," because a vertex may belong to several ego networks at the same time.) 
# In the dataset file, however, 
# the center vertices are not clearly designated (in particular, they are not vertices 0, 1, 2, ..., 9).

# Your task in this assignment is as follows. 
# Consider the following set of 11 vertices: 0, 107, 348, 414, 612, 686, 698, 1684, 1912, 3437, 3980. 
# It is guaranteed that this set includes all 10 ego network centers,  plus one extra vertex. 
# The program should distinguish the added 11th vertex from the 10 ego network centers. 
# As the answer, please provide the number of this additional vertex.

# The answer should be provided just as a number, one of 0, 107, 348, 414, 612, 686, 698, 1684, 1912, 3437, 3980.

G = nx.read_edgelist("facebook_combined.txt")

pseudocenters = [ "0", "107", "1684", "1912", "3437", "348", "612", "3980", "414", "686", "698" ]

# for i in pseudocenters:
    # print(i + " local clustering coefficient:" + str(nx.clustering(G, i))) # 612:0.69
    # print(i + " vertex degree:" + str(nx.degree(G, i))) # 612:15
    # print(i + " eccentricity:" + str(nx.eccentricity(G, i)))

# for dc in nx.degree_centrality(G).items():
    # if dc[0] in pseudocenters:
        # print(dc[0] + " degree_centrality:" + str(dc[1])) # 612 degree_centrality:0.003714710252600297

# for dc in nx.closeness_centrality(G).items():
#     if dc[0] in pseudocenters:
#         print(dc[0] + " closeness_centrality:" + str(dc[1])) # 612 degree_centrality:0.003714710252600297

centers = [ "0", "107", "1684", "1912", "3437", "348", "3980", "414", "686", "698" ]

for no in list(G.nodes):
    if no in centers:
        continue

    not_neighbor=False
    for c in centers:
        if no in G.neighbors(c):
            not_neighbor=c
    if not_neighbor == False:
        print(no + " is not connected")
        break
    else:
        print(no + " is connected")







# # Read data from the dataset, and create graph G_fb
# G_fb = nx.read_edgelist("facebook_combined.txt", create_using = nx.Graph(), nodetype=int)

# # Show the number of edges in G_fb, 88234
# print("edges = " + str(G_fb.number_of_edges()))

# # Show number of nodes in G_fb, 4039
# print("nodes = " + str(G_fb.number_of_nodes()))

# print(list(G_fb.nodes))
# print(nx.degree(G_fb,3401))

# total_edges = G_fb.number_of_edges()
# total_nodes = G_fb.number_of_nodes()
# # maximum possible edges, 8154741
# complete_edges = int(total_nodes * (total_nodes - 1) / 2)
# # 0.010819963503439287
# edge_probab = total_edges / complete_edges
# # 0.6055467186200876
# # nx.average_clustering(G_fb)

# # print(nx.clustering(G_fb))

# G_er = nx.erdos_renyi_graph(total_nodes, edge_probab)

# # print(G_er.number_of_nodes(), G_er.number_of_edges())

# # 0.01079858842743829
# # print(nx.average_clustering(G_er))

