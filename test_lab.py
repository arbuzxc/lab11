# Николенко 107б
import pytest
from lab import multiply, divide, distance, quadratic, geometric_sum


def test_multiply():
    assert multiply(2, 3) == 6


def test_divide():
    assert divide(6, 3) == 2
    with pytest.raises(ValueError):
        divide(1, 0)


def test_distance():
    assert distance(0, 0, 3, 4) == 5


def test_quadratic():
    assert quadratic(1, -3, 2) == (2, 1)
    assert quadratic(1, 2, 1) == (-1, -1)
    assert quadratic(1, 1, -4) == (2, -2)


def test_geometric_sum():
    assert geometric_sum(2, 3, 3) == 26
    assert geometric_sum(1, 2, 5) == 31
