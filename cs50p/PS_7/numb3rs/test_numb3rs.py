import numb3rs

def test_range():
    assert numb3rs.validate("0.87.110.176") == True
    assert numb3rs.validate("200.220.245.255") == True
    assert numb3rs.validate("200.220.245.256") == False

def test_format():
    assert numb3rs.validate("0.87.110.176") == True
    assert numb3rs.validate(".0.87.110.176") == False
    assert numb3rs.validate("0.87.110.176.") == False
    assert numb3rs.validate("0.87.110.176.11") == False
    assert numb3rs.validate("0.87.110") == False

