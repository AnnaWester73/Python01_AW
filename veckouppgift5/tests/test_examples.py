from veckouppgift5.examples import add

def test_add():
    expected = 3
    actual = add(1, 2)
    assert actual == expected