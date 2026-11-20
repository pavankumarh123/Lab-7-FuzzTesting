
import pytest
from hypothesis import given, strategies as st

from processor import (
    parse_int_list,
    sanitize_string,
    safe_average
)


# TEST 1: parse_int_list

@given(st.lists(st.integers(), max_size=50))
def test_parse_int_list(numbers):
    data = ",".join(map(str, numbers))
    assert parse_int_list(data) == numbers


@given(st.text())
def test_parse_int_list_no_crash_for_valid_integer_strings(data):
    try:
        parse_int_list(data)
    except ValueError:
        pass


def test_parse_int_list_invalid_input():
    with pytest.raises(TypeError):
        parse_int_list(None)


# TEST 2: sanitize_string

@given(st.text())
def test_sanitize_string_no_crash(data):
    result = sanitize_string(data)

    assert isinstance(result, str)

    for char in result:
        assert char.isalnum() or char.isspace()


def test_sanitize_string_invalid_input():
    with pytest.raises(TypeError):
        sanitize_string(123)


# TEST 3: safe_average

@given(st.lists(st.integers(), min_size=1, max_size=100))
def test_safe_average(numbers):
    result = safe_average(numbers)

    assert result == sum(numbers) / len(numbers)


@given(st.lists(st.integers(), max_size=100))
def test_safe_average_no_crash(numbers):
    result = safe_average(numbers)

    if numbers:
        assert isinstance(result, (int, float))
    else:
        assert result == 0


def test_safe_average_invalid_input():
    with pytest.raises(TypeError):
        safe_average("hello")


def test_safe_average_invalid_list_elements():
    with pytest.raises(ValueError):
        safe_average([10, "hello", 20])


def test_safe_average_empty_list():
    assert safe_average([]) == 0
