"""Дневник чтения: страницы, прочитанные за неделю."""


def main():
    pages = [18, 25, 0, 32, 14, 40, 21]
    for day, count in enumerate(pages, start=1):
        print(f"День {day}: {count} стр.")


if __name__ == "__main__":
    main()
