# Фінансовий трекер студента
# Програма дозволяє студенту вести облік витрат, бюджету та бачити звіти.

import datetime

# Змінні для збереження бюджету та витрат
budget = 0.0
expenses = []

def welcome():
    """Вітання користувача при запуску програми."""
    print("👋 Привіт! Я бот 'Фінансовий трекер студента'.")
    print("Введи команду 'допомога', щоб побачити доступні команди.")

def show_help():
    """Виводить список доступних команд."""
    print("\n📌 Доступні команди:")
    print("  допомога              - список команд")
    print("  встановити бюджет     - встановити місячний бюджет")
    print("  додати витрату        - додати нову витрату")
    print("  показати витрати      - переглянути всі витрати")
    print("  залишок               - показати залишок бюджету")
    print("  звіт за категоріями   - показати витрати по категоріях")
    print("  вийти                 - завершити роботу\n")

def set_budget():
    """Встановлення загального бюджету."""
    global budget
    try:
        budget = float(input("Введи суму бюджету (грн): "))
        print(f"✅ Бюджет встановлено: {budget:.2f} грн")
    except ValueError:
        print("❌ Помилка: введено нечислове значення.")

def add_expense():
    """Додає нову витрату до списку витрат."""
    try:
        amount = float(input("Сума витрати (грн): "))
        category = input("Категорія витрати (їжа, транспорт тощо): ")
        date_str = input("Дата (РРРР-ММ-ДД), або Enter для сьогоднішньої: ")
        if date_str.strip() == "":
            date = datetime.date.today()
        else:
            date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        expenses.append({"amount": amount, "category": category, "date": date})
        print("✅ Витрату додано.")
    except ValueError:
        print("❌ Помилка формату. Спробуй ще раз.")

def show_expenses():
    """Виводить список усіх витрат."""
    if not expenses:
        print("📭 Витрат поки що немає.")
    else:
        print("\n📒 Список витрат:")
        for i, e in enumerate(expenses, 1):
            print(f"{i}. {e['date']} | {e['category']} | {e['amount']:.2f} грн")

def show_balance():
    """Обчислює і показує залишок бюджету."""
    total_spent = sum(e["amount"] for e in expenses)
    remaining = budget - total_spent
    print(f"\n💰 Всього витрачено: {total_spent:.2f} грн")
    print(f"📉 Залишок бюджету: {remaining:.2f} грн")

def category_report():
    """Формує звіт витрат по категоріях."""
    if not expenses:
        print("📭 Витрат поки що немає.")
        return
    report = {}
    for e in expenses:
        report[e["category"]] = report.get(e["category"], 0) + e["amount"]
    print("\n📊 Витрати за категоріями:")
    for category, total in report.items():
        print(f"{category}: {total:.2f} грн")

def main():
    """Головний цикл програми."""
    welcome()
    while True:
        command = input("\nВведи команду: ").strip().lower()
        if command == "допомога":
            show_help()
        elif command == "встановити бюджет":
            set_budget()
        elif command == "додати витрату":
            add_expense()
        elif command == "показати витрати":
            show_expenses()
        elif command == "залишок":
            show_balance()
        elif command == "звіт за категоріями":
            category_report()
        elif command == "вийти":
            print("👋 До побачення!")
            break
        else:
            print("❌ Невідома команда. Введи 'допомога'.")

# Запуск програми
if name == "__main__":
    main()