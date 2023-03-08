from project import category_validation, generate_incognito, category_words

def test_category_validation():
    assert category_validation('1') == True
    assert category_validation('Food') == True
    assert category_validation('9') == False
    assert category_validation('Cinema') == False

def test_generate_incognito():
    assert generate_incognito('snake') == '_____'
    assert generate_incognito('Abraham Lincoln') == '_______ _______'

def test_category_words():
    test_variable = category_words('Animals','Easy')
    assert len(test_variable) <= 5
    test_variable = category_words('Movies','Medium')
    assert len(test_variable) <= 12 and len(test_variable) >= 6
    test_variable = category_words('Food','Hard')
    assert len(test_variable) >= 11