from cleanser.core.reddit import reddit_superscript


def test_simple():
    r = reddit_superscript("reddit is pretty ^cool and f^r^e^s^h.")
    assert "reddit is pretty cool and fresh." == r
