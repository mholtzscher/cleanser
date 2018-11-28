from cleanser import Cleanser


def test():
    b = Cleanser("Hello World")
    assert repr(b) == "Cleanser('Hello World')"
    assert str(b) == "Hello World"
