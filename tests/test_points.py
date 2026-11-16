import pytest

from sandbox.money.points import points


def test_point_per_full_100_rub():
    assert points(999_99) == 9
    assert points(1000_00) == 10


def test_points_are_exact_on_huge_total():
    # Критерий 1 #33 по правилу «балл за 100 ₽»: 10**30 баллов — это 10**30 * 100_00 копеек.
    assert points(10**30 * 100_00) == 10**30
    assert points(10**30 * 100_00 - 1) == 10**30 - 1


def test_zero_total_gives_no_points():
    assert points(0) == 0


@pytest.mark.parametrize("total", [-1, 1.5, True, "100"])
def test_bad_total_is_error(total):
    with pytest.raises(ValueError, match="^сумма должна быть целым неотрицательным числом копеек$"):
        points(total)
