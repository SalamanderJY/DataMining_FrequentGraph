# Let G i = (V,E) (i = 1,2,...,n) be n undirected simple graphs consisting of the same set of vertices.
# A graph is undirected if edge (u,v) and edge (v,u) refer to the same edge.
# A graph is simple if it contains neither loops nor multi-edges.
# A subset of vertices S belong to V is said to be d-densely connected in graph Gi
# if every vertex in the induced sub-graph G[S] has degree at least d, where d > 0.
# Vertex subset S is said to be frequent if it is d-densely connected in at least s graphs in G1 ,G2 ,...,Gn.
import numpy as np
import random
import itertools

import networkx as nx
import matplotlib.pyplot as plt


class Graph:

    def __init__(self, vertex, edge, degree):
        # vertex * vertex
        self.vertex = vertex
        self.edge = edge
        self.degree = degree
        self.satisfyVertex = []
        self.satisfyDegree = []
        self.matrix = np.zeros((vertex, vertex), np.uint8)
        # initial Adjacency Matrix
        self.initialAdjacencyMatrix()
        # find vertex by degree
        self.findVertexByDegree()
        # find all induced subgraph satisfy that they are d-densely.
        self.findInitialInducedGraph()
        # graph show the initial graph
        # self.drawGraph()

    def initialAdjacencyMatrix(self):
        # total edge of graph
        edges = int(self.vertex * (self.vertex - 1) / 2)
        # initial edge set
        initial = np.zeros((1, edges), np.uint8)
        for i in range(0, self.edge):
            initial[0][i] = 1
        # random edge connected
        random.shuffle(initial[0])

        # print(initial)
        # initial adjacency matrix
        count = 0
        for i in range(0, self.vertex):
            for j in range(0, self.vertex):
                if j > i:
                    self.matrix[i][j] = initial[0][count]
                    count += 1
                # generate undirected simple graphs corresponding vertex
                if self.matrix[i][j] == 1:
                    self.matrix[j][i] = 1
        print(self.matrix)

    def findVertexByDegree(self):
        for i in range(0, self.vertex):
            if np.sum(self.matrix[i]) >= self.degree:
                self.satisfyVertex.append(i)

        print(self.satisfyVertex)

    # judge the vertex points is induced sub-graph or not.
    def isInducedGraph(self, points):

        induced = {}
        flag = True
        for i in range(0, len(points)):
            if str(points[i][0]) in induced:
                if self.matrix[points[i][0], points[i][1]] == 1:
                    induced[str(points[i][0])] += 1
            else:
                if self.matrix[points[i][0], points[i][1]] == 1:
                    induced[str(points[i][0])] = 1

        for i in range(0, len(points)):
            if str(points[i][1]) in induced:
                if self.matrix[points[i][1], points[i][0]] == 1:
                    induced[str(points[i][1])] += 1
            else:
                if self.matrix[points[i][1], points[i][0]] == 1:
                    induced[str(points[i][1])] = 1

        for key in induced.keys():
            if induced[key] < self.degree:
                flag = False
                break
        # print(induced)
        return flag

    def findInitialInducedGraph(self):
        for i in range(self.degree + 1, self.vertex + 1):
            if len(self.satisfyVertex) < i:
                break
            else:
                degreeCombination = list(itertools.combinations(self.satisfyVertex, i))
                # print(degreeCombination)
                # judge if the combination is the real induced sub-graph or not.
                for j in range(0, len(degreeCombination)):
                    subgraph = list(itertools.combinations(degreeCombination[j], 2))
                    # print(subgraph)
                    if self.isInducedGraph(subgraph):
                        self.satisfyDegree.append(degreeCombination[j])
        print("Real Induced Graph:")
        print(self.satisfyDegree)

    def drawGraph(self):
        g = nx.Graph()
        v = []
        e = []
        for i in range(0, self.vertex):
            v.append(i)
        for i in range(0, self.vertex):
            for j in range(0, self.vertex):
                points = []
                if self.matrix[i][j] == 1:
                    points.append(i)
                    points.append(j)
                    e.append(tuple(points))
        #print(e)
        g.add_nodes_from(v)
        g.add_edges_from(e)
        nx.draw_circular(g, with_labels=True, font_weight='bold')
        plt.plot()
        plt.savefig("dense_graph.png")
        plt.show()


if __name__ == "__main__":

    #starttime = time.time()
    for i in range(0, 1):
        gr = Graph(18, 20, 5)
    #endtime = time.time()
    #print(endtime - starttime)

    # gr.drawGraph()


