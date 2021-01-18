class Graph:
    def __init__(self):
        self.numberOfNodes = 0
        self.adjacentList = {}

    def addVertex(self, node):
        self.adjacentList[node] = []
        self.numberOfNodes+=1

    def addEdge(self, node1, node2):
        # undirected Graph
        self.adjacentList[node1].append(node2)
        self.adjacentList[node2].append(node1)

    def showConnetions(self):
        for x in self.adjacentList:
            print(x, '-> ', self.adjacentList[x])