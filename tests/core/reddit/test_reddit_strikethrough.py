from cleanser.core.reddit import reddit_strikethrough


def test_strikethrough():
    r = reddit_strikethrough("~~This is an example of strikethrough~~")
    assert "This is an example of strikethrough" == r


def test_no_strikethrough_single_tilde():
    r = reddit_strikethrough("~This is not an example of strikethrough~")
    assert "~This is not an example of strikethrough~" == r


def test_no_strikethrough():
    r = reddit_strikethrough("There are ~2 lbs in a kilogram")
    assert "There are ~2 lbs in a kilogram" == r
