from numb3rs import validate

def test_octet_values():
    assert validate('512.512.512.512') == False
    assert validate('9.18.76.74') == True
    assert validate('255.256.256.256') == False

def test_ip_form():
    assert validate('107.') == False
    assert validate('107.100.100.120') == True
    assert validate('107.20.100.200.130.450') == False