import pytest
import numpy as np

from convertlib import miles_to_km


def test_basic_conversion():
    assert miles_to_km(1) == 1.60934
    assert miles_to_km(2) == 2 * 1.60934
    assert miles_to_km(0) == 0


def test_float_conversion():
    assert miles_to_km(1.5) == 1.5 * 1.60934


def test_array_conversion():
    miles_array = np.array([1, 2, 3])
    km_array = miles_array * 1.60934
    np.testing.assert_array_equal(miles_to_km(miles_array), km_array, strict=True)


def test_negative_miles():
    assert miles_to_km(-1) == -1 * 1.60934


def test_unusual_inputs():
    with pytest.raises(TypeError):
        miles_to_km("string")
