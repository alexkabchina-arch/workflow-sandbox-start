import pytest

from sandbox.money.over import count_over_kop


def test_counts_amounts_strictly_over_limit():
    # Сумма, равная порогу, не считается
    assert count_over_kop(300, 100, 500, 300, 900) == 2


def test_no_amounts_is_zero():
    assert count_over_kop(300) == 0


def test_negative_limit_is_error():
    with pytest.raises(ValueError, match="порог не может быть отрицательным"):
        count_over_kop(-1, 100)
