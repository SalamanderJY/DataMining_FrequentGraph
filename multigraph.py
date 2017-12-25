# Let G i = (V,E) (i = 1,2,...,n) be n undirected simple graphs consisting of the same set of vertices.
# A graph is undirected if edge (u,v) and edge (v,u) refer to the same edge.
# A graph is simple if it contains neither loops nor multi-edges.
# A subset of vertices S belong to V is said to be d-densely connected in graph Gi
# if every vertex in the induced sub-graph G[S] has degree at least d, where d > 0.
# Vertex subset S is said to be frequent if it is d-densely connected in at least s graphs in G1 ,G2 ,...,Gn.
import numpy as np
import random
import itertools
import operator as op

import networkx as nx
import networkx.drawing
import matplotlib.pyplot as plt

import graph


class MultiGraph:

    def __init__(self, graphs, support):
        self.isVisited = {}
        self.frequentGraph = []
        self.support = support
        self.graphs = graphs

        self.findAllFrequentGraph()

    def findAllFrequentGraph(self):

        for i in range(0, len(self.graphs)):
            for j in range(0, len(self.graphs[i].satisfyDegree)):
                # Get every induce subgraph
                induce = self.graphs[i].satisfyDegree[j]
                # Judge if it is visited or not
                if str(induce) in self.isVisited:
                    continue
                else:
                    self.isVisited[str(induce)] = True
                    count = 0
                    for k in range(0, len(self.graphs)):
                        for l in range(0, len(self.graphs[k].satisfyDegree)):
                            if op.eq(induce, self.graphs[k].satisfyDegree[l]):
                                count += 1
                                break
                    if count >= self.support:
                        self.frequentGraph.append(induce)
        print(self.frequentGraph)


if __name__ == "__main__":
    graphs = []
    graph1 = graph.Graph(6, 12, 3)
    graphs.append(graph1)
    graph2 = graph.Graph(6, 12, 3)
    graphs.append(graph2)
    graph3 = graph.Graph(6, 12, 3)
    graphs.append(graph3)
    graph4 = graph.Graph(6, 12, 3)
    graphs.append(graph4)


    multigraph = MultiGraph(graphs, 3)

