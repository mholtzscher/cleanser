from cleanser import reddit_subreddits


def test_simple():
    r = reddit_subreddits("/r/askreddit is pretty cool.")
    assert " is pretty cool." == r


def test_multiple():
    r = reddit_subreddits("/r/askreddit is pretty cool but r/dankmemes is better.")
    assert " is pretty cool but  is better." == r


def test_short_format():
    r = reddit_subreddits("r/askreddit")
    assert "" == r


def test_long_format():
    r = reddit_subreddits("/r/dankmemes")
    assert "" == r
