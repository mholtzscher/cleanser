from cleanser import purify


def test_remove_all():
    text = """Hi there.\nI'm Tom."""
    assert purify(text, reddit=True) == "Hi there. I'm Tom."


def test_disable_whitespace():
    text = """Hi  there.\nI'm Tom."""
    assert purify(text, whitespaces=False) == "Hi  there.\nI'm Tom."
