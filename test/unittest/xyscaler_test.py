""" Unit tests for XYScaler class. """
import pytest
from drawing_tools import XYScaler

def test_p1a_maps_to_p1b():
    """ Test that p1a is transformed to p1b. """
    p1a = (1,2)
    p1b = (30,40)
    p2a = (5,6)
    p2b = (70,80)

    scaler = XYScaler(p1a,p1b,p2a,p2b)
    assert p1b == scaler(p1a)

def test_p2a_maps_to_p2b():
    """ Test that p2a is transformed to p2b. """
    p1a = (1,2)
    p1b = (30,40)
    p2a = (5,6)
    p2b = (70,80)
    scaler = XYScaler(p1a,p1b,p2a,p2b)
    assert p2b == scaler(p2a)

def test_axis_width_opposite_direction():
    """ Test that p2a is transformed to p2b when the axis have opposite direction. """
    p1a = (0,0)
    p1b = (100,100)
    p2a = (10,10)
    p2b = (0,0)
    scaler = XYScaler(p1a,p1b,p2a,p2b)
    assert p2b == scaler(p2a)

def test_midpoints():
    """ Test the midpoint is transformed to the midpoint in the b system."""
    p1a = (0,0)
    p1b = (100,100)
    p2a = (10,10)
    p2b = (0,0)
    scaler = XYScaler(p1a,p1b,p2a,p2b)
    assert (50.0, 50.0) == scaler((5.0,5.0))

def test_raise_identicalcoordinate_a0():
    """ if coordinates causes the scale factor to be 0 or infinite raise exceptions """
    p1a = (0,0)
    p1b = (100,100)
    p2a = (0,10)
    p2b = (0,0)

    with pytest.raises(ValueError):
        XYScaler(p1a,p1b,p2a,p2b)

def test_raise_identicalcoordinate_a1():
    """ if coordinates causes the scale factor to be 0 or infinite raise exceptions """
    p1a = (0,0)
    p1b = (100,100)
    p2a = (10,0)
    p2b = (0,0)

    with pytest.raises(ValueError):
        XYScaler(p1a,p1b,p2a,p2b)

def test_raise_identicalcoordinate_b0():
    """ if coordinates causes the scale factor to be 0 or infinite raise exceptions """
    p1a = (0,0)
    p1b = (100,100)
    p2a = (10,10)
    p2b = (100,0)

    with pytest.raises(ValueError):
        XYScaler(p1a,p1b,p2a,p2b)

def test_raise_identicalcoordinate_b1():
    """ if coordinates causes the scale factor to be 0 or infinite raise exceptions """
    p1a = (0,0)
    p1b = (100,100)
    p2a = (10,0)
    p2b = (0,100)

    with pytest.raises(ValueError):
        XYScaler(p1a,p1b,p2a,p2b)

def test_AspectLocked():
    """Test the scaling factor from the first oordinate is also use on the 2nd coordinate
    when aspect_locked is true."""
    p1a = (0,0)
    p1b = (0,0)
    p2a = (10,10)
    p2b = (10,100)

    scaler= XYScaler(p1a,p1b,p2a,p2b,True)
    assert (10,10)  == scaler(p2a)

