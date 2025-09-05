from .node import Node
from .edge import Edge


class Graph:
  def __init__(self, directed: bool = False):
    self.adj_list = {}
    self.directed = directed

  def __add_node(self, node: Node) -> None:
    if node not in self.adj_list:
      self.adj_list[node] = []

  def add_edge(self, edge: Edge) -> None:
    self.__add_node(edge.from_node)
    self.__add_node(edge.to_node)
    self.adj_list[edge.from_node].append(edge)
    if not self.directed:
      self.adj_list[edge.to_node].append(Edge(edge.to_node, edge.from_node, 1.0))

  def get_edges(self, node: Node) -> list[Edge]:
    return list(self.adj_list.get(node, []))
