from twttr import shorten

def test_normaltext():
    assert shorten("twitter") == "twttr"

def text_novowelstext():
    assert shorten("jst d t") == "jst d it"

def test_uppertext():
    assert shorten("APPLE") == "PPL"

def test_numbertext():
    assert shorten("0092twitter212") == "0092twttr212"

def test_puntuation():
    assert shorten("hello, world.") == "hll, wrld."
