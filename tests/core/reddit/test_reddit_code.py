from cleanser.core.reddit import reddit_code


def test_code():
    text = "One tick `is placed on either side`."
    assert reddit_code(text) == "One tick is placed on either side."
