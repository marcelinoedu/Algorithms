import sys
import os
sys.path.append(os.path.abspath(".."))
from resources.graph import Graph
from resources.node import Node
from resources.stack import Stack





class IDS:
    
    def __init__(self, graph: Graph, start_node: Node, goal_node: Node):
        self.graph = graph
        self.start_node = start_node
        self.goal_node = goal_node
        self.visited_node_path = []
        self.stack = Stack()