from cleanser import Cleanser


def test_periods():
    text = "Python is awesome.."
    expected = "Python is awesome."
    assert Cleanser(text).double_punctuation().text == expected

    text = "Python is awesome....."
    expected = "Python is awesome."
    assert Cleanser(text).double_punctuation().text == expected


def test_question_marks():
    text = "Python is awesome??"
    expected = "Python is awesome?"
    assert Cleanser(text).double_punctuation().text == expected

    text = "Python is awesome????????"
    expected = "Python is awesome?"
    assert Cleanser(text).double_punctuation().text == expected


def test_exclamations():
    text = "Python is awesome!!"
    expected = "Python is awesome!"
    assert Cleanser(text).double_punctuation().text == expected

    text = "Python is awesome!!!!!"
    expected = "Python is awesome!"
    assert Cleanser(text).double_punctuation().text == expected


def test_commas():
    text = "Python,, is awesome,,"
    expected = "Python, is awesome,"
    assert Cleanser(text).double_punctuation().text == expected

    text = "Python,,,,,, is awesome"
    expected = "Python, is awesome"
    assert Cleanser(text).double_punctuation().text == expected


def test_colon():
    text = "Python:: is awesome"
    expected = "Python: is awesome"
    assert Cleanser(text).double_punctuation().text == expected

    text = "Python:::::: is awesome"
    expected = "Python: is awesome"
    assert Cleanser(text).double_punctuation().text == expected


def test_semi_colon():
    text = "Python;; is awesome"
    expected = "Python; is awesome"
    assert Cleanser(text).double_punctuation().text == expected

    text = "Python;;;;;; is awesome"
    expected = "Python; is awesome"
    assert Cleanser(text).double_punctuation().text == expected


def test_asterisk():
    text = "Python** is awesome"
    expected = "Python* is awesome"
    assert Cleanser(text).double_punctuation().text == expected

    text = "Python****** is awesome"
    expected = "Python* is awesome"
    assert Cleanser(text).double_punctuation().text == expected
