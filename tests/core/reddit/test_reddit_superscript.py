from cleanser import Cleanser


def test_simple():
    text = "reddit is pretty ^cool and f^r^e^s^h."
    expected = "reddit is pretty cool and fresh."
    assert Cleanser(text).reddit_superscript().text == expected
