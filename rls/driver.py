from __future__ import annotations
import httpx

class DeviceDriver:
    def __init__(self, base_url: str):
        self.base_url = base_url.rstrip("/")

    def set_channel(self, node: str, port: str, channel: int) -> None:
        r = httpx.put(f"{self.base_url}/config/{node}/{port}", json={"channel": channel}, timeout=5.0)
        r.raise_for_status()

    def set_power(self, node: str, port: str, power: float) -> None:
        r = httpx.put(f"{self.base_url}/config/{node}/{port}", json={"power": power}, timeout=5.0)
        r.raise_for_status()

    def get_state(self, node: str, port: str) -> dict:
        r = httpx.get(f"{self.base_url}/state/{node}/{port}", timeout=5.0)
        r.raise_for_status()
        return r.json()
