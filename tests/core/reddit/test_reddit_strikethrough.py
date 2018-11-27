from cleanser import Cleanser


def test_strikethrough():
    result = (
        Cleanser("~~An example of strikethrough~~I should remain.")
        .reddit_strikethrough()
        .text
    )
    assert result == "I should remain."


def test_no_strikethrough_single_tilde():
    result = (
        Cleanser("~This is not an example of strikethrough~")
        .reddit_strikethrough()
        .text
    )
    assert result == "~This is not an example of strikethrough~"


def test_no_strikethrough():
    result = Cleanser("There are ~2 lbs in a kilogram").reddit_strikethrough().text
    assert result == "There are ~2 lbs in a kilogram"
