graph_matrix = [
    [0,4,0,0,0,0,8,0,0],
    [4,0,8,0,0,0,11,0,0],
    [0,8,0,7,2,0,0,0,4],
    [0,0,7,0,0,9,0,0,14],
    [0,0,2,0,0,0,7,6,0],
    [0,0,0,9,0,0,0,0,10],
    [8,11,0,0,7,0,0,1,0],
    [0,0,0,0,6,0,1,0,2],
    [0,0,4,14,0,10,0,2,0]
]

def convert(graph_matrix):
    n = len(graph_matrix)
    ipt = []
    for i in range(n):
        j = i
        while j < n:
            if graph_matrix[i][j]>0:
                ipt.append([i,j,graph_matrix[i][j]])
            j += 1

    return ipt

def add_weight(ipt,result):
    n = len(ipt)
    m = len(result)
    for i in range(n):
        for j in range(m):
            if ipt[i][0] == result[j][0] and ipt[i][1] == result[j][1]:
                result[j].append(ipt[i][2])

    return result

def sort_edges(ipt):
    return ipt[2]

def find(graph,node):
    if graph[node] < 0:
        return node
    else:
        temp = find(graph,graph[node])
        graph[node] = temp
        return temp

def union(graph,a,b,result):
    ta = a
    tb = b
    a = find(graph,a)
    b = find(graph,b)
    if a == b:
        pass
    else:
        result.append([ta,tb])
        if graph[a]<graph[b]:
            graph[a] = graph[a] + graph[b]
            graph[b] = a
        else:
            graph[b] = graph[a] + graph[b]
            graph[a] = b

ipt = convert(graph_matrix)
n = 9
result = []
ipt.sort(key=sort_edges)
graph = [-1] * (n)
for u,v,d in ipt:
    union(graph,u,v,result)

result = add_weight(ipt,result)

for item in result:
    print(f"Krawędź {item[0]} - {item[1]} : {item[2]}")