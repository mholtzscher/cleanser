from cleanser.core.reddit import reddit_strikethrough


def test_strikethrough():
    result = reddit_strikethrough("~~An example of strikethrough~~I should remain.")
    assert result == "I should remain."


def test_no_strikethrough_single_tilde():
    result = reddit_strikethrough("~This is not an example of strikethrough~")
    assert result == "~This is not an example of strikethrough~"


def test_no_strikethrough():
    result = reddit_strikethrough("There are ~2 lbs in a kilogram")
    assert result == "There are ~2 lbs in a kilogram"
