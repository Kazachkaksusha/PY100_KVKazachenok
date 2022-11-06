import random


def get_unique_list_numbers() -> list[int]:
    list_numbers = [i for i in range(-10, 11)]
    return random.sample(list_numbers, 15)


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
