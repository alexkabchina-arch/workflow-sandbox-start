"""Строка чека для товара. Формат и края — решение владельца #24:
«<название> <qty> шт × <цена> ₽ = <сумма> ₽», суммы — рубли с копейками через запятую,
без разделителя тысяч; пустое название, количество ≤ 0 и отрицательная цена — ошибка."""

import unicodedata


def _rub(kop: int) -> str:
    rub, rest = divmod(kop, 100)
    return f"{rub},{rest:02d} ₽"


def _bad_char(ch: str) -> bool:
    # Управляющие и невидимые (Cc, Cf, …) и разрывы строк (Zl, Zp): иначе перевод строки
    # в названии подделал бы в чеке отдельную строку, а U+200B прошёл бы как непустое название
    return unicodedata.category(ch)[0] == "C" or unicodedata.category(ch) in ("Zl", "Zp")


def receipt_line(name: str, qty: int, price_kop: int) -> str:
    name = name.strip()
    if not name or any(_bad_char(ch) for ch in name) or qty <= 0 or price_kop < 0:
        raise ValueError("неверная строка чека")
    return f"{name} {qty} шт × {_rub(price_kop)} = {_rub(qty * price_kop)}"
