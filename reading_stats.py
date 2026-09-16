"""Расчёт статистики дневника чтения."""


def summarize(pages):
    """Вернуть итог по дням, включая дни без чтения в среднем значении."""
    if any(type(value) is not int or value < 0 for value in pages):
        raise ValueError("Количество страниц должно быть целым неотрицательным числом")
    total = sum(pages)
    return {
        "total": total,
        "average": total / len(pages) if pages else 0.0,
        "active_days": sum(value > 0 for value in pages),
        "best_day_pages": max(pages, default=0),
    }
