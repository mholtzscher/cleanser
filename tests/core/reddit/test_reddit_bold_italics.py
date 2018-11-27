from cleanser import Cleanser


def test_bold():
    text = "Two asterisks **are placed on either side**."
    assert (
        Cleanser(text).reddit_bold_italics().text
        == "Two asterisks are placed on either side."
    )


def test_italics():
    text = "One asteric *is placed on either side*."
    assert (
        Cleanser(text).reddit_bold_italics().text
        == "One asteric is placed on either side."
    )
