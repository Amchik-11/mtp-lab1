"""Дневник чтения: страницы, прочитанные за неделю."""

from reading_stats import summarize


def main():
    pages = [18, 25, 0, 32, 14, 40, 21]
    for day, count in enumerate(pages, start=1):
        print(f"День {day}: {count} стр.")

    stats = summarize(pages)
    print(f"\nВсего прочитано: {stats['total']} стр.")
    print(f"В среднем за день: {stats['average']:.1f} стр.")
    print(f"Дней с чтением: {stats['active_days']}")
    print(f"Лучший результат за день: {stats['best_day_pages']} стр.")


if __name__ == "__main__":
    main()
