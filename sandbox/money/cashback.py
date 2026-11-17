"""Кэшбэк с суммы чека в копейках."""


def cashback_kop(total_kop: int) -> int:
    """Вернуть 5 % суммы чека, округлив вниз до целой копейки."""
    if total_kop < 0:
        raise ValueError("сумма чека не должна быть отрицательной")
    return total_kop * 5 // 100
