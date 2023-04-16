'''
Задача 18: Требуется найти в массиве A самый близкий по величине элемент к заданному числу X.
Если таких элементов несколько, вы вывести один любой.
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
В последующих  строках записаны N целых чисел Ai (можно использовать псевдогенерацию). Последняя строка содержит число X

*Пример:*

5
    7 -2 3 5 1
    6
    -> 7

'''

from random import randint

def Generator_of_List(N):
    '''
    :param N: размер массива
    :return: список со случайными значениями от 0 до 9
    '''
    list1 = [randint(0,9) for _ in range(N)]
    print(list1)
    return list1

A = int(input("Введите размер массива: "))
X = int(input("Введите число: "))
list1 = Generator_of_List(A)

list2 = list(map(lambda x: x-X, list1)) # создаем список разности между элементом и заданным числом, при этом сохранена логика ндексов из списка List1
                                        # при необходимости можно найти все числа по индексу у которых разница 0 (или другое значение)

for i in range((max(list1)+1) // 2): # создаем цикл, и идем от 0 до максимума
                                     # так как присутствует модуль, введено //
    for j in list2:
        if i == abs(j):
            id1 = list2.index(j)
            print(f"   | ±{i} от числа {X} на позиции {id1} | количество {X}±{i}: {list1.count(list1[id1])}")
            break


