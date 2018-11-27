from cleanser import Cleanser


def test_simple():
    r = Cleanser("reddit is pretty ^cool and f^r^e^s^h.").reddit_superscript().text
    assert "reddit is pretty cool and fresh." == r
