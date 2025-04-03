from Lab11_gvanhorn_1 import rotation_correction
import pytest

def test_rotation_correction_below_360():
    expected = 100
    actual = rotation_correction(100)
    assert actual == expected

def test_rotation_above_360():
    expected = 100
    actual = rotation_correction(460)
    assert actual == expected

def test_negative_rotation():
    expected = 260
    actual = rotation_correction(-100)
    assert actual == expected

def test_non_numeric_entry():
    with pytest.raises(ValueError):
        rotation_correction('flip 360')
