"""Суммы выше порога: сколько сумм в копейках строго больше порога; без сумм — 0."""


def count_over_kop(limit_kop: int, *amounts_kop: int) -> int:
    if limit_kop < 0:
        raise ValueError("порог не может быть отрицательным")
    # Условие #8: строго больше — сумма, равная порогу, не считается
    return sum(1 for a in amounts_kop if a > limit_kop)
