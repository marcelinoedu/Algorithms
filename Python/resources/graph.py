from .node import Node
from .edge import Edge


class Graph:
  def __init__(self, directed: bool = False):
    self.adj_list = {}
    self.directed = directed

  def add_node(self, node: Node) -> None:
    if node not in self.adj_list:
      self.adj_list[node] = []

  def add_edge(self, edge: Edge) -> None:
    self.add_node(edge.from_node)
    self.add_node(edge.to_node)

    self.adj_list[edge.from_node].append((edge.to_node, edge.cost))

    if not self.directed:
      self.adj_list[edge.to_node].append((edge.from_node, edge.cost))

  def get_neighbors(self, node: Node) -> list:
    return list(self.adj_list.get(node, []))
