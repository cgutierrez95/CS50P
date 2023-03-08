from bank import value

def test_return_0():
    assert value('hello') == 0
    assert value('Hello') == 0

def test_return_20():
    assert value('hi') == 20
    assert value('Howdy') == 20

def test_return_100():
    assert value('Morning') == 100
    assert value('Buenas') == 100