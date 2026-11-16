"""Стоимость пакетов в копейках по цене: количество, умноженное на цену (тикет #37);
отрицательное количество или цена — ошибка."""


def bags_total_kop(bags: int, price_kop: int) -> int:
    # Только целые: float дал бы дробные копейки, bool — подкласс int (True — «один»)
    for value in (bags, price_kop):
        if isinstance(value, bool) or not isinstance(value, int):
            raise ValueError("количество и цена должны быть целыми")
    if bags < 0 or price_kop < 0:
        raise ValueError("количество и цена не могут быть отрицательными")
    return bags * price_kop
