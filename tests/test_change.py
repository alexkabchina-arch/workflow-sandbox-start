import pytest

from sandbox.money.change import change_kop


def test_change_is_paid_minus_due():
    assert change_kop(1000, 730) == 270


def test_exact_payment_is_zero_change():
    assert change_kop(500, 500) == 0


def test_underpayment_is_error():
    with pytest.raises(ValueError, match=r"^оплачено меньше суммы$"):
        change_kop(400, 500)
