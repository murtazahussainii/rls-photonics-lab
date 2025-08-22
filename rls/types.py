from __future__ import annotations
from dataclasses import dataclass
from typing import Literal, Union

Channel = Union[int, str]                 # e.g., 47 or "C47"
Power = Union[float, Literal["auto"]]     # dBm or "auto"

@dataclass(frozen=True)
class PortRef:
    node: str
    port: str  # e.g., "line0"

@dataclass
class ProvisionRequest:
    src: PortRef
    dst: PortRef
    channel: Channel
    power: Power
