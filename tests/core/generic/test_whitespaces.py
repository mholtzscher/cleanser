from cleanser import Cleanser


def test_spaces():
    text = "I have  some extra      spaces.   "
    expected = "I have some extra spaces."
    assert Cleanser(text).whitespaces().text == expected


def test_tabs():
    text = "I have  a tab or two in                me."
    expected = "I have a tab or two in me."
    assert Cleanser(text).whitespaces().text == expected


def test_newline():
    text = "I am a longer piece of text.\n The best food is pizza."
    expected = "I am a longer piece of text. The best food is pizza."
    assert Cleanser(text).whitespaces().text == expected


def test_newlines():
    text = """I am a longer piece of text.
    The best food is pizza.
    I can't write poetry."""
    expected = (
        "I am a longer piece of text. The best food is pizza. I can't write poetry."
    )
    assert Cleanser(text).whitespaces().text == expected


def test_newline_nospaces():
    text = "Hi there.\nI'm Tom."
    expected = "Hi there. I'm Tom."
    assert Cleanser(text).whitespaces().text == expected

    text = "Hi there.\n\nI'm Tom."
    expected = "Hi there. I'm Tom."
    assert Cleanser(text).whitespaces().text == expected
