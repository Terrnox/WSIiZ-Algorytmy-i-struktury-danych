import networkx as nx
import matplotlib.pyplot as plt
import scipy

def create_graph():
    graph_type = input("Jaki chcesz zbudować graf (skierowany, nieskierowany, ważony)? ")
    num_vertices = int(input("Podaj liczbę wierzchołków: "))
    num_edges = int(input("Podaj liczbę krawędzi: "))

    if graph_type == "skierowany":
        G = nx.DiGraph()
    elif graph_type == "nieskierowany":
        G = nx.Graph()
    elif graph_type == "ważony":
        G = nx.Graph()
    else:
        print("Nieznany typ grafu.")
        return

    for i in range(num_vertices):
        G.add_node(i)

    print("Podaj krawędzie w formacie: 'start end weight' (dla ważonych) lub 'start end' (dla nieważonych)")
    for i in range(num_edges):
        edge = input("Podaj krawędź: ").split()

        if graph_type == "ważony":
            G.add_edge(int(edge[0]), int(edge[1]), weight=int(edge[2]))
        else:
            G.add_edge(int(edge[0]), int(edge[1]))

    print("\nMacierz sąsiedztwa:")
    print(nx.adjacency_matrix(G).todense())

    print("\nLista sąsiedztwa:")
    for line in nx.generate_adjlist(G):
        print(line)

    nx.draw(G, with_labels=True)
    plt.show()


create_graph()