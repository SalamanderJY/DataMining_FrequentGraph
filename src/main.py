import networkx as nx
import matplotlib.pyplot as plt


G = nx.Graph()
G.add_nodes_from([0, 1, 2, 3, 4, 5])
G.add_edges_from([(0, 2), (0, 3), (0, 4), (2, 3), (2, 4), (3, 4)])
nx.draw_circular(G, with_labels=True, font_weight='bold')
plt.plot()
plt.show()

print(nx.__version__)