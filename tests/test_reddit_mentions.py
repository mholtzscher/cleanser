from cleanser import reddit_mentions


def test_simple():
    r = reddit_mentions("/u/spez is pretty cool.")
    assert " is pretty cool." == r


def test_multiple():
    r = reddit_mentions("/u/spez is pretty cool but u/fuckswithducks is better.")
    assert " is pretty cool but  is better." == r


def test_short_format():
    r = reddit_mentions("u/spez")
    assert "" == r


def test_long_format():
    r = reddit_mentions("/u/spez")
    assert "" == r
