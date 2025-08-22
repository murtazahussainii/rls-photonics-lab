import subprocess, time, os, signal, pytest

@pytest.fixture(scope="session")
def device_server():
    proc = subprocess.Popen(["uvicorn", "device_sim.app:app", "--port", "8081"])
    time.sleep(0.8)
    yield "http://127.0.0.1:8081"
    os.kill(proc.pid, signal.SIGTERM)

@pytest.fixture
def driver(device_server):
    from rls.driver import DeviceDriver
    return DeviceDriver(device_server)

@pytest.fixture
def topo():
    from rls.topology import Topology
    t = Topology()
    t.add_link("A", "B", 0.5)
    t.add_link("B", "C", 0.5)
    return t
