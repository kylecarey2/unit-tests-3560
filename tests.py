import pytest
import main as m


def test_fibonacci():
    assert m.fibonacci(0) == 0
    assert m.fibonacci(5) == 5
    assert m.fibonacci(7) == 13

    with pytest.raises(ValueError):
        m.fibonacci(-2)


def test_is_palindrome():
    assert m.is_palindrome("racecar") is True
    assert m.is_palindrome("rac .ecar") is True
    assert m.is_palindrome("kyle") is False


def test_word_count():
    assert m.word_count("Hello world hello kyle") == {"hello": 2, "world": 1, "kyle": 1}
    assert m.word_count("") == {}
    assert m.word_count("kyle kyle kyle kyl") == {"kyle": 3, "kyl": 1}


def test_average():
    assert m.average([12.5, 34.82, 2]) == pytest.approx(16.44)
    assert m.average([0, 0, 0]) == 0

    with pytest.raises(ValueError):
        m.average([])


def test_find_max():
    assert m.find_max([1, 2, 3, 4, 5, 10]) == 10
    assert m.find_max([-1, -2, -3, -4]) == -1

    with pytest.raises(ValueError):
        m.find_max([])


def test_unique():
    assert m.unique([1, 4, 4, 6, 5]) == [1, 4, 6, 5]
    assert m.unique(["hello", "world", "how", "is", "the", "world"]) == ["hello", "world", "how", "is", "the"]
    assert m.unique([]) == []


def test_convert_temp():
    assert m.convert_temp(0, "F") == 32
    assert m.convert_temp(89.6, "C") == pytest.approx(32)

    with pytest.raises(ValueError):
        m.convert_temp(50, "INVALID")


def test_sort_dict_by_value():
    assert m.sort_dict_by_value({"Hello": 2, "Hello2": -1, "cat": 0}) == [
        ("Hello2", -1),
        ("cat", 0),
        ("Hello", 2),
    ]
    assert m.sort_dict_by_value({}) == []


def test_merge_dicts():
    assert m.merge_dicts({}, {}) == {}
    assert m.merge_dicts({"one": 1}, {"two": 2}) == {"one": 1, "two": 2}
    assert m.merge_dicts({"one": 1}, {"two": 2, "three": 3}) == {"one": 1, "two": 2, "three": 3}
    assert m.merge_dicts({}, {"two": 2, "three": 3}) == {"two": 2, "three": 3}
    assert m.merge_dicts({"one": 1}, {}) == {"one": 1}


def test_safe_divide():
    assert m.safe_divide(10, 1) == 10
    assert m.safe_divide(5, 2) == 2.5

    with pytest.raises(ZeroDivisionError):
        m.safe_divide(3, 0)
