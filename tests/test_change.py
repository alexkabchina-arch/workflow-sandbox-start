import pytest

from sandbox.money.change import change_kop


def test_change_is_paid_minus_due():
    assert change_kop(1000, 730) == 270


def test_exact_payment_is_zero_change():
    assert change_kop(500, 500) == 0


def test_underpayment_is_error():
    with pytest.raises(ValueError, match=r"^оплачено меньше суммы$"):
        change_kop(400, 500)


def test_underpayment_by_one_kop_is_error():
    # Граница: на копейку меньше — уже ошибка, а не отрицательная сдача
    with pytest.raises(ValueError, match=r"^оплачено меньше суммы$"):
        change_kop(499, 500)


def test_change_exact_on_large_sum():
    # Целые копейки без float: разница в копейку видна и на больших суммах
    assert change_kop(10**17 + 1, 10**17) == 1


@pytest.mark.parametrize(("paid", "due"), [(-100, -500), (-1000, -730), (100, -1)])
def test_negative_amount_is_error(paid, due):
    with pytest.raises(ValueError, match=r"^сумма не может быть отрицательной$"):
        change_kop(paid, due)
