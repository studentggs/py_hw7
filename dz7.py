#Задача 1

def winnie_pooh(x):
    b = [sum((1 for k in i.replace('-', '') if k in 'прпрпрпр')) for i in x.split()]
    return 'Парам пам-пам' if all(map(lambda x: x == b[-1], b)) else 'Пам парам'


print(winnie_pooh('пара-ра-рам рам-пум-пупам па-ре-по-дам'))

#Задача 2

def print_operation_table(operation, rows=6, cols=6):
    matrix = [[0] * cols for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            matrix[i][j] = operation((i + 1), (j + 1))

    for i in matrix:
        print(*i)
    return ''

print(print_operation_table(lambda x, y: x * y))