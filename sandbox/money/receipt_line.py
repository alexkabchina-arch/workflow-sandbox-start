"""Строка чека для товара. Формат и края — решение владельца #24:
«<название> <qty> шт × <цена> ₽ = <сумма> ₽», суммы — рубли с копейками через запятую,
без разделителя тысяч; пустое название, количество ≤ 0 и отрицательная цена — ошибка."""


def _rub(kop: int) -> str:
    rub, rest = divmod(kop, 100)
    return f"{rub},{rest:02d} ₽"


def receipt_line(name: str, qty: int, price_kop: int) -> str:
    if not name.strip() or qty <= 0 or price_kop < 0:
        raise ValueError("неверная строка чека")
    return f"{name} {qty} шт × {_rub(price_kop)} = {_rub(qty * price_kop)}"
