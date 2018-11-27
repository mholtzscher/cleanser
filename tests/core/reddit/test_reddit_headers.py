from cleanser import Cleanser


def test_single():
    r = Cleanser("#This is an example H1 Header").reddit_headers().text
    assert "This is an example H1 Header" == r


def test_double():
    r = Cleanser("##This is an example H2 Header").reddit_headers().text
    assert "This is an example H2 Header" == r


def test_triple():
    r = Cleanser("###This is an example H3 Header").reddit_headers().text
    assert "This is an example H3 Header" == r
