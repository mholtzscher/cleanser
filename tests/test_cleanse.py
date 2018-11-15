from cleanser import cleanse


def test_basic():
    text = ""
    assert cleanse(text) == ""
