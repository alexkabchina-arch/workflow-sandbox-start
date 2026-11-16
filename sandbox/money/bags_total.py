"""Стоимость пакетов в копейках по цене (тикет #37)."""


def bags_total_kop(bags: int, price_kop: int) -> int:
    """Количество, умноженное на цену. Оба — целые (не float и не bool): иначе `ValueError`;
    отрицательное количество или цена — тоже `ValueError`. Ошибка называет плохой аргумент."""
    checks = (
        (
            bags,
            "количество пакетов должно быть целым",
            "количество пакетов не может быть отрицательным",
        ),
        (price_kop, "цена должна быть целой", "цена не может быть отрицательной"),
    )
    for value, not_int, negative in checks:
        # float дал бы дробные копейки, bool — подкласс int (True — «один»)
        if isinstance(value, bool) or not isinstance(value, int):
            raise ValueError(not_int)
        if value < 0:
            raise ValueError(negative)
    return bags * price_kop
