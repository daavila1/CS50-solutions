from bank import value

def test_0():
    assert value("hello") == 0
    assert value(" helLo   ") == 0
    assert value(" HELLO   ") == 0



def test_20():
    assert value("hi") == 20
    assert value("HI") == 20
    assert value("hI        ") == 20


def test_100():
    assert value("what's up?") == 100
    assert value("WHAT'S UP     ?") == 100
    assert value("        WhAT's Up     ?") == 100

