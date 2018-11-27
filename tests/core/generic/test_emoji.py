from cleanser import Cleanser


def test_basic():
    assert Cleanser("Python is 👍").emoji().text == "Python is "


def test_multiple():
    assert Cleanser("😺😺 Pyt🦃🐉hon is 👌😀😀").emoji().text == " Python is "


def test_unicode():
    assert (
        Cleanser(u"\U0001F1E6\U0001F1F1Python is \U0001F947").emoji().text
        == "Python is "
    )
