"""Разброс сумм: разница между наибольшей и наименьшей суммой в копейках; без сумм — ошибка."""

from sandbox.money.maximum import max_kop
from sandbox.money.minimum import min_kop


def range_kop(*amounts_kop: int) -> int:
    # Условие #5: без сумм — то же сообщение, что у max_kop и min_kop; одна сумма — 0
    return max_kop(*amounts_kop) - min_kop(*amounts_kop)
