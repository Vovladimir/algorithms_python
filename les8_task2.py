'''
 Доработать алгоритм Дейкстры (рассматривался на уроке), чтобы он дополнительно возвращал список вершин,
 которые необходимо обойти.
'''

graph = [
    [0, 1, 0, 0, 0],
    [1, 0, 1, 0, 0],
    [0, 1, 0, 1, 1],
    [0, 0, 1, 0, 1],
    [0, 0, 1, 1, 0]
]

def dijkstra(graph, start):

    length = len(graph)
    is_visited = [False] * length
    cost = [float('inf')] * length

    cost[start] = 0
    min_cost = 0
    way = []

    while min_cost < float('inf'):
        is_visited[start] = True
        way.append(start)

        for i, vertex in enumerate(graph[start]):
            if vertex != 0 and not is_visited[i]:
                new_cost = vertex + cost[start]
                if cost[i] > new_cost:
                    cost[i] = new_cost

        min_cost = float('inf')
        for i in range(length):
            if min_cost > cost[i] and not is_visited[i]:
                min_cost = cost[i]
                start = i

    return cost, way


print(dijkstra(graph, 0))

