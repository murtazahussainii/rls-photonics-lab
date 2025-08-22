from __future__ import annotations
from .types import ProvisionRequest
from .parsing import parse_channel, parse_power
from .topology import Topology

class Orchestrator:
    def __init__(self, topo: Topology, driver):
        self.topo = topo
        self.driver = driver

    def provision_flow(self, req: ProvisionRequest) -> dict:
        ch = parse_channel(req.channel)
        pwr = parse_power(req.power)
        path = self.topo.shortest_path(req.src.node, req.dst.node)
        for node in path:
            port = "line0"
            self.driver.set_channel(node, port, ch)
            if pwr != "auto":
                self.driver.set_power(node, port, float(pwr))
        return {"ok": True, "path": path, "channel": ch, "power": pwr}
