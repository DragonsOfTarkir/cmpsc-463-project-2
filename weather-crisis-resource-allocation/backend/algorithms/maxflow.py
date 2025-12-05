"""
maxflow.py

Compute maximum flow between a source and sink using Edmonds-Karp (BFS-based Ford-Fulkerson).

Provides:
- compute_max_flow(capacity=None, source=0, sink=None)
  * capacity (optional): square adjacency matrix (list of lists) where capacity[u][v] is capacity from u to v
  * if capacity is None, a sample capacity matrix is used
  * source default 0, sink defaults to last node
  * returns {"max_flow": value, "flow_matrix": flow_matrix}

Implementation detail:
- Edmonds-Karp uses BFS to find shortest augmenting paths (by number of edges).
- The function returns both the numeric max flow and the flow matrix describing flow sent along each edge.
"""

from collections import deque
from typing import List, Optional, Dict


def _bfs(residual: List[List[float]], source: int, sink: int, parent: List[int]) -> bool:
    """
    BFS on residual graph to find augmenting path. Fills parent[] with path.
    Returns True if sink is reachable from source.
    """
    n = len(residual)
    visited = [False] * n
    q = deque()
    q.append(source)
    visited[source] = True
    parent[source] = -1

    while q:
        u = q.popleft()
        for v in range(n):
            if not visited[v] and residual[u][v] > 1e-9:  # allow float tolerances
                visited[v] = True
                parent[v] = u
                q.append(v)
                if v == sink:
                    return True
    return False


def edmonds_karp(capacity: List[List[float]], source: int, sink: int) -> (float, List[List[float]]):
    """
    Edmonds-Karp algorithm returning (max_flow_value, flow_matrix)
    capacity: adjacency matrix
    """
    n = len(capacity)
    # Make residual copy (float)
    residual = [[float(capacity[i][j]) for j in range(n)] for i in range(n)]
    parent = [-1] * n
    max_flow = 0.0

    # flow_matrix: track flow sent from u to v (for output)
    flow = [[0.0] * n for _ in range(n)]

    while _bfs(residual, source, sink, parent):
        # Find minimum residual capacity along the path found by BFS
        path_flow = float("inf")
        s = sink
        while s != source:
            path_flow = min(path_flow, residual[parent[s]][s])
            s = parent[s]

        # Update residual capacities and flow matrix
        v = sink
        while v != source:
            u = parent[v]
            residual[u][v] -= path_flow
            residual[v][u] += path_flow

            # update flow: increase u->v, decrease v->u to reflect net flow
            flow[u][v] += path_flow
            flow[v][u] -= path_flow

            v = parent[v]

        max_flow += path_flow

    return max_flow, flow


def compute_max_flow(capacity: Optional[List[List[float]]] = None, source: int = 0, sink: Optional[int] = None) -> Dict:
    """
    Compute max flow. If capacity is None, uses a sample graph.

    Sample capacity matrix (directed graph) example (4 nodes):
       Node indices: 0 (source), 1, 2, 3 (sink)
    capacity = [
      [0, 16, 13, 0],
      [0, 0, 10, 12],
      [0, 4, 0, 14],
      [0, 0, 0, 0]
    ]

    Returns:
      {
        "max_flow": 23.0,
        "flow_matrix": [[...], ...],
        "n": number_of_nodes
      }
    """
    if capacity is None:
        capacity = [
            [0, 16, 13, 0],
            [0, 0, 10, 12],
            [0, 4, 0, 14],
            [0, 0, 0, 0]
        ]

    n = len(capacity)
    if n == 0:
        return {"max_flow": 0.0, "flow_matrix": [], "message": "Empty capacity matrix."}

    if sink is None:
        sink = n - 1

    if source < 0 or source >= n or sink < 0 or sink >= n:
        return {"error": "Invalid source or sink index."}

    max_flow_value, flow_matrix = edmonds_karp(capacity, source, sink)

    # Convert tiny float rounding errors to exact zeros and to floats with reasonable precision
    for i in range(n):
        for j in range(n):
            # if value very close to integer, round it to integer
            val = flow_matrix[i][j]
            if abs(val - round(val)) < 1e-9:
                flow_matrix[i][j] = float(round(val))
            else:
                # keep a limited precision
                flow_matrix[i][j] = float(round(val, 6))

    return {"max_flow": float(round(max_flow_value, 6)), "flow_matrix": flow_matrix, "n": n}
