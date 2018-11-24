from cleanser.core.reddit import reddit_spoilers


def test_simple():
    result = reddit_spoilers(">!spoiler!<")
    assert result == "spoiler"


def test_middle_text():
    result = reddit_spoilers("In Infinity War >!everyone dies!!<")
    assert result == "In Infinity War everyone dies!"
