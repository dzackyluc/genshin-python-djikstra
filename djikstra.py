import heapq
import tkinter as tk
from tkinter import simpledialog
from PIL import Image, ImageTk

# Inisiasi class Graph untuk membuat algoritma djikstra
class Graph:
    # Inisiasi Graph dengan dictionary kosong
    def __init__(self, graph={}):
        self.graph = graph

    # Menambahkan Data pada Graph
    def add_edge(self, node1, node2, weight):
        if node1 not in self.graph:
            self.graph[node1] = {}
        self.graph[node1][node2] = weight
    
    # Algoritma Djikstra untuk mencari jarak terpendek
    def shortest_path(self, start, end):
        # Inisiasi jarak dan node yang sudah dikunjungi
        distances = {node: float('inf') for node in self.graph}
        # Jarak dari node awal adalah 0
        distances[start] = 0

        # Priority Queue untuk menyimpan node dengan jaraknya
        pq = [(0, start)]
        # Mengurutkan Priority Queue menggunakan heapq BST
        heapq.heapify(pq)

        # Set untuk menyimpan node yang sudah dikunjungi
        visited = set()
        # Dictionary untuk menyimpan node sebelumnya
        previous = {}

        # Looping untuk mencari jarak terpendek
        while pq:
            # Mengambil node dengan jarak terpendek
            current_distance, current_node = heapq.heappop(pq)
            # Skip jika node sudah dikunjungi
            if current_node in visited:
                continue
            
            # Menandai node yang sedang dikunjungi
            visited.add(current_node)

            # Update jarak node tetangga dari node yang sedang dikunjungi
            for neighbor, weight in self.graph[current_node].items():
                tentative_distance = current_distance + weight
                if tentative_distance < distances[neighbor]:
                    distances[neighbor] = tentative_distance
                    previous[neighbor] = current_node
                    heapq.heappush(pq, (tentative_distance, neighbor))

        # Membuat path dari node awal ke node akhir
        path = []
        # Menambahkan node akhir ke path
        while end:
            path.append(end)
            end = previous.get(end)

        # Mengembalikan path dari node awal ke node akhir
        return path[::-1]

# Create a Tkinter window
root = tk.Tk()
root.title("Stormbearer Point Chest Route")

# Create a canvas to display the image
canvas = tk.Canvas(root, width=886, height=542)
canvas.pack()

# Load the image file
image = Image.open("stormbearer_point.png")
photo = ImageTk.PhotoImage(image)

# Menampilkan Image pada Canvas
canvas.create_image(0, 0, anchor=tk.NW, image=photo)

# Membuat Node dan Edge untuk Graph
nodes = {
    'Waypoint': (220, 425),
    'Chest 1': (335, 420),
    'Chest 2': (330, 375),
    'Chest 3': (80, 450),
    'Chest 4': (175, 230),
    'Chest 5': (225, 120),
    'Chest 6': (95, 170),
    'Chest 7': (485, 390),
    'Chest 8': (580, 390),
    'Chest 9': (480, 145),
    'Chest 10': (700, 280),
    'Chest 11': (785, 380)
}

edges = {
    'Waypoint': {'Chest 1': 18, 'Chest 2': 26, 'Chest 3': 70},
    'Chest 1': {'Chest 2': 10},
    'Chest 2': {'Chest 4': 44, 'Chest 7': 36},
    'Chest 3': {'Chest 6': 143},
    'Chest 4': {'Chest 5': 26, 'Chest 3': 118},
    'Chest 5': {'Chest 6': 32},
    'Chest 6': {'Chest 4': 21},
    'Chest 7': {'Chest 8': 16},
    'Chest 8': {'Chest 10': 30, 'Chest 11': 31},
    'Chest 9': {'Chest 5': 44},
    'Chest 10': {'Chest 9': 48},
    'Chest 11': {'Chest 10': 22}
}

graph = Graph(edges)

# menggambar titik lokasi pada canvas gambar
for node, coords in nodes.items():
    x, y = coords
    node_circle = canvas.create_oval(x-5, y-5, x+5, y+5, fill='blue')
    node_text = canvas.create_text(x, y-30, text=node, fill='yellow')

# Mendapatkan input tujuan awal dan akhir dari pengguna
start_node = simpledialog.askstring("Input", "Masukkan titik awal:").capitalize()
end_node = simpledialog.askstring("Input", "Masukkan titik akhir:").capitalize()

# Mencari jarak terpendek dari satu Node ke Node Lain
shortest_path = graph.shortest_path(start_node, end_node)

# Jika terdapat path, maka akan menggambar edge
if len(shortest_path)-1 >= 1:
    for i in range(len(shortest_path)-1):
        node1 = shortest_path[i]
        node2 = shortest_path[i+1]
        x1, y1 = nodes[node1]
        x2, y2 = nodes[node2]
        edge = canvas.create_line(x1, y1, x2, y2, width=3)
    root.mainloop()
# Jika tidak terdapat path, maka akan menampilkan pesan
else:
    print("No path found")