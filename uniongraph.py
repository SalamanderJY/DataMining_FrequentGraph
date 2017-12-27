# Given parameters d and s and an additional integer k, design and implement an algorithm to find k diversified frequent
# d-densely connected vertex subsets S1, S2 ,..., Sk such that |S| is maximized.

import graph
import multigraph
import itertools


class UnionGraph:

    def __init__(self, graphs, k):
        self.frequentGraph = graphs.frequentGraph
        self.k = k
        self.subsets = []

    def findMaximialUnion(self):
        if self.k >= len(self.frequentGraph):
            self.subsets = self.frequentGraph
        else:
            cleanFrequentGraph, dirtyFrequentGraph = self.pruningSubgraph()
            if self.k >= len(cleanFrequentGraph):
                subset = list(itertools.combinations(dirtyFrequentGraph, self.k - len(cleanFrequentGraph)))
            else:
                subset = list(itertools.combinations(dirtyFrequentGraph, self.k))
                size = 0
                flag = 0
                for i in range(0, len(subset)):
                    if size < self.getUnionGraphSize(subset[i]):
                        size = self.getUnionGraphSize(subset[i])
                        flag = i
                self.subsets = subset[flag]


    def pruningSubgraph(self):
        containFrequentGraph = []
        for i in range(0, len(self.frequentGraph)):
            pointer = self.frequentGraph[i]
            for j in range(i + 1, len(self.frequentGraph)):
                if self.isSubset(pointer, self.frequentGraph[j]):
                    containFrequentGraph.append(i)
                    break
        cleanFrequentGraph = self.frequentGraph
        dirtyFrequentGraph = []
        for i in range(0, len(containFrequentGraph)):
            del cleanFrequentGraph[containFrequentGraph[i]]
        for i in range(0, len(containFrequentGraph)):
            dirtyFrequentGraph.append(self.frequentGraph[containFrequentGraph[i]])
        return cleanFrequentGraph, dirtyFrequentGraph

    def isSubset(self, tuple1, tuple2):
        count1 = 0
        count2 = 0
        match = 0
        while count1 < len(tuple1) & count2 < len(tuple2):
            if tuple1[count1] == tuple2[count2]:
                count1 += 1
                count2 += 1
                match += 1
            else:
                count2 += 1
        if match == len(tuple1):
            return True
        else:
            return False

    def getUnionGraphSize(self, subset):
        initial = set(subset[0])
        for i in range(1, len(subset)):
            initial = initial.union(set(subset[i]))
        return len(initial)

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

    multigraph = multigraph.MultiGraph(graphs, 3)
    print(type(multigraph.frequentGraph))




