from cleanser import Cleanser
import html

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


def test_unescaped_quote_symobl():
    text = """&gt; you can't stink in a vacuum
    Hi there."""
    expected = "Hi there."
    assert Cleanser(text).unescape_html().reddit_quotes().whitespaces().text == expected


def test_sample_text():
    expected = "You are wrong. Well, astronauts have said stuff. You are right."
    assert Cleanser(SAMPLE).reddit_quotes().whitespaces().text == expected


def test_content_removal():
    expected = "You are wrong. you can't do that in space Well, astronauts have said stuff. would actually harden in space You are right."
    result = Cleanser(SAMPLE).reddit_quotes(content_removal=False).whitespaces().text
    assert result == expected
