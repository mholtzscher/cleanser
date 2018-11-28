from cleanser import Cleanser


def test_bold():
    text = "Two asterisks **are placed on either side**."
    expected = "Two asterisks are placed on either side."
    assert Cleanser(text).reddit_bold_italics().text == expected


def test_italics():
    text = "One asteric *is placed on either side*."
    expected = "One asteric is placed on either side."
    assert Cleanser(text).reddit_bold_italics().text == expected
