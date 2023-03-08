from jar import Jar

def test_jar_init():
    jar = Jar()

def test_jar_str():
    jar = Jar()
    assert str(jar) == ''
    jar.deposit(6)
    assert str(jar) == '🍪🍪🍪🍪🍪🍪'

def test_jar_deposit():
    jar = Jar(10)
    jar.deposit(9)
    assert jar.size == 9

def test_jar_withdraw():
    jar = Jar(10)
    jar.deposit(9)
    jar.withdraw(6)
    assert jar.size == 3
