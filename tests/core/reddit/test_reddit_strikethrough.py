from cleanser import Cleanser


def test_strikethrough():
    text = "~~An example of strikethrough~~I should remain."
    expected = "I should remain."
    assert Cleanser(text).reddit_strikethrough().text == expected


def test_no_strikethrough_single_tilde():
    text = "~This is not an example of strikethrough~"
    expected = "~This is not an example of strikethrough~"
    assert Cleanser(text).reddit_strikethrough().text == expected


def test_no_strikethrough():
    text = "There are ~2 lbs in a kilogram"
    expected = "There are ~2 lbs in a kilogram"
    assert Cleanser(text).reddit_strikethrough().text == expected
