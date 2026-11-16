import pytest

from sandbox.money.shortfall import shortfall_kop


def test_shortfall_is_due_minus_paid():
    assert shortfall_kop(700, 1000) == 300


@pytest.mark.parametrize("paid", [1000, 1200])
def test_paid_enough_is_zero_shortfall(paid):
    assert shortfall_kop(paid, 1000) == 0


def test_shortfall_by_one_kop():
    # Граница: на копейку меньше — недостача ровно в копейку
    assert shortfall_kop(999, 1000) == 1


@pytest.mark.parametrize(("paid", "due"), [(-1, 1000), (100, -1), (-5, -5)])
def test_negative_amount_is_error(paid, due):
    with pytest.raises(ValueError, match=r"^сумма не может быть отрицательной$"):
        shortfall_kop(paid, due)
