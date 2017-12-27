import graph
import networkx as nx
import networkx.drawing
import matplotlib.pyplot as plt


G = nx.Graph()
G.add_nodes_from([0, 1, 2, 3])
G.add_edges_from([(0, 1), (1, 2), (1, 3), (2, 3), (0, 2)])
nx.draw_circular(G, with_labels=True, font_weight='bold')
plt.plot()
plt.show()