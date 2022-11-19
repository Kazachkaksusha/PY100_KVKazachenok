"""
Функция рисует в консоль состояние поля
Пусть: 0 - пустое поле " "
       1 - крестик "X"
       2 - нолик "O"

Пример пустого поля:

[0, 0, 0, 0, 0, 0, 0, 0, 0]

В консоли:

 | |
 | |
 | |

Пример поля:

[2, 0, 2, 0, 1, 0, 0, 0, 1]

В консоли:

 O| |O
  |X|
  | |X


:param [list]:
:return:
"""

DICT_CHAR = {0: " ",
             1: "X",
             2: "O"}


def draw_field(field: list):
    for index, char in enumerate(field):
        if char in DICT_CHAR:
            field[index] = DICT_CHAR[char]
    print("|".join(map(str, field[0:3])))
    print("|".join(map(str, field[3:6])))
    print("|".join(map(str, field[6:9])))


field = [0, 1, 0, 2, 0, 0, 0, 1, 0]
print(draw_field(field))


"""
Функция определяет кто выйграл в игре

Пусть (a, b) - a: 0 - игра ещё идет
                  1 - игра закончена
               b: 0 - никто не победил или ничья
                  1 - выиграл первый
                  2 - выиграл второй

Пример пустого поля:
   
[0, 0, 0, 0, 0, 0, 0, 0, 0]

(0, 0)

Пример поля:

[2, 1, 2, 1, 1, 2, 2, 1, 1]

(1, 1)

:param field:
:return: возвращает кортеж значений (a, b): a - означает закончена ли игра.
                                            b - означает кто выйграл.
"""

fields_win_1 = [[], [], [], ... ]   # Список списков с выигрышными комбинациями для 1 игрока
fields_win_2 = [[], [], [], ... ]   # Список списков с выигрышными комбинациями для 2 игрока


def who_win(field: list) -> (int, int):
    for char in field:
        if char == 0:
            return 0, 0
        else:
            for field in fields_win_1:
                return 1, 1
            for field in fields_win_2:
                return 1, 2
            else:
                return 1, 0


print(who_win(field))
