def find_interesting_numbers():
    interesting_numbers = []

    # Проверяем числа от 1729 и выше
    limit = 10000  # Ограничим поиск, чтобы ускорить программу

    # Вложенные циклы для нахождения чисел, которые можно выразить как сумму двух кубов
    for i in range(1, limit):
        for j in range(i + 1, limit):
            sum_of_cubes = i ** 3 + j ** 3
            # Ищем такие числа, которые уже встречались
            for k in range(1, i):
                for l in range(k + 1, j):
                    if sum_of_cubes == k ** 3 + l ** 3 and sum_of_cubes not in interesting_numbers:
                        interesting_numbers.append(sum_of_cubes)

    # Сортируем числа в порядке возрастания
    interesting_numbers.sort()

    return interesting_numbers[:5]  # Возвращаем первые 5 интересных чисел


# Выводим первые 5 интересных чисел
result = find_interesting_numbers()
for number in result:
    print(number)
