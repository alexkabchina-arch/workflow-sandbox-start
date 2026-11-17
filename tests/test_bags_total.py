import pytest

from sandbox.money.bags_total import bags_total_kop


def test_bags_total_is_count_times_price():
    assert bags_total_kop(3, 500) == 1500


def test_zero_bags_cost_nothing():
    assert bags_total_kop(0, 500) == 0


@pytest.mark.parametrize(
    ("bags", "price_kop", "message"),
    [
        (-1, 500, "^количество пакетов не может быть отрицательным$"),
        (3, -500, "^цена не может быть отрицательной$"),
    ],
)
def test_negative_input_is_error(bags, price_kop, message):
    with pytest.raises(ValueError, match=message):
        bags_total_kop(bags, price_kop)


@pytest.mark.parametrize(
    ("bags", "price_kop", "message"),
    [
        (1.5, 500, "^количество пакетов должно быть целым$"),
        (True, 500, "^количество пакетов должно быть целым$"),
        (2, 99.5, "^цена должна быть целой$"),
        (2, True, "^цена должна быть целой$"),
    ],
)
def test_non_integer_input_is_error(bags, price_kop, message):
    with pytest.raises(ValueError, match=message):
        bags_total_kop(bags, price_kop)
