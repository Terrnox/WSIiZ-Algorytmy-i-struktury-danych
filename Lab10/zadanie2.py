graph1 = {
    'A': ['B', 'E'],
    'B': ['A','C', 'E'],
    'C': ['B','F'],
    'D': ['G','H'],
    'E': ['A','B','F'],
    'F': ['C','E','I'],
    'G': ['D','H'],
    'H': ['D','G'],
    'I': ['F']
}

graph2 = {
    'A': ['B','F'],
    'B': ['C','E'],
    'C': ['D'],
    'D': ['B','H'],
    'E': ['D','G'],
    'F': ['E','G'],
    'G': ['F'],
    'H': ['G']
}


graph = graph2 #Wybór grafu lub zdefiniowanie własnego poprzez słownik
visited = {}
parent = {}
trav_time = {}
dfs_traversal_output = []

for node in graph.keys():
    visited[node] = False
    parent[node] = None
    trav_time[node] = [-1,-1]

time = 0

def dfs_util(u):
    global time
    time = time + 1
    visited[u] = True
    trav_time[u][0] = time
    dfs_traversal_output.append(u)

    for v in graph[u]:
        if visited[v] == False:
            parent[v] = u
            dfs_util(v)

    visited[u] = True
    time = time + 1
    trav_time[u][1] = time


dfs_util("A")
print("Odwiedzone wierzchołki")
print(dfs_traversal_output)
print("Poprzednicy")
print(parent)
print("Czas przedstawiony w secie")
print(trav_time)

print("Poszczególne czasy")
for node in graph.keys():
    print(node, "->", trav_time[node])