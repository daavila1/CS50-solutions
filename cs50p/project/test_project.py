import pytest
import project

def test_get_type():
    assert project.get_type("yes") == "yes"
    assert project.get_type("no") == "no"
    with pytest.raises(ValueError):
        project.get_type("random input")

def test_generate():
    password = project.generate("asdf", "123", "***", 12)
    assert len(password) == 12
    assert isinstance(password, list)

def test_get_parameter(monkeypatch):
    #test alphabetic characters
    monkeypatch.setattr('builtins.input', lambda _: "asd")
    assert project.get_parameter(0) == "asd"

    monkeypatch.setattr('builtins.input', lambda _: "a123b")
    with pytest.raises(ValueError):
        project.get_parameter(0)

    #test numeric characters
    monkeypatch.setattr('builtins.input', lambda _: "123")
    assert project.get_parameter(1) == "123"

    monkeypatch.setattr('builtins.input', lambda _: "a1s2d")
    with pytest.raises(ValueError):
        project.get_parameter(1)

    #test symbols
    monkeypatch.setattr('builtins.input', lambda _: "+*.,;")
    assert project.get_parameter(2) == "+*.,;"

    monkeypatch.setattr('builtins.input', lambda _: "+a1s2d*")
    with pytest.raises(ValueError):
        project.get_parameter(2)

    #test lenght
    monkeypatch.setattr('builtins.input', lambda _: "12")
    assert project.get_parameter(3) == "12"

    monkeypatch.setattr('builtins.input', lambda _: "+a1s2d*")
    with pytest.raises(ValueError):
        project.get_parameter(3)
