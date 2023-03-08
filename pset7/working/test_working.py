from working import convert
import pytest

def test_incorrect_minutes():
    with pytest.raises(ValueError):
        convert(r'9:60 AM to 5:60 PM')

def test_wrong_separator():
    with pytest.raises(ValueError):
        convert(r'9:00 AM - 5:00 PM')

def test_invalid_time_format():
    with pytest.raises(ValueError):
        convert(r' 3 AM $ 9 P')

def test_incorrect_hour():
    with pytest.raises(ValueError):
        convert(r'09:00 AM to 17:00 PM')

def test_correct_time():
    assert convert(r'10:30 PM to 8:50 AM') == '22:30 to 08:50'
    assert convert(r'10 PM to 8 AM') == '22:00 to 08:00'
    assert convert(r'9:00 AM to 5:00 PM') == '09:00 to 17:00'