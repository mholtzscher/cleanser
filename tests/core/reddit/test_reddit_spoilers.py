from cleanser import Cleanser


def test_simple():
    result = Cleanser(">!spoiler!<").reddit_spoilers().text
    assert result == "spoiler"


def test_middle_text():
    result = Cleanser("In Infinity War >!everyone dies!!<").reddit_spoilers().text
    assert result == "In Infinity War everyone dies!"
