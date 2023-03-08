from fuel import convert, gauge
import pytest

def test_convert():
    assert convert('1/2') == 50
    assert convert('1/4') == 25
    with pytest.raises(ZeroDivisionError):
        convert('1/0')
    with pytest.raises(ValueError):
        convert('3/2')

def test_gauge():
    assert gauge(50) == '50%'
    assert gauge(25) == '25%'
    assert gauge(99) == 'F'
    assert gauge(1) == 'E'