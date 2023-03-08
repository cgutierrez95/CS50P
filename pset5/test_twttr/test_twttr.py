from twttr import shorten

def test_upper_lower():
    assert shorten('hello') == 'hll'
    assert shorten('HeLLo wOrld') == 'HLL wrld'

def test_numbers():
    assert shorten('h3ll0 w0rld') == 'h3ll0 w0rld'

def test_punctuation():
    assert shorten('This is cs50!!') == 'Ths s cs50!!'