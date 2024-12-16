import pytest
import random


@pytest.fixture
def foo():
    my_list = [random.randint(1, 50) for i in range(10)]
    print(my_list)
    print(sorted(my_list))
    print(len(my_list))
    print(sum(my_list))
    return my_list


@pytest.mark.length
def test_length(foo):
    assert len(foo) == 10


@pytest.mark.sort
def test_sort(foo):
    assert sorted(foo) == sorted(foo)


@pytest.mark.range
def test_range(foo):
    for i in foo:
        assert 1 <= i <= 50


@pytest.mark.sum
def test_sum(foo):
    assert sum(foo) > 0


@pytest.mark.odds_evens
def test_odds(foo):
    assert any(i % 2 != 0 for i in foo)


@pytest.mark.odds_evens
def test_evens(foo):
    assert any(i % 2 == 0 for i in foo)


@pytest.mark.negative
def test_negative(foo):
    assert all(i >= 0 for i in foo)


@pytest.mark.range
def test_min_max(foo):
    assert min(foo) >= 1
    assert max(foo) <= 50

