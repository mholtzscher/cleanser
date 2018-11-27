from cleanser import Cleanser


def test_simple():
    r = Cleanser("/r/askreddit is pretty cool.").reddit_subreddits().text
    assert " is pretty cool." == r


def test_multiple():
    r = (
        Cleanser("/r/askreddit is pretty cool but r/dankmemes is better.")
        .reddit_subreddits()
        .text
    )
    assert " is pretty cool but  is better." == r


def test_short_format():
    r = Cleanser("r/askreddit").reddit_subreddits().text
    assert "" == r


def test_long_format():
    r = Cleanser("/r/dankmemes").reddit_subreddits().text
    assert "" == r
