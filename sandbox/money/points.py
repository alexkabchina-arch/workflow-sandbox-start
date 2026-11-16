"""Бонусные баллы за покупку."""

KOP_PER_POINT = 100_00  # 1 балл за каждые полные 100 ₽
ERROR = "сумма должна быть целым неотрицательным числом копеек"


def points(total_kop: int) -> int:
    """Баллы за чек: 1 за каждые полные 100 ₽ суммы в копейках."""
    # bool — подкласс int, но не сумма: отвергается, как в bags.py.
    if isinstance(total_kop, bool) or not isinstance(total_kop, int) or total_kop < 0:
        raise ValueError(ERROR)
    return total_kop // KOP_PER_POINT  # целое деление: без float, точно на любых суммах
