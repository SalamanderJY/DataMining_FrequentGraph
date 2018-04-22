import matplotlib.pyplot as plt
import networkx as nx

from src import graph_generator, multi_graph


class DrawGraph:

    def drawGraph(self, graph, index=0):
        g = nx.Graph()
        v = []
        e = []
        for i in range(0, graph.vertex):
            v.append(i)
        for i in range(0, graph.vertex):
            for j in range(0, graph.vertex):
                points = []
                if graph.matrix[i][j] == 1:
                    points.append(i)
                    points.append(j)
                    e.append(tuple(points))
        print(e)
        g.add_nodes_from(v)
        g.add_edges_from(e)
        nx.draw_circular(g, with_labels=True, font_weight='bold')
        plt.plot()
        plt.savefig("graph" + str(index) + ".png")
        plt.show()

    def drawGraphs(self, graphs, index=0):

        for i in range(0, len(graphs)):
            graph = graphs[i]
            self.drawGraph(graph, i)


if __name__ == "__main__":
    graphs = []
    graph1 = graph_generator.Graph(6, 10, 3)
    graphs.append(graph1)
    graph2 = graph_generator.Graph(6, 10, 3)
    graphs.append(graph2)
    graph3 = graph_generator.Graph(6, 10, 3)
    graphs.append(graph3)
    graph4 = graph_generator.Graph(6, 10, 3)
    graphs.append(graph4)

    draw = DrawGraph()
    draw.drawGraphs(graphs)

    multigraph = multi_graph.MultiGraph(graphs, 2)
