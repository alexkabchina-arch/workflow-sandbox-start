"""Сдача: сколько вернуть покупателю в копейках; оплачено меньше суммы — ошибка; отрицательные
входы (возврат) — ошибка, как у соседних функций зоны «деньги»."""


def change_kop(paid_kop: int, due_kop: int) -> int:
    if paid_kop < 0 or due_kop < 0:
        raise ValueError("сумма не может быть отрицательной")
    if paid_kop < due_kop:
        raise ValueError("оплачено меньше суммы")
    return paid_kop - due_kop
