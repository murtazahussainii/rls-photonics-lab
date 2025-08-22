import pytest, httpx

@pytest.mark.asyncio
async def test_alarm_roundtrip(device_server):
    async with httpx.AsyncClient() as cli:
      await cli.post(f"{device_server}/inject-alarm", json={"node":"B","code":"LOS"})
      r = await cli.get(f"{device_server}/alarms/next", timeout=5.0)
      r.raise_for_status()
      alarm = r.json()
      assert alarm["node"] == "B"
      assert alarm["code"] == "LOS"
