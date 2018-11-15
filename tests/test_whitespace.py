from cleanser import whitespace


def test_spaces():
    text = "I have  some extra      spaces.   "
    assert whitespace(text) == "I have some extra spaces."


def test_tabs():
    text = "I have  a tab or two in                me."
    assert whitespace(text) == "I have a tab or two in me."


def test_newline():
    text = "I am a longer piece of text.\n The best food is pizza."
    assert whitespace(text) == "I am a longer piece of text. The best food is pizza."


def test_newlines():
    text = """I am a longer piece of text.
    The best food is pizza.
    I can't write poetry."""
    assert (
        whitespace(text)
        == "I am a longer piece of text. The best food is pizza. I can't write poetry."
    )
