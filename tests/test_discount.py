import pytest

from sandbox.money.discount import discount_kop


def test_discount_of_round_sum():
    # 10 % от 10,00 ₽
    assert discount_kop(1000, 10) == 100


def test_discount_fraction_rounds_half_up():
    # Ответ владельца в #22: 149,85 коп. → 150
    assert discount_kop(999, 15) == 150


def test_discount_exact_half_rounds_up():
    # 5 % от 0,10 ₽ = 0,5 коп. → 1
    assert discount_kop(10, 5) == 1


def test_discount_below_half_rounds_down():
    # 1 % от 1,49 ₽ = 1,49 коп. → 1
    assert discount_kop(149, 1) == 1


def test_discount_bounds_are_valid():
    assert discount_kop(1000, 0) == 0
    assert discount_kop(1000, 100) == 1000
    assert discount_kop(0, 50) == 0


@pytest.mark.parametrize(
    ("total_kop", "percent"),
    [(1000, 101), (1000, -1), (-1, 10)],
)
def test_discount_invalid_input(total_kop, percent):
    with pytest.raises(ValueError, match="^неверные данные скидки$"):
        discount_kop(total_kop, percent)
