import sys
import os
sys.path.append(os.path.abspath(".."))

from resources.graph import Graph
from resources.edge import Edge
from resources.node import Node
from Python.algoritms.search.bfs import BFS
from Python.algoritms.search.dfs import DFS
from Python.algoritms.search.binarySearch import BinarySearch



# a = Node("A")
# b = Node("B")
# c = Node("C")
# d = Node("D")
# e = Node("E")
# f = Node("F")
# g = Node("G")
# h = Node("H")
# i = Node("I")
# j = Node("J")



# G = Graph()
# G.add_edge(Edge(a, b, 1.0))
# G.add_edge(Edge(a, c, 1.0))
# G.add_edge(Edge(b, d, 1.0))
# G.add_edge(Edge(b, e, 1.0))
# G.add_edge(Edge(c, f, 1.0))
# G.add_edge(Edge(d, g, 1.0))
# G.add_edge(Edge(d, h, 1.0))
# G.add_edge(Edge(e, i, 1.0))
# G.add_edge(Edge(f, j, 1.0))


# # print(G.adj_list)




# # bfs = BFS(graph=g, start_node=e, goal_node=f)
# # bfs.search()

# dfs = DFS(graph=G, start_node=a, goal_node=e)
# dfs.search()


bs = BinarySearch([0,1,2,3,4,5,6,7], 10)
print(bs.search())




