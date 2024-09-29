from splti import my_demo


def test_happy():
    res = my_demo.get_important_stuff()

    assert len(res) == my_demo.N
    assert min(res) >= my_demo.LOW
    assert max(res) <= my_demo.HIGH
    for i in res:
        assert isinstance(i, int)
