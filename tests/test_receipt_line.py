import pytest

from sandbox.money.receipt_line import receipt_line


def test_detailed_line_from_owner_example():
    # Решение владельца #24: «<название> <qty> шт × <цена> ₽ = <сумма> ₽»
    assert receipt_line("Молоко", 2, 7990) == "Молоко 2 шт × 79,90 ₽ = 159,80 ₽"


def test_amounts_have_two_kopeck_digits_and_comma():
    assert receipt_line("Хлеб", 1, 1250) == "Хлеб 1 шт × 12,50 ₽ = 12,50 ₽"
    assert receipt_line("Спички", 3, 5) == "Спички 3 шт × 0,05 ₽ = 0,15 ₽"


def test_no_thousands_separator():
    assert receipt_line("Телевизор", 2, 12345600) == "Телевизор 2 шт × 123456,00 ₽ = 246912,00 ₽"


def test_zero_price_is_allowed():
    assert receipt_line("Пакет", 1, 0) == "Пакет 1 шт × 0,00 ₽ = 0,00 ₽"


def test_line_total_is_exact_on_large_values():
    # Целые копейки без float
    assert receipt_line("Партия", 10**9, 10**9 + 1) == (
        "Партия 1000000000 шт × 10000000,01 ₽ = 10000000010000000,00 ₽"
    )


@pytest.mark.parametrize(
    ("name", "qty", "price_kop"),
    [
        ("", 1, 100),
        ("   ", 1, 100),
        ("Молоко", 0, 100),
        ("Молоко", -1, 100),
        ("Молоко", 1, -1),
    ],
)
def test_bad_line_is_error(name, qty, price_kop):
    with pytest.raises(ValueError, match="^неверная строка чека$"):
        receipt_line(name, qty, price_kop)
