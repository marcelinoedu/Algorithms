class Node:
  def __init__(self, name: str) -> None:
    self.name = name

  def __repr__(self) -> str:
    return f"Node({self.name})"

  def __eq__(self, __o: object) -> bool:
    return isinstance(__o, Node) and self.name == __o.name

  def __hash__(self) -> int:
    return hash(self.name)