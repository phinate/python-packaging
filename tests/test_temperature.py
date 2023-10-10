import pytest
import numpy as np

from convertlib import celsius_to_fahrenheit  


def test_basic_conversion():
    assert celsius_to_fahrenheit(0) == 32
    assert celsius_to_fahrenheit(100) == 212

def test_float_conversion():
    assert celsius_to_fahrenheit(37.5) == 37.5 * 9 / 5 + 32

def test_array_conversion():
    celsius_array = np.array([0, 100, -40])
    fahrenheit_array = celsius_array * 9 / 5 + 32
    np.testing.assert_array_equal(celsius_to_fahrenheit(celsius_array), fahrenheit_array)

def test_negative_temperatures():
    assert celsius_to_fahrenheit(-40) == -40
    assert celsius_to_fahrenheit(-10) == -10 * 9 / 5 + 32

def test_unusual_inputs():
    with pytest.raises(TypeError):
        celsius_to_fahrenheit("string")
