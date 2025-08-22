from __future__ import annotations
from typing import Union, Literal
import re

class ParseError(ValueError): ...

def parse_channel(ch: Union[int, str]) -> int:
    if isinstance(ch, int):
        if ch < 0: raise ParseError("channel cannot be negative")
        return ch
    s = str(ch).strip().upper()
    m = re.fullmatch(r"(C)?(\d+)", s)
    if not m:
        raise ParseError(f"invalid channel: {ch!r}")
    return int(m.group(2))

def parse_power(pwr: Union[float, str, Literal["auto"]]) -> Union[float, Literal["auto"]]:
    if isinstance(pwr, (int, float)):
        return float(pwr)
    s = str(pwr).strip().lower()
    if s == "auto":
        return "auto"
    try:
        return float(s)
    except ValueError as e:
        raise ParseError(f"invalid power: {pwr!r}") from e
