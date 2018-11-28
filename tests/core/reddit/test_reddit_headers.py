from cleanser import Cleanser


def test_single():
    text = "#This is an example H1 Header"
    expected = "This is an example H1 Header"
    assert Cleanser(text).reddit_headers().text == expected


def test_double():
    text = "##This is an example H2 Header"
    expected = "This is an example H2 Header"
    assert Cleanser(text).reddit_headers().text == expected


def test_triple():
    text = "###This is an example H3 Header"
    expected = "This is an example H3 Header"
    assert Cleanser(text).reddit_headers().text == expected
