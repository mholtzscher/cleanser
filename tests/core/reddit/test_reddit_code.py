from cleanser import Cleanser


def test_code():
    text = "One tick `is placed on either side`."
    assert Cleanser(text).reddit_code().text == "One tick is placed on either side."
