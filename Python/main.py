import sys
import os
sys.path.append(os.path.abspath(".."))

from resources.graph import Graph
from resources.edge import Edge
from resources.node import Node
from Python.algoritms.search.bfs import BFS



a = Node("A")
b = Node("B")
c = Node("C")
d = Node("D")
e = Node("E")
f = Node("F")


g = Graph()
g.add_edge(Edge(a, b, 1.0))
g.add_edge(Edge(a, c, 1.0))
g.add_edge(Edge(b, d, 1.0))
g.add_edge(Edge(b, e, 1.0))
g.add_edge(Edge(c, f, 1.0))

bfs = BFS(graph=g, start_node=e, goal_node=f)
bfs.search()


