from .node import Node


class Queue:
    def __init__(self):
        self.items = []
        
    def enqueue(self, item) -> None:
        self.items.append(item)
        
    def dequeue(self) -> Node:
        if self.is_empty():
            raise ValueError("A fila está vazia!")
        return self.items.pop(0)
    
    def is_empty(self) -> bool:
        return len(self.items) == 0
