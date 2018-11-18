from cleanser.core.reddit import reddit_headers


def test_single():
    r = reddit_headers("#This is an example H1 Header")
    assert "This is an example H1 Header" == r


def test_double():
    r = reddit_headers("##This is an example H2 Header")
    assert "This is an example H2 Header" == r


def test_triple():
    r = reddit_headers("###This is an example H3 Header")
    assert "This is an example H3 Header" == r
