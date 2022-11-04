def get_count_char(str_):
    dict_char = {}
    str_ = str_.lower()
    for char in str_:
        if char.isalpha():
            if char in dict_char.keys():
                dict_char[char] += 1
            else:
                dict_char[char] = 1
    return dict_char


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
