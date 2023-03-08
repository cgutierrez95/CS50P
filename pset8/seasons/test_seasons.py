from seasons import convert
import pytest

def test_invalid_date():
    with pytest.raises(SystemExit):
        convert('1995/10/10')

def test_valid_date():
    assert convert('1995-10-10') == 'Fourteen million, two hundred ninety-six thousand, three hundred twenty minutes'
