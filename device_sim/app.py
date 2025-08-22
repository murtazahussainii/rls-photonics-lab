from __future__ import annotations
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict, Any
import asyncio

app = FastAPI(title="RLS Device Sim")

class PortCfg(BaseModel):
    channel: int | None = None
    power: float | None = None

DB_PORTS: Dict[str, Dict[str, Any]] = {
    "A": {"line0": {"cfg": {}, "state": {}}},
    "B": {"line0": {"cfg": {}, "state": {}}},
    "C": {"line0": {"cfg": {}, "state": {}}},
}

ALARM_QUEUE: asyncio.Queue[dict] = asyncio.Queue()

@app.get("/nodes")
def nodes(): return list(DB_PORTS.keys())

@app.get("/ports/{node}")
def list_ports(node: str):
    if node not in DB_PORTS: raise HTTPException(404, "node not found")
    return list(DB_PORTS[node].keys())

@app.put("/config/{node}/{port}")
def set_cfg(node: str, port: str, cfg: PortCfg):
    try:
        DB_PORTS[node][port]["cfg"].update(cfg.model_dump(exclude_none=True))
    except KeyError:
        raise HTTPException(404, "port not found")
    return {"ok": True}

@app.get("/state/{node}/{port}")
def get_state(node: str, port: str):
    try:
        return {"cfg": DB_PORTS[node][port]["cfg"], "state": DB_PORTS[node][port]["state"]}
    except KeyError:
        raise HTTPException(404, "port not found")

@app.post("/inject-alarm")
async def inject_alarm(payload: dict):
    await ALARM_QUEUE.put(payload)
    return {"queued": True}

@app.get("/alarms/next")
async def next_alarm():
    alarm = await ALARM_QUEUE.get()
    return alarm
