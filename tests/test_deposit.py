import pytest

from sandbox.money.deposit import deposit_kop


def test_deposit_is_1000_kop_per_bottle():
    # Решение владельца #21: 10 ₽ за бутылку
    assert deposit_kop(1) == 1000
    assert deposit_kop(3) == 3000


def test_deposit_is_exact_int_on_large_count():
    # Целые копейки без float: результат int и точен на больших количествах
    result = deposit_kop(10**17 + 1)
    assert type(result) is int
    assert result == 10**20 + 1000


def test_zero_bottles_zero_deposit():
    assert deposit_kop(0) == 0


@pytest.mark.parametrize("bottles", [-1, -5])
def test_negative_bottles_is_error(bottles):
    with pytest.raises(ValueError, match="^число бутылок не может быть отрицательным$"):
        deposit_kop(bottles)
