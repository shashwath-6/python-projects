import tkinter as tk
import heapq
import random


class CityGraph:
    def __init__(self):
        self.graph = {}

    def add_road(self, start, end, weight):
        """Adds a bidirectional road between two intersections."""
        if start not in self.graph:
            self.graph[start] = {}
        if end not in self.graph:
            self.graph[end] = {}
        self.graph[start][end] = weight
        self.graph[end][start] = weight

    def update_traffic(self, start, end, new_weight):
        """Dynamically updates traffic conditions (edge weight)."""
        if start in self.graph and end in self.graph[start]:
            self.graph[start][end] = new_weight
            self.graph[end][start] = new_weight

    def find_shortest_path(self, start, goal):
        """Dijkstra's Algorithm to find the shortest path."""
        pq = [(0, start, [])]  # (current cost, current node, path)
        visited = set()

        while pq:
            cost, node, path = heapq.heappop(pq)
            if node in visited:
                continue
            path = path + [node]
            visited.add(node)

            if node == goal:
                return path, cost

            for neighbor, weight in self.graph.get(node, {}).items():
                if neighbor not in visited:
                    heapq.heappush(pq, (cost + weight, neighbor, path))

        return None, float('inf')


class TrafficSimulatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("AI-Powered Traffic Navigation")
        self.canvas = tk.Canvas(root, width=600, height=600, bg="white")
        self.canvas.pack()

        self.city = CityGraph()
        self.locations = {
            "A": (100, 100), "B": (300, 100), "C": (500, 100),
            "D": (100, 300), "E": (300, 300), "F": (500, 300),
            "G": (100, 500), "H": (300, 500), "I": (500, 500)
        }
        self.create_city_graph()
        self.draw_city()

        self.start, self.goal = "A", ""
        self.find_and_draw_path()

    def create_city_graph(self):
        """Creates a predefined city road network with random traffic conditions."""
        roads = [
            ("A", "B", random.randint(5, 20)), ("B", "C", random.randint(5, 20)),
            ("A", "D", random.randint(5, 20)), ("B", "E", random.randint(5, 20)), ("C", "F", random.randint(5, 20)),
            ("D", "E", random.randint(5, 20)), ("E", "F", random.randint(5, 20)),
            ("D", "G", random.randint(5, 20)), ("E", "H", random.randint(5, 20)), ("F", "I", random.randint(5, 20)),
            ("G", "H", random.randint(5, 20)), ("H", "I", random.randint(5, 20))
        ]
        for road in roads:
            self.city.add_road(*road)

    def draw_city(self):
        """Draws the city as a graph using Tkinter."""
        self.canvas.delete("all")
        for loc, (x, y) in self.locations.items():
            self.canvas.create_oval(x - 20, y - 20, x + 20, y + 20, fill="white", outline="black", width=2)
            self.canvas.create_text(x, y, text=loc, font=("Arial", 14, "bold"))

        for start in self.city.graph:
            for end in self.city.graph[start]:
                x1, y1 = self.locations[start]
                x2, y2 = self.locations[end]
                self.canvas.create_line(x1, y1, x2, y2, fill="gray", width=2)

    def find_and_draw_path(self):
        """Finds the shortest path and visualizes it."""
        path, cost = self.city.find_shortest_path(self.start, self.goal)
        if path:
            for i in range(len(path) - 1):
                x1, y1 = self.locations[path[i]]
                x2, y2 = self.locations[path[i + 1]]
                self.canvas.create_line(x1, y1, x2, y2, fill="blue", width=3)
            print(f"Fastest Route: {' -> '.join(path)} (Cost: {cost})")
        else:
            print("No path found!")


if __name__ == "__main__":
    root = tk.Tk()
    app = TrafficSimulatorApp(root)
    root.mainloop()
