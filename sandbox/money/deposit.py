"""Залог за стеклянную тару в копейках. Ставка и края — решение владельца #21:
1000 коп. за бутылку, ноль бутылок — 0, отрицательное число — ошибка."""

DEPOSIT_PER_BOTTLE_KOP = 1000


def deposit_kop(bottles: int) -> int:
    if bottles < 0:
        raise ValueError("число бутылок не может быть отрицательным")
    return bottles * DEPOSIT_PER_BOTTLE_KOP
