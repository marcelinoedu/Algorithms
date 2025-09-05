import sys
import os
sys.path.append(os.path.abspath(".."))
from resources.graph import Graph
from resources.edge import Edge
from resources.node import Node
from resources.queue import Queue



class BFS:

    def __init__(self, graph: Graph, start_node: Node, goal_node: Node = None) -> None:
        self.graph = graph
        self.start_node = start_node
        self.goal_node = goal_node
        self.visited_nodes_path = []
        self.queue = Queue()
        

    def search(self) -> None:
        if self.start_node not in self.graph.adj_list:
            raise ValueError("Node de início não pertence ao Grafo")
        
        self.queue.enqueue(self.start_node)
        
        while not self.queue.is_empty():
            print(f"fila: {self.queue.items}")
            actual_node = self.queue.dequeue()
            print(f"node tirado da fila: {actual_node}")
            self.visited_nodes_path.append(actual_node)
            if actual_node == self.goal_node:
                print(f"resultado encontrado= {self.goal_node}, caminho feito={self.visited_nodes_path}")
                break
            edges = self.graph.get_edges(actual_node) 
            print(f"vizinhos: {edges}")
            for edge in edges:
                if edge.to_node not in self.visited_nodes_path:
                    self.queue.enqueue(edge.to_node)
                    print(f"vizinho colocado na fila {edge.to_node}")
            print(f"atualização dos nodes vizitados {self.visited_nodes_path}")
            
