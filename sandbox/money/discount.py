"""Скидка кассира в процентах от суммы чека, в копейках: до копейки, половина — вверх (#22)."""

from sandbox.money.percent import percent_kop


def discount_kop(total_kop: int, percent: int) -> int:
    # Условие #22: процент вне 0–100 или отрицательная сумма — ошибка ввода
    if total_kop < 0 or not 0 <= percent <= 100:
        raise ValueError("неверные данные скидки")
    # Ответ владельца в #22: к ближайшему, половина вверх — так считает percent_kop.
    # Не путать со скидкой заказа order_total_kop (total.py): там дробь отбрасывается
    return percent_kop(total_kop, percent)
