from cleanser import Cleanser


def test_basic():
    text = "Python is 👍"
    expected = "Python is "
    assert Cleanser(text).emojis().text == expected


def test_multiple():
    text = "😺😺 Pyt🦃🐉hon is 👌😀😀"
    expected = " Python is "
    assert Cleanser(text).emojis().text == expected


def test_unicode():
    text = u"\U0001F1E6\U0001F1F1Python is \U0001F947"
    expected = "Python is "
    assert Cleanser(text).emojis().text == expected
