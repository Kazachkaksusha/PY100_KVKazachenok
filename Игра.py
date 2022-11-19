from typing import List, Union, Tuple


def init_field(size: int, empty_ceil: Union[str, None]) -> List[List]:
    """
    Возвращает пустое поле
    :param size: параметр размера поля
    :param empty_ceil: параметр заполнения пустой ячейки
    :return: поле в виде списка списков
    """
    field = []
    for row in range(size):
        field.append([empty_ceil]*size)

    return field


def draw_field(field: List[List]) -> None:
    """
    Отрисовывает состояние поля после каждого хода
    :param field: поле в виде списка списков
    :return: -
    """
    for row in field:
        for ceil in row:
            print(f"|{ceil}", end="")
        print("|")


def get_int_val(text, border=None) -> int:
    """
    Возвращает целое число с проверками
    :param text: игрок вводит значение индекса ячейки для хода
    :param border: граница значений индексов ячейки в поле
    :return: индекс ячейки в поле - целое число в заданной границе
    """
    while True:
        val = input(text)
        try:
            val = int(val)
        except ValueError:
            print("Должно быть целое число")
            continue
        if border is not None:
            if not 0 <= val <= border:
                print(f"Значение должно быть в интервале (0, {border})")
                continue
        return val


def get_char(text: str, req_list: List) -> str:
    """
    Проверяет, что символ находится среди требуемых
    :param text:
    :param req_list: список требуемых символов
    :return:
    """
    while True:
        val = input(text)
        if val not in req_list:
            print(f"Значение должно быть из списка {req_list}")
            continue
        return val


def get_index_from_step(field: List[List], size: int) -> Tuple[int, int]:
    """
    Получает индексы ячейки в поле куда нужно ходить
    :param field: поле в виде списка списков
    :param size: параметр размера поля
    :return: индексы ячейки куда нужно ходить
    """
    while True:
        index_row = get_int_val("Введи индекс для строки\n", size - 1)
        index_col = get_int_val("Введи индекс для столбца\n", size - 1)
        if field[index_row][index_col] != " ":
            print("Ячейка занята")
            continue
        return index_row, index_col


def set_player_to_field(field: List[List], current_player: str, index_row: int, index_col: int) -> List[List]:
    """
    Помещает буквенное отображение игрока в выбранную в поле ячейку
    :param field: поле в виде списка списков
    :param current_player: обозначение текущего игрока
    :param index_row: индекс строки ячейки куда ходит текущий игрок
    :param index_col: индекс столбца ячейки куда ходит текущий игрок
    :return: обновленное поле в виде списка списков
    """
    field[index_row][index_col] = current_player
    return field


def change_player(player: str) -> str:
    """
    Передает ход следующему игроку
    :param player: игрок, совершивший ход
    :return: игрок, к которому перешел ход
    """
    new_player = "X" if player == "0" else "0"

    return new_player


def is_win(field: List[List], size: int, current_player: str) -> bool:
    """
    Проверяет поле на наличие выиграшной комбинации
    :param field: поле в виде списка списков
    :param size: параметр размера поля
    :param current_player: текущий игрок
    :return: True, если комбинация выигрышная и False, если нет
    """
    for i in range(size):
        for row in field:
            if all(ceil == current_player != ' ' for ceil in row):
                return True
        if all(row[i] == current_player != ' ' for row in field):
            return True
    if all(field[i][i] == current_player != ' ' for i in range(size)):
        return True
    if all(field[i][~i] == current_player != ' ' for i in range(size)):
        return True

    return False


def game(field: List[List], size: int, player: str) -> (str, None):
    # Функция запуска игры
    current_player = player  # игрок
    count_step = 0  # счетчик текущего хода
    draw_field(field)  # отрисовали поле
    while count_step < size*size:
        print(f"Ставит игрок {current_player}")
        index_row, index_col = get_index_from_step(field, size)  # получили координаты для хода
        field = set_player_to_field(field, current_player, index_row, index_col)  # поставили игрока на поле
        count_step += 1  # обновили счетчик ходов
        draw_field(field)  # отрисовали поле
        if is_win(field, size, current_player):  # Проверка выигрыша
            print(f"Выиграл игрок {current_player}")
            return current_player  # break
        current_player = change_player(current_player)  # смена игрока

    print("Ничья")
    return None


def app() -> None:
    """
    Запуск приложения
    :return: -
    """
    size = get_int_val("Введи размер поля\n")  # Определяем размер поля (можно с использованием input())
    empty_ceil = " "
    field = init_field(size, empty_ceil)
    player = get_char("Кто будет играть первым?\n", req_list=["X", "0"])
    # Определяем кто первым играет (можно с использованием input())
    who_player = get_char(f"C кем играем? {['h', 'c']}\n", req_list=['h', 'c'])
    # С кем играем (1, 2), ("human", "comp"), ("h", "c")
    if who_player == "h":
        game(field, size, player)
    else:
        print("В разработке")
        play_with_h = get_char(f"Хотите сыграть с человеком ? {['yes', 'no']}\n", req_list=['yes', 'no'])
        # Предлагает сыграть с человеком
        if play_with_h == "yes":
            game(field, size, player)
        else:
            print("В разработке")


if __name__ == "__main__":
    app()
