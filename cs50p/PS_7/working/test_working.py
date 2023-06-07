import pytest
from working import convert

def test_format():
    assert convert("7 AM to 5 PM") == "07:00 to 17:00"
    assert convert("7:30 AM to 5:30 PM") == "07:30 to 17:30"
    assert convert("7 AM to 5:30 PM") == "07:00 to 17:30"
    with pytest.raises(ValueError):
        convert("1  pm 10  pm")
    with pytest.raises(ValueError):
        convert("1  pm, to 10  pm")

def test_am_pm():
    assert convert("7 AM to 5 PM") == "07:00 to 17:00"

def test_pm_am():
    assert convert("7 PM to 5 AM") == "19:00 to 05:00"

def test_am_am():
    assert convert("7 AM to 11 AM") == "07:00 to 11:00"

def test_pm_pm():
    assert convert("1 PM to 10 PM") == "13:00 to 22:00"

def test_error():
    with pytest.raises(ValueError):
        convert("1  PM to 10 PM")
    with pytest.raises(ValueError):
        convert("130 PM to 10 PM")
    with pytest.raises(ValueError):
        convert("1.30 PM to 10 PM")
    with pytest.raises(ValueError):
        convert("1:60 PM to 10 PM")

def test_outrange():
    with pytest.raises(ValueError):
        convert("24 AM to 25 AM")
    with pytest.raises(ValueError):
        convert("7:60 AM to 5 PM")
    with pytest.raises(ValueError):
        convert("7 AM to 5:70 PM")

