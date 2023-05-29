graph1 = {
    "0":{"1":5,"2":10},
    "1":{"2":3,"3":2,"4":9},
    "2":{"1":2,"4":1},
    "3":{"0":7,"4":6},
    "4":{"3":4}
}

graph2 = {
    "0":{"1":5,"2":3},
    "1":{"2":1,"3":6,"4":4},
    "2":{"1":2,"4":6},
    "3":{"0":3,"4":7},
    "4":{"3":2}
}

def get_cheapest_node(costs_dict, processed_list):
    cheapest_cost = float("inf")
    cheapest_key = None

    for name,cost in costs_dict.items():
        if name not in processed_list and cost < cheapest_cost:
            cheapest_cost = cost
            cheapest_key = name

    return cheapest_key

graph = graph2
costs={}
parents={}

for name in graph.keys():
    costs[name]=float("inf")

processed = []
current_node = "0"
costs[current_node] = 0
parents[current_node] = None

while current_node:

    for neighbour in graph[current_node]:
        if costs[neighbour] > costs[current_node] + graph[current_node][neighbour]:
            costs[neighbour] = costs[current_node] + graph[current_node][neighbour]
            parents[neighbour] = current_node

    processed.append(current_node)
    current_node = get_cheapest_node(costs,processed)

for d,c in costs.items():
    print(f"Koszt dla {d} to {c}")

    current_d = d
    while(parents[current_d]):
        print(current_d)
        current_d = parents[current_d]
    else:
        print(current_d)