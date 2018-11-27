from cleanser import Cleanser


def test_simple():
    r = Cleanser("/u/spez is pretty cool.").reddit_mentions().text
    assert " is pretty cool." == r


def test_multiple():
    r = (
        Cleanser("/u/spez is pretty cool but u/fuckswithducks is better.")
        .reddit_mentions()
        .text
    )
    assert " is pretty cool but  is better." == r


def test_short_format():
    r = Cleanser("u/spez").reddit_mentions().text
    assert "" == r


def test_long_format():
    r = Cleanser("/u/spez").reddit_mentions().text
    assert "" == r
