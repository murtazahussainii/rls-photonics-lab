import pytest
from rls.parsing import parse_channel, parse_power, ParseError

@pytest.mark.parametrize("raw,exp", [(47,47), ("47",47), ("c47",47), ("C47",47)])
def test_parse_channel_ok(raw,exp):
    assert parse_channel(raw) == exp

@pytest.mark.parametrize("raw", ["X47","", -1])
def test_parse_channel_bad(raw):
    with pytest.raises(ParseError): parse_channel(raw)

@pytest.mark.parametrize("raw,exp", [(0.0,0.0), ("-3.2",-3.2), ("auto","auto")])
def test_parse_power_ok(raw,exp):
    assert parse_power(raw) == exp

def test_parse_power_bad():
    with pytest.raises(ParseError): parse_power("loud")
