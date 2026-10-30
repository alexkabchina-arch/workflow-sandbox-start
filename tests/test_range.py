import pytest

from sandbox.money.range_ import range_kop


def test_range_of_several_amounts():
    assert range_kop(100, 500, 300) == 400


def test_range_of_single_amount_is_zero():
    assert range_kop(700) == 0


def test_range_of_no_amounts_is_error():
    with pytest.raises(ValueError, match="нужна хотя бы одна сумма"):
        range_kop()
