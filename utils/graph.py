import networkx as nx
from matplotlib import pyplot as plt


class Graph:
    def __init__(self):
        self.graph = nx.DiGraph()


    def get_vertices(self):
        return self.graph.nodes()

    def print_graph(self):
        print(list(nx.topological_sort(self.graph)))

    def add_edge(self, v1, v2):
        self.graph.add_edges_from([(v1,v2)])


    def plot_graph(self):
        plt.tight_layout()
        nx.draw_networkx(self.graph, arrows=True)
        plt.savefig("g.png", format="PNG")
        plt.clf()