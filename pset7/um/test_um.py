from um import count

def test_um_within_a_word():
    assert count(r'yummi') == 0

def test_um_with_special_characters():
    assert count(r'um?') == 1

def test_um_that_counts():
    assert count(r'Um, thanks for the album') == 1
    assert count(r'Um, thanks, um...') == 2