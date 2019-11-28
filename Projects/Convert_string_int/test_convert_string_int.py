import pytest
from convert_string_int import convert_to_int

def test_string_with_missing_comma():
    actual = convert_to_int("178100,301")
    assert actual is None, f"Expected: None, Actual: {actual}"

def test_on_string_with_incorrectly_placed_comma():
    actual = convert_to_int("12,72,891")
    assert actual is None, f"Expected: None, Actual: {actual}"

def test_on_float_valued_string():
    actual = convert_to_int("23,816.92")
    assert actual is None, f"Expected: None, Actual: {actual}"

def test_type():
    with pytest.raises(AssertionError):
        convert_to_int(123)
        convert_to_int(123.23)
        convert_to_int(-123)
        convert_to_int(True)

