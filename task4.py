# Задача 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Сдвиньте все элементы списка на 2 позиции вправо.
# 3 -> [2, 3, -3, -2, -1, 0, 1]

def zadacha4():
    array = [-3, -2, -1, 0, 1, 2, 3]
    count = 0
    for index, x in enumerate(array):
        if index == 2:
           print(array) 
           return
        array.insert(0, array[-1])
        del array[-1]

zadacha4()