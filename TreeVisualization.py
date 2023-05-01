# Python file for visualizing graph

from graphviz import Graph

class Visualization:
    def __init__(self):
        G = Graph()

    def visual(self, one, two):
        self.G.node(one)
        self.G.node(two)
        self.G.edge(one, two)

        self.G.render(view = True)
        self.G.render(filename = "KBGame")
