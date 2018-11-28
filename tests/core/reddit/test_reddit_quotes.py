from cleanser import Cleanser

SAMPLE = """
You are wrong.

> you can't do that in space

Well, astronauts have said stuff.

> would actually harden in space

You are right.
"""


def test_basic():
    text = """> you can't stink in a vacuum
    Hi there."""
    expected = "\n    Hi there."
    assert Cleanser(text).reddit_quotes().text == expected


def test_sample_text():
    expected = "You are wrong. Well, astronauts have said stuff. You are right."
    assert Cleanser(SAMPLE).reddit_quotes().whitespaces().text == expected
