from cleanser import emoji


def test_basic():
    assert emoji("Python is 👍") == "Python is "


def test_multiple():
    assert emoji("😺😺 Pyt🦃🐉hon is 👌😀😀") == " Python is "


def test_unicode():
    assert emoji(u"\U0001F1E6\U0001F1F1Python is \U0001F947") == "Python is "
