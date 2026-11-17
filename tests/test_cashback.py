import pytest

from sandbox.money.cashback import cashback_kop


def test_cashback_is_five_percent():
    assert cashback_kop(10_000) == 500


def test_negative_total_is_rejected():
    with pytest.raises(ValueError):
        cashback_kop(-1)


@pytest.mark.parametrize(
    "total_kop", [199.0, 19.99, float("nan"), float("inf"), True, False, "100"]
)
def test_total_must_be_integer_kopecks(total_kop):
    with pytest.raises(ValueError):
        cashback_kop(total_kop)


@pytest.mark.parametrize("total_kop, expected", [(1, 0), (19, 0), (20, 1), (39, 1)])
def test_cashback_rounds_down_to_whole_kopeck(total_kop, expected):
    assert cashback_kop(total_kop) == expected


def test_zero_total_has_no_cashback():
    assert cashback_kop(0) == 0


def test_large_total_keeps_integer_precision():
    assert cashback_kop(10**20 + 19) == 5_000_000_000_000_000_000
