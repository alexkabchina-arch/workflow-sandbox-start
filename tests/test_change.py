import pytest

from sandbox.money.change import change_kop


def test_change_is_paid_minus_due():
    assert change_kop(1000, 700) == 300


@pytest.mark.parametrize(("paid", "due"), [(1000, 1000), (700, 1000)])
def test_exact_or_underpayment_is_zero_change(paid, due):
    assert change_kop(paid, due) == 0


def test_underpayment_by_one_kop_is_zero_change():
    # Граница: на копейку меньше — сдачи нет, а не отрицательная сдача
    assert change_kop(999, 1000) == 0


def test_change_exact_on_large_sum():
    # Целые копейки без float: разница в копейку видна и на больших суммах
    assert change_kop(10**17 + 1, 10**17) == 1


@pytest.mark.parametrize(("paid", "due"), [(-1, 1000), (1000, -1), (-100, -500)])
def test_negative_amount_is_error(paid, due):
    with pytest.raises(ValueError, match=r"^сумма не может быть отрицательной$"):
        change_kop(paid, due)
