import numpy as np
import networkx as nx
import matplotlib.pyplot as plt


def create_graph_from_matrix(A, nameG="graph"):
    """
    Create and visualize an undirected graph from a given symmetric matrix `A`.

    Parameters:
    A (numpy.ndarray): Symmetric matrix representing edge weights.
    nameG (str): Name for saving the graph visualization.

    Returns:
    None (displays and saves the graph visualization).
    """
    n = A.shape[0]  # Get the size of the matrix (number of nodes)

    # Create an undirected graph
    G = nx.Graph()

    # Add nodes to the graph
    G.add_nodes_from(range(n))

    # Add edges to the graph based on the upper triangular part of the matrix
    for i in range(n):
        for j in range(i + 1, n):  # Consider only upper triangular part
            if A[i, j] > 0:  # Only add edges if the weight is non-zero
                G.add_edge(i, j, weight=A[i, j])  # Add edge with weight

    # Draw the graph
    pos = nx.spring_layout(G, seed=42, k=0.3)  # Define layout for nodes
    nx.draw(
        G,
        pos,
        node_color="skyblue",
        node_size=1000,
        font_size=10,
        font_color="black",
        with_labels=True,
        edge_color="gray",
        width=2.0,
    )

    # Draw edge labels (weights)
    labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_color="red")

    # Save and show the plot
    plt.title("Graph constructed from Matrix")
    plt.savefig(f"{nameG}", format="PNG", dpi=300)


if __name__ == "__main__":
    # Example usage:
    n = 6  # Size of the matrix (n x n)
    A = np.random.randint(0, 5, size=(n, n))  # Random symmetric matrix
    A = (A + A.T) / 2  # Ensure matrix is symmetric
    create_graph_from_matrix(A, nameG="graph_example")
