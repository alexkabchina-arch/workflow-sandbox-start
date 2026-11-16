"""Стоимость пакетов на кассе в копейках. Цена и края — решение владельца #29:
1000 коп. за пакет, ноль пакетов — 0, отрицательное число — ошибка."""

BAG_PRICE_KOP = 1000


def bags_kop(count: int) -> int:
    # Только целое число пакетов: float дал бы дробные копейки, NaN прошёл бы `< 0`,
    # а bool — подкласс int, True молча считался бы одним пакетом
    if isinstance(count, bool) or not isinstance(count, int):
        raise ValueError("число пакетов должно быть целым")
    if count < 0:
        raise ValueError("число пакетов не может быть отрицательным")
    return count * BAG_PRICE_KOP
