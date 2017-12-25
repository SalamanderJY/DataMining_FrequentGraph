# Given parameters d and s and an additional integer k, design and implement an algorithm to find k diversified frequent
# d-densely connected vertex subsets S1, S2 ,..., Sk such that |S| is maximized.

class UnionGraph:

    def __init__(self, graphs, k):
        self.frequentGraph = graphs.frequentGraph
        self.k = k
        self.subsets = []


    def findMaximialUnion(self):
        if self.k >= len(self.frequentGraph):
            self.subsets = self.frequentGraph
        else:

    def puningSubgraph(self):




