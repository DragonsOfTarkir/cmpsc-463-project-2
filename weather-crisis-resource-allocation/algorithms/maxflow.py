from collections import deque

def bfs(capacity, source, sink, parent):
    visited = [False] * len(capacity)
    queue = deque([source])
    visited[source] = True

    while queue:
        u = queue.popleft()
        for v in range(len(capacity)):
            if not visited[v] and capacity[u][v] > 0:
                queue.append(v)
                visited[v] = True
                parent[v] = u
                if v == sink:
                    return True
    return False


def max_flow(capacity, source, sink):
    parent = [-1] * len(capacity)
    max_flow_value = 0

    while bfs(capacity, source, sink, parent):
        path_flow = float('inf')
        v = sink

        # Find bottleneck
        while v != source:
            u = parent[v]
            path_flow = min(path_flow, capacity[u][v])
            v = u

        # Update capacities
        v = sink
        while v != source:
            u = parent[v]
            capacity[u][v] -= path_flow
            capacity[v][u] += path_flow
            v = u

        max_flow_value += path_flow

    return max_flow_value
