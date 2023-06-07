import pytest
from um import count

def test_normal():
    assert count("um um um um") == 4
    assert count("uM UM um Um") == 4
    assert count("um, um, um,") == 3
    assert count("um...") == 1

def test_words():
    assert count("tumblr") == 0
    assert count("cum") == 0
    assert count("instrumentation") == 0
    assert count("ummm") == 0

def test_expressions():
    assert count("hello, um, um, world ") == 2
    assert count("um, my favourtite social network, is um, tumblr") == 2

def text_insensitive():
    assert count("UM, this is a great UMbrella") == 1
    assert count("Um") == 1
    assert count("uM") == 1
    assert count("um") == 1