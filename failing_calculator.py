from __future__ import annotations

from typing import Iterable


def average_ratios(numbers: Iterable[float]) -> float:
    """Hesaplanan oranların ortalamasını döner.

    Sıfır değerlerini geçersiz kabul eder ve ZeroDivisionError üretmez.
    """
    numbers_list = list(numbers)
    if not numbers_list:
        raise ValueError("numbers listesi boş olamaz")

    total = 0.0
    count = 0

    for value in numbers_list:
        if value == 0:
            continue
        total += 100.0 / value
        count += 1

    if count == 0:
        raise ValueError("numbers listesinde sıfır dışı bir değer bulunamadı")

    return total / count


if __name__ == "__main__":
    example = [10, 5, 0]
    print(average_ratios(example))
