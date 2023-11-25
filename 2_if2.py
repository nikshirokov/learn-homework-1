"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками.
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры
  и выводя на экран результаты

"""
def comparator(first_line, second_line):
    if isinstance(first_line, str) and isinstance(second_line, str):
        if first_line == second_line:
            return 1
        elif len(first_line) > len(second_line):
            return 2
        elif second_line == 'learn':
            return 3
    else:return 0

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    print(comparator('Hello', 'py'))
    print(comparator('Hello', 'Hello'))
    print(comparator('Py', 'learn'))
    print(comparator(1, 'one'))


if __name__ == "__main__":
    main()
