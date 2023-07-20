from api import get_fact


def test_api(n=10):
    assert get_fact(n) != -1 
