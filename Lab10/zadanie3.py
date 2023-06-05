from queue import Queue

def BFS(G,s):
    n = len(graph)
    visited = [False] * n
    d = [-1] * n
    p = [-1] * n

    visited[s] = True
    d[s] = 0
    Q = Queue()
    Q.put(s)
    while not Q.empty():
        u = Q.get()

        for v in range(n):
            if G[u][v] == 1 and not visited[v]:
                visited[v] = True
                d[v] = d[u] + 1
                p[v] = u
                Q.put(v)

    return visited, d, p



graph = [
    [0,1,0,1,0,0],
    [0,0,0,0,1,0],
    [0,0,0,0,1,1],
    [1,0,0,0,0,0],
    [0,0,0,1,0,0],
    [0,0,0,0,0,1]
]


visited, distance, parent = BFS(graph,3)

for v in range(len(graph)):
    print(f"Wierzchołek {v}: visited = {visited[v]} distance = {distance[v]}, {parent[v]}")