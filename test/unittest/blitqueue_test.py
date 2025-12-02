"""Unit tests for BlitQueue class."""
from drawing_tools import BlitQueue


def test_sorting(): #pylint: disable=missing-function-docstring
    q = BlitQueue()
    q.add(None, (1, 1), 1)
    q.add(None, (3, 3), 3)
    q.add(None, (2, 2), 2)

    sorted_q = q.get()
    assert sorted_q[0][1] == (1, 1)
    assert sorted_q[1][1] == (2, 2)
    assert sorted_q[2][1] == (3, 3)

def test_stable_sorting():  # pylint: disable=missing-function-docstring
    q = BlitQueue()
    q.add(None, (3, 3), 3)
    q.add(None, (1, 1), 1)
    q.add(None, (4, 4), 3)
    q.add(None, (2, 2), 2)
    q.add(None, (5, 5), 3)

    sorted_q = q.get()
    assert sorted_q[2][1] == (3, 3)
    assert sorted_q[3][1] == (4, 4)
    assert sorted_q[4][1] == (5, 5)
