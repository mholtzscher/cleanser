from cleanser import Cleanser


def test_simple():
    text = "/r/askreddit is pretty cool."
    expected = " is pretty cool."
    assert Cleanser(text).reddit_subreddits().text == expected


def test_multiple():
    text = "/r/askreddit is pretty cool but r/dankmemes is better."
    expected = " is pretty cool but  is better."
    assert Cleanser(text).reddit_subreddits().text == expected


def test_short_format():
    text = "r/askreddit"
    expected = ""
    assert Cleanser(text).reddit_subreddits().text == expected


def test_long_format():
    text = "/r/dankmemes"
    expected = ""
    assert Cleanser(text).reddit_subreddits().text == expected
