"""Консольный дневник чтения с данными, заданными пользователем."""

import argparse

from reading_stats import summarize


def main():
    parser = argparse.ArgumentParser(description="Подсчитать статистику чтения по дням")
    parser.add_argument(
        "--pages", type=int, nargs="+", default=[18, 25, 0, 32, 14, 40, 21],
        metavar="N", help="прочитанные страницы за каждый день; например: 10 0 25",
    )
    args = parser.parse_args()
    try:
        stats = summarize(args.pages)
    except ValueError as error:
        parser.error(str(error))

    print("ДНЕВНИК ЧТЕНИЯ")
    for day, count in enumerate(args.pages, start=1):
        print(f"  День {day:2}: {count:4} стр.")
    print(f"\nВсего прочитано: {stats['total']} стр.")
    print(f"В среднем за день: {stats['average']:.1f} стр.")
    print(f"Дней с чтением: {stats['active_days']} из {len(args.pages)}")
    print(f"Лучший результат за день: {stats['best_day_pages']} стр.")


if __name__ == "__main__":
    main()
