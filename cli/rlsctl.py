from __future__ import annotations
import os, json, argparse
from rls.driver import DeviceDriver
from rls.topology import Topology
from rls.orchestrator import Orchestrator
from rls.types import ProvisionRequest, PortRef

def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("provision")
    p.add_argument("--src", required=True)       # e.g., A/line0
    p.add_argument("--dst", required=True)
    p.add_argument("--channel", required=True)
    p.add_argument("--power", required=True)
    args = ap.parse_args()

    drv = DeviceDriver(os.getenv("RLS_DEVICE_URL","http://127.0.0.1:8081"))
    topo = Topology(); topo.add_link("A","B"); topo.add_link("B","C")
    orch = Orchestrator(topo, drv)

    src_node, src_port = args.src.split("/",1)
    dst_node, dst_port = args.dst.split("/",1)
    req = ProvisionRequest(PortRef(src_node,src_port), PortRef(dst_node,dst_port),
                           args.channel, args.power)
    result = orch.provision_flow(req)
    print(json.dumps(result))

if __name__ == "__main__":
    main()
