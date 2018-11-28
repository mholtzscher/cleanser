from cleanser import Cleanser


def test_simple():
    text = ">!spoiler!<"
    expected = "spoiler"
    assert Cleanser(text).reddit_spoilers().text == expected


def test_middle_text():
    text = "In Infinity War >!everyone dies!!<"
    expected = "In Infinity War everyone dies!"
    assert Cleanser(text).reddit_spoilers().text == expected
