from .node import Node

class Edge:
  def __init__(self, from_node: Node, to_node: Node, cost: float) -> None:
    self.from_node = from_node
    self.to_node = to_node
    self.cost = cost
  
  def __repr__(self) -> str:
    return f"Edge({self.from_node.name} -> {self.to_node.name}, cost={self.cost})"
