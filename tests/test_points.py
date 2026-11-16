import pytest

from sandbox.money.points import points


def test_point_per_full_100_rub():
    assert points(999_99) == 9
    assert points(1000_00) == 10


def test_zero_total_gives_no_points():
    assert points(0) == 0


@pytest.mark.parametrize("total", [-1, 1.5, True, "100"])
def test_bad_total_is_error(total):
    with pytest.raises(ValueError, match="^сумма должна быть целым неотрицательным числом копеек$"):
        points(total)
