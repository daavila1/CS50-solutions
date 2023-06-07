from jar import Jar


def test_init():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0
    jar1 = Jar(12, 5)
    assert jar1.capacity == 12
    assert jar1.size == 5


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(5)
    assert jar.size == 5
    jar.deposit(2)
    assert jar.size == 7
    jar.deposit(0)
    assert jar.size == 7


def test_withdraw():
    jar = Jar(12, 12)
    jar.withdraw(5)
    assert jar.size == 7
    jar.withdraw(7)
    assert jar.size == 0
    jar.withdraw(0)
    assert jar.size == 0