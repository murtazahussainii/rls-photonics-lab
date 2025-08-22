from __future__ import annotations
from dataclasses import dataclass
import heapq

@dataclass(frozen=True)
class Link:
    a: str
    b: str
    loss_db: float = 0.5

class Topology:
    def __init__(self):
        self.nodes: set[str] = set()
        self.adj: dict[str, list[tuple[str, float]]] = {}

    def add_link(self, a: str, b: str, loss_db: float = 0.5):
        self.nodes |= {a, b}
        self.adj.setdefault(a, []).append((b, loss_db))
        self.adj.setdefault(b, []).append((a, loss_db))

    def shortest_path(self, src: str, dst: str) -> list[str]:
        dist = {n: float("inf") for n in self.nodes}
        prev = {n: None for n in self.nodes}
        dist[src] = 0.0
        pq = [(0.0, src)]
        while pq:
            d, u = heapq.heappop(pq)
            if u == dst: break
            if d != dist[u]: continue
            for v, w in self.adj.get(u, []):
                nd = d + w
                if nd < dist[v]:
                    dist[v] = nd
                    prev[v] = u
                    heapq.heappush(pq, (nd, v))
        if dist[dst] == float("inf"):
            raise ValueError("no path")
        path = []
        cur = dst
        while cur:
            path.append(cur); cur = prev[cur]
        return list(reversed(path))
