"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np

def smart_predict(number):
    """Предсказываем число
    
    Args:
        number (int): Загаданное число.
        
    Returns:
        int: Число попыток
    """
    count = 0
    predict_number = 50
    find_segment = 25  # Сегмент поиска определяет середину отрезка где необходимо искать число и с каждым шагом делится надвое
    
    while True:
        count += 1
        if number == predict_number:
            break
        # Если не угадали, сравниваем и сдигаемся на середину нового отрезка, где находится искомое число
        elif number < predict_number:
            predict_number -= find_segment
        else: 
            predict_number += find_segment
        #print(f"num {number}   pred {predict_number}    seg {find_segment}")
        # Делим сегмент на 2 с округлением в большую сторону
        find_segment = -1 * find_segment//2 * -1      
    return count


def score_game(predict_algo) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(predict_algo(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм предсказывает число в среднем за: {score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(smart_predict)
