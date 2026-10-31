import pytest

from sandbox.money.over import count_over_kop


def test_counts_amounts_strictly_over_limit():
    # Сумма, равная порогу, не считается
    assert count_over_kop(300, 100, 500, 300, 900) == 2


def test_no_amounts_is_zero():
    assert count_over_kop(300) == 0


def test_refund_is_compared_signed_not_by_abs():
    # Возврат −500 не дороже порога 300: сравнение со знаком, не по модулю
    assert count_over_kop(300, -500) == 0


def test_over_exact_on_large_sum():
    # Целые копейки без float: соседние суммы различаются и на больших значениях
    assert count_over_kop(10**17, 10**17 + 1, 10**17) == 1


def test_zero_limit_is_allowed():
    # Ошибка — только у отрицательного порога, ноль допустим
    assert count_over_kop(0, 0, 1) == 1


def test_negative_limit_is_error():
    with pytest.raises(ValueError, match=r"^порог не может быть отрицательным$"):
        count_over_kop(-1, 100)
