from cleanser.core.reddit import reddit_bold_italics


def test_bold():
    text = "Two asterisks **are placed on either side**."
    assert reddit_bold_italics(text) == "Two asterisks are placed on either side."


def test_italics():
    text = "One asteric *is placed on either side*."
    assert reddit_bold_italics(text) == "One asteric is placed on either side."
