"""
mst.py

Compute a Minimum Spanning Tree (MST) for an undirected weighted graph.

Provides:
- compute_mst(graph=None)
  * graph (optional) should be a dict: {"nodes": [...], "edges": [(u, v, weight), ...]}
  * if graph is None, a sample graph is used
  * returns {"mst_edges": [(u, v, w), ...], "total_cost": sum_w}

Implementation: Kruskal's algorithm with Union-Find (Disjoint Set Union).
"""

from typing import List, Tuple, Dict, Optional


class UnionFind:
    """Simple Union-Find with path compression and union by rank."""
    def __init__(self, elements):
        self.parent = {e: e for e in elements}
        self.rank = {e: 0 for e in elements}

    def find(self, x):
        # Path compression
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return False
        # union by rank
        if self.rank[rx] < self.rank[ry]:
            self.parent[rx] = ry
        else:
            self.parent[ry] = rx
            if self.rank[rx] == self.rank[ry]:
                self.rank[rx] += 1
        return True


def kruskal(nodes: List, edges: List[Tuple], debug: bool = False) -> Tuple[List[Tuple], float]:
    """
    Run Kruskal's algorithm.
    edges: list of tuples (u, v, weight)
    returns: (mst_edges, total_cost)
    """
    # Sort edges by weight
    edges_sorted = sorted(edges, key=lambda e: e[2])
    uf = UnionFind(nodes)

    mst = []
    total_cost = 0.0

    for u, v, w in edges_sorted:
        if uf.union(u, v):
            mst.append((u, v, w))
            total_cost += w
            if debug:
                print(f"Added edge {(u, v, w)} to MST")

        # early stop if mst size == nodes-1
        if len(mst) == len(nodes) - 1:
            break

    return mst, total_cost


def compute_mst(graph: Optional[Dict] = None, debug: bool = False) -> Dict:
    """
    Compute MST for given graph. If graph is None, use a sample graph.

    Expected graph format:
    {
      "nodes": ["A", "B", "C", ...],
      "edges": [
         ("A","B", 5.0),
         ("B","C", 3.2),
         ...
      ]
    }

    Returns:
    {
      "mst_edges": [("A","B",5.0), ...],
      "total_cost": 13.2
    }
    """
    if graph is None:
        # Sample graph (undirected)
        graph = {
            "nodes": ["A", "B", "C", "D", "E"],
            "edges": [
                ("A", "B", 4),
                ("A", "C", 2),
                ("B", "C", 1),
                ("B", "D", 5),
                ("C", "D", 8),
                ("C", "E", 10),
                ("D", "E", 2),
            ],
        }

    nodes = graph.get("nodes", [])
    edges = graph.get("edges", [])

    if not nodes:
        return {"mst_edges": [], "total_cost": 0.0, "message": "Graph contains no nodes."}

    # Run Kruskal
    mst_edges, total_cost = kruskal(nodes, edges, debug=debug)

    # Basic connectivity check: a valid MST should have len(nodes)-1 edges if graph was connected
    if len(mst_edges) != max(0, len(nodes) - 1):
        return {
            "mst_edges": mst_edges,
            "total_cost": total_cost,
            "warning": "Graph appears disconnected; returned a forest (MST for each connected component)."
        }

    return {"mst_edges": mst_edges, "total_cost": total_cost}

