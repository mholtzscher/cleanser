from cleanser import all


def test_basic():
    text = ""
    assert all(text) == ""
