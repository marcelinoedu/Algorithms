from .node import Node


class Stack:
    
    def __init__(self):
        
        self.items = []
        
    def push(self, item: Node) -> None:
        self.items.insert(0,item)
    
    def pop(self) -> Node:
        if self.is_empty():
            raise IndexError("A fila está vazia!")
        return self.items.pop(0)
    
    def is_empty(self):
        
        return len(self.items) == 0        
    