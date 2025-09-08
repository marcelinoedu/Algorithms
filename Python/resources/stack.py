from .node import Node


class Stack:
    
    def __init__(self):
        
        self.items = []
        
    def push(self, item: Node) -> None:
        self.items.append(item)
    
    def pop(self) -> Node:
        if self.is_empty():
            raise IndexError("A fila está vazia!")
        return self.items.pop()
    
    def is_empty(self):
        return len(self.items) == 0        
    