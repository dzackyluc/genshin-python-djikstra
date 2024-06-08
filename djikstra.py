import heapq
import tkinter as tk
from collections import defaultdict

class Dijkstra:
    def __init__(self, graph):
        self.graph = graph

    def shortest_path(self, start, end):
        # Initialize distances and visited nodes
        distances = {node: float('inf') for node in self.graph}
        distances[start] = 0
        visited = set()

        # Priority queue to store nodes with their distances
        queue = [(0, start)]

        while queue:
            # Get the node with the minimum distance
            current_distance, current_node = heapq.heappop(queue)

            # Skip if the node has already been visited
            if current_node in visited:
                continue

            # Mark the current node as visited
            visited.add(current_node)

            # Update distances of adjacent nodes
            for neighbor, weight in self.graph[current_node].items():
                distance = current_distance + weight

                # If a shorter path is found, update the distance
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(queue, (distance, neighbor))

        # Return the shortest distance from start to end
        return distances[end]

class GraphDrawer:
    def __init__(self, graph, pos):
        self.graph = graph
        self.pos = pos

    def draw_graph(self):
        canvas = tk.Canvas(width=500, height=500)
        canvas.pack()

        for node, coords in self.pos.items():
            x, y = coords
            node_circle = canvas.create_oval(x-5, y-5, x+5, y+5, fill='white')
            node_text = canvas.create_text(x, y, text=node)

        for node, edges in self.graph.items():
            for neighbor, weight in edges.items():
                x1, y1 = pos[node]
                x2, y2 = pos[neighbor]
                edge = canvas.create_line(x1, y1, x2, y2, width=2)
                edge_text = canvas.create_text((x1+x2)/2, (y1+y2)/2, text=str(weight))

# Define the graph
graph = {
    'Chest 1': {'Chest 2': 5, 'Chest 3': 2},
    'Chest 2': {'Chest 1': 5, 'Chest 3': 1, 'Chest 4': 3},
    'Chest 3': {'Chest 1': 2, 'Chest 2': 1, 'Chest 4': 6},
    'Chest 4': {'Chest 2': 3, 'Chest 2': 6}
}

pos = {
    'Cathedral': (100, 100),
    'Windmill': (150, 150),
    'Town Square': (200, 200),
    'Wine and Song': (250, 250),
    'Mondstadt Gate': (300, 300),
    'Outskirts': (350, 350),
    'Forest': (400, 400),
    'Chest 1': (450, 450),
    'Chest 2': (500, 500),
    'Chest 3': (550, 550),
    'Chest 4': (600, 600)
}

# Create an instance of GraphDrawer
GraphDrawer(graph, pos).draw_graph()