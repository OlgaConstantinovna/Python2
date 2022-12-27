# Задача 3. Даны две строки. Посчитайте сколько раз каждый символ первой строки встречается во второй
# «one» «onetwonine» - o – 2, n – 3, e – 2
def zadacha3():
    phrasa = 'one'
    text = 'onetwonine'
    count = 0
    res = {}
    for x in text:
        for y in phrasa:
            if x == y:
                count += 1
                if res.get(x):
                    res[x] += 1
                else:
                    res[x] = 1


    print(f'Каждый символ встречается {res} раз')

zadacha3()