from rls.types import ProvisionRequest, PortRef
from rls.orchestrator import Orchestrator

def test_provision_happy_path(topo, driver):
    orch = Orchestrator(topo, driver)
    req = ProvisionRequest(
        src=PortRef("A","line0"),
        dst=PortRef("C","line0"),
        channel="C47",
        power="auto"
    )
    res = orch.provision_flow(req)
    assert res["ok"] is True
    assert res["path"] == ["A","B","C"]
    assert res["channel"] == 47
