import pytest
import random
numbers = [1,2,3]

@pytest.mark.ui
def test_1():
    assert 1 == 1

@pytest.mark.api
def test_2():
    assert 1 == 1


def test_3():
    assert 1 == 1

@pytest.mark.smoke
def test_flaky():
    assert 1 == random.choice(numbers)
