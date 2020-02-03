import pytest

from .stringcalculator import StringCalculator


def test_empty_string_returns_zero():
    c = StringCalculator()
    assert c.add("") == 0

def test_single_number_returns_number():
    c = StringCalculator()
    assert c.add("0") == 0
    assert c.add("1") == 1
    assert c.add("2") == 2
    assert c.add("1235") == 1235
    assert c.add("99999999") == 99999999

def test_two_numbers_return_sum():
    c = StringCalculator()
    assert c.add("0,0") == 0
    assert c.add("1,2") == 3
    assert c.add("20,1") == 21
    assert c.add("100,1000") == 1100

def test_numbers_delimited_by_newline():
    c = StringCalculator()
    assert c.add("0\n0") == 0
    assert c.add("1,2\n3") == 6
    assert c.add("1\n1\n1") == 3

def test_custom_delimiter():
    c = StringCalculator()
    assert c.add("//,\n1,2,3") == 6
    assert c.add("//;\n1;2;3") == 6
    assert c.add("//;;\n1;;2;;3") == 6
    assert c.add("//asd\n1asd2asd3") == 6

def test_custom_delimiter_with_newlines():
    c = StringCalculator()
    assert c.add("//;\n1;2\n3;4") == 10

def test_negative_numbers_throw():
    c = StringCalculator()
    with pytest.raises(ValueError):
        c.add("-1")
    with pytest.raises(ValueError):
        c.add("3,2,-1")
    with pytest.raises(ValueError):
        c.add("//;\n1;-2")

def test_negative_numbers_are_listed():
    c = StringCalculator()
    with pytest.raises(ValueError) as excinfo:
        c.add("-1,-2,-3")
    assert "-1" in str(excinfo.value)
    assert "-2" in str(excinfo.value)
    assert "-3" in str(excinfo.value)

def test_call_count_starts_at_zero():
    c = StringCalculator()
    assert c.call_count == 0

def test_call_count_increases():
    c = StringCalculator()
    c.add("")
    c.add("1")
    assert c.call_count == 2
