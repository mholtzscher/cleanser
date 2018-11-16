from cleanser import reddit_quotes, whitespace

sample = """
You are wrong.

> you can't do that in space

Well, astronauts have said stuff.

> would actually harden in space

You are right.
"""


def test_basic():
    text = """> you can't stink in a vacuum
    Hi there."""
    r = reddit_quotes(text)
    assert r == "\n    Hi there."


def test_sample_text():
    r = reddit_quotes(sample)
    r = whitespace(r)
    assert r == "You are wrong. Well, astronauts have said stuff. You are right."
