import pytest

from sandbox.money import spread
from sandbox.money.range_ import range_kop


def test_range_is_spread_range_not_a_copy():
    # Одна реализация разброса (#155): правка в spread.py доходит и сюда
    assert range_kop is spread.range_kop


def test_range_of_several_amounts():
    assert range_kop(100, 500, 300) == 400


def test_range_is_signed_not_by_abs():
    # Возврат −500 и продажа 100: разброс 600, не 400 по модулю
    assert range_kop(-500, 100) == 600


def test_range_of_single_amount_is_zero():
    assert range_kop(700) == 0


def test_range_of_no_amounts_is_error():
    with pytest.raises(ValueError, match="нужна хотя бы одна сумма"):
        range_kop()
