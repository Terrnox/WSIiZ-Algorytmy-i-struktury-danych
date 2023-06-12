graph = [
    [0,4,0,0,8,0,0,0,0],
    [4,0,8,0,11,0,0,0,0],
    [0,8,0,7,0,2,0,4,0],
    [0,0,7,0,0,0,0,14,9],
    [8,11,0,0,0,7,1,0,0],
    [0,0,2,0,7,0,6,0,0],
    [0,0,0,0,1,6,0,2,0],
    [0,0,4,14,0,0,2,0,10],
    [0,0,0,9,0,0,0,10,0]
]


def Prim(graph,start):
    sum_of_edges = 0
    n = len(graph)
    visited = [False] * n
    visited[start] = True
    number_of_edges = 0

    while number_of_edges < n - 1:
        mini = float('inf')
        x = 0
        y = 0
        for i in range(n):
            if visited[i] == True:
                for j in range(n):
                    if visited[j] == False and graph[i][j]>0:
                        if mini > graph[i][j]:
                            mini = graph[i][j]
                            x = i
                            y = j

        print(f"Krawedź {x} - {y}: {graph[x][y]}")
        sum_of_edges = sum_of_edges + graph[x][y]
        visited[y] = True
        number_of_edges += 1

    return sum_of_edges


print("Suma wag krawędzi: ",Prim(graph,0))