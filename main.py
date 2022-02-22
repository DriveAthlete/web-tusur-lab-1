import math


def base_y(x: float) -> float:
    return math.pow(x, 3) + 3 * x + 4


def get_input() -> float:
    while True:
        print("Введите значение X:")
        try:
            return float(input())
        except ValueError as exc:
            print(f"Введеная строка не является числом. Попробуйте заново.\nПодробнее: {exc}")


def func(x: float) -> float:
    if x >= 0 and x <= 1:
        return base_y(x)
    elif x < 0:
        return math.pow(base_y(x), 2)
    else:
        return -4.0


def print_output(y: float):
    print(f"Результат функции = {y}")


def main():
    input_x = get_input()
    output_y = func(input_x)
    print_output(output_y)


if __name__ == "__main__":
    print(__name__)
    main()
