"""Недостача: сколько не хватает до суммы чека в копейках; оплачено столько же или больше — 0;
отрицательные входы — ошибка по условию тикета #14 (возврат здесь не считается)."""


def shortfall_kop(paid_kop: int, due_kop: int) -> int:
    if paid_kop < 0 or due_kop < 0:
        raise ValueError("сумма не может быть отрицательной")
    return max(due_kop - paid_kop, 0)
