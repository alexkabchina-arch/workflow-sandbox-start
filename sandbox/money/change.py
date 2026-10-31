"""Сдача: сколько вернуть покупателю в копейках; оплачено меньше суммы — ошибка."""


def change_kop(paid_kop: int, due_kop: int) -> int:
    if paid_kop < due_kop:
        raise ValueError("оплачено меньше суммы")
    return paid_kop - due_kop
