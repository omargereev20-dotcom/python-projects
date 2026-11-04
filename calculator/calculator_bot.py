# My first Python project
def load_history():
    try:
        with open("history.txt", "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        return ""


def save_history(calculation):
    with open("history.txt", "a+", encoding="utf-8") as file:
        file.seek(0, 2)

        if file.tell() > 0:
            file.seek(0)
            last_character = file.read()[-1]

            if last_character != "\n":
                file.write("\n")

        file.write(f"{calculation}\n")


def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Ошибка: необходимо вводить числа!")


def get_operation():
    while True:
        operation = input("Введите операцию (+, -, *, /): ")

        if operation in ["+", "-", "*", "/"]:
            return operation
        else:
            print("Ошибка: неизвестная операция!")


def save_calculation(a, operation, b):
    try:
        if operation == "+":
            result = a + b
        elif operation == "-":
            result = a - b
        elif operation == "*":
            result = a * b
        elif operation == "/":
            result = a / b

    except ZeroDivisionError:
        print("На ноль делить нельзя!")
        return None

    calculation_text = f"{a} {operation} {b} = {result}"
    save_history(calculation_text)

    return result


def calculator():
    a = get_number("Введите первое число: ")
    operation = get_operation()
    b = get_number("Введите второе число: ")

    return save_calculation(a, operation, b)


def show_history():
    saved_history = load_history()

    if not saved_history:
        print("История вычислений пуста.")
        return

    print("\n--- ИСТОРИЯ ВЫЧИСЛЕНИЙ ---")

    for number, calculation in enumerate(saved_history.splitlines(), start=1):
        print(f"{number}. {calculation}")


def clear_history():
    saved_history = load_history()

    if not saved_history:
        print("История вычислений уже пуста.")
        return

    with open("history.txt", "w", encoding="utf-8") as file:
        pass

    print("История очищена!")


while True:
    print("\n--- КАЛЬКУЛЯТОР ---")
    print("1. Выполнить вычисление")
    print("2. История вычислений")
    print("3. Выход")
    print("4. Очистить историю")

    choice = input("Выбери действие: ").strip()

    if choice == "1":
        result = calculator()

        if result is not None:
            print(f"Результат: {result}")

    elif choice == "2":
        show_history()

    elif choice == "3":
        print("До свидания!")
        break

    elif choice == "4":
        clear_history()

    else:
        print("Неизвестная команда!")




