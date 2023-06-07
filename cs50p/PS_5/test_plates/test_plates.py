from plates import is_valid


def test_letters():
    assert is_valid("as") == True
    assert is_valid("asd") == True
    assert is_valid("a") == False
    assert is_valid("a2") == False


def test_len():
    assert is_valid("as") == True
    assert is_valid("asdfgh") == True
    assert is_valid("a") == False
    assert is_valid("asdfghj") == False


def test_numbers():
    assert is_valid("aaa222") == True
    assert is_valid("aa22aa") == False

def test_cero():
    assert is_valid("aaa100") == True
    assert is_valid("aaa001") == False

def test_puntuation():
    assert is_valid("PI3.14") == False
    assert is_valid("PI3!14") == False
    assert is_valid("PI3 14") == False
