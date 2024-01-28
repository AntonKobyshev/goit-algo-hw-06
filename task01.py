import networkx as nx
import matplotlib.pyplot as plt
import math

graph = [
    ("Alice", "Bob", {"weight": 7}),
    ("Charlie", "David", {"weight": 9}),
    ("David", "Eve", {"weight": 3}),
    ("Frank", "Alice", {"weight": 5}),
    ("Bob", "Charlie", {"weight": 4}),
    ("George", "Frank", {"weight": 4}),
    ("Henry", "George", {"weight": 5}),
    ("Henry", "Isabel", {"weight": 12}),
    ("Isabel", "Jack", {"weight": 8}),
    ("Jack", "Bob", {"weight": 11}),
    ("Alice", "Jack", {"weight": 7}),
    ("Charlie", "Alice", {"weight": 8}),
    ("Frank", "Eve", {"weight": 9}),
    ("Eve", "Alice", {"weight": 5}),
    ("David", "Alice", {"weight": 4}),
    ("Alice", "Isabel", {"weight": 7}),
    ("Henry", "Alice", {"weight": 12}),
    ("Alice", "George", {"weight": 12}),
]

G = nx.DiGraph()
G.add_edges_from(graph)

positions = nx.circular_layout(G)

center_position = (0, 0)
max_degree_node = max(G.degree, key=lambda x: x[1])[0]
positions[max_degree_node] = center_position

radius = 2
angle_increment = 2 * math.pi / (len(G.nodes) - 1)
for i, node in enumerate(sorted(G.nodes())):
    if node != max_degree_node:
        angle = i * angle_increment
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        positions[node] = (x, y)

def draw_graph():
    nx.draw(
        G,
        positions,
        with_labels=True,
        labels={node: node for node in G.nodes()},  
        node_color="blue",
        node_size=3400,
        font_size=8,
    )
    nx.draw_networkx_edge_labels(
        G,
        positions,
        edge_labels=nx.get_edge_attributes(G, "weight"),
    )

    plt.title("Social Network")
    plt.show()


if __name__ == "__main__":
    draw_graph()
