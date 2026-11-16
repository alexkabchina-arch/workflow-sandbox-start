import pytest

from sandbox.money.bags_total import bags_total_kop


def test_bags_total_is_count_times_price():
    assert bags_total_kop(3, 500) == 1500


def test_zero_bags_cost_nothing():
    assert bags_total_kop(0, 500) == 0


@pytest.mark.parametrize(("bags", "price_kop"), [(-1, 500), (3, -500)])
def test_negative_input_is_error(bags, price_kop):
    with pytest.raises(ValueError, match="^количество и цена не могут быть отрицательными$"):
        bags_total_kop(bags, price_kop)


@pytest.mark.parametrize(("bags", "price_kop"), [(1.5, 500), (True, 500), (2, 99.5)])
def test_non_integer_input_is_error(bags, price_kop):
    with pytest.raises(ValueError, match="^количество и цена должны быть целыми$"):
        bags_total_kop(bags, price_kop)
