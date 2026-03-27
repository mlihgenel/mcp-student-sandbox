from __future__ import annotations

from pathlib import Path
from typing import Iterable, List

TAX_RATE = 0.15
LOG_FILE = Path("log.txt")


def calculate_totals(values: Iterable[float], rate: float = TAX_RATE) -> List[float]:
    """Hesaplanan toplamları döndürür."""
    if values is None:
        raise ValueError("values parametresi None olamaz")

    return [round(value * (1 + rate), 2) for value in values]


def format_total(value: float) -> str:
    """Kullanıcı için göstermek üzere formatlanmış metin üretir."""
    return f"Total: {value:.2f}"


def append_log(results: Iterable[float], log_path: Path = LOG_FILE) -> None:
    """Sonuçları log dosyasına ekler."""
    with log_path.open("a", encoding="utf-8") as f:
        f.write(f"{list(results)}\n")


def process_data(data: Iterable[float], *, log_file: Path = LOG_FILE) -> List[float]:
    """Verilen sayısal verilere vergi ekleyip sonuçları döndürür ve loglar."""
    totals = calculate_totals(data)

    for total in totals:
        print(format_total(total))

    append_log(totals, log_file)
    return totals


if __name__ == "__main__":
    example = [100.0, 200.5, 300]
    print("Process data result:", process_data(example))
