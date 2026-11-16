import pytest

from sandbox.money.bags import bags_kop


def test_bag_is_1000_kop():
    # Решение владельца #29: 10 ₽ за пакет
    assert bags_kop(1) == 1000
    assert bags_kop(3) == 3000


def test_bags_is_exact_int_on_large_count():
    # Целые копейки без float: результат int и точен на больших количествах
    result = bags_kop(10**17 + 1)
    assert type(result) is int
    assert result == 10**20 + 1000


def test_zero_bags_cost_nothing():
    assert bags_kop(0) == 0


@pytest.mark.parametrize("count", [1.5, 2.0, float("nan"), True, "2"])
def test_non_integer_bags_is_error(count):
    with pytest.raises(ValueError, match="^число пакетов должно быть целым$"):
        bags_kop(count)


@pytest.mark.parametrize("count", [-1, -5])
def test_negative_bags_is_error(count):
    with pytest.raises(ValueError, match="^число пакетов не может быть отрицательным$"):
        bags_kop(count)
