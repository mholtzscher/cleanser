from cleanser import Cleanser


def test_simple():
    text = "/u/spez is pretty cool."
    expected = " is pretty cool."
    assert Cleanser(text).reddit_mentions().text == expected


def test_multiple():
    text = "/u/spez is pretty cool but u/fuckswithducks is better."
    expected = " is pretty cool but  is better."
    assert Cleanser(text).reddit_mentions().text == expected


def test_short_format():
    text = "u/spez"
    expected = ""
    assert Cleanser(text).reddit_mentions().text == expected


def test_long_format():
    text = "/u/spez"
    expected = ""
    assert Cleanser(text).reddit_mentions().text == expected
