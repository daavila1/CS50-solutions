import pytest
from fuel import gauge, convert

def test_fraction():
    assert convert("2/2") == 100
    assert convert("1/2") == 50
    assert convert("1/3") == 33

def test_divzero():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_xgreatery():
    with pytest.raises(ValueError):
        convert("5/2")

def test_str():
    with pytest.raises(ValueError):
        convert("Cat")

def test_E():
    assert gauge(1) == "E"
    assert gauge(0) == "E"

def test_F():
    assert gauge(99) == "F"
    assert gauge(100) == "F"

def test_percent():
    assert gauge(50) == "50%"
    assert gauge(33) == "33%"
    assert gauge(75) == "75%"


