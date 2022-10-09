# Создайте программу для игры в "Крестики-нолики".

matrix = [['*' for i in range(3)] for i in range(3)]

def print_matrix():
    for i in matrix:
        print(*i)
print_matrix()

step = 0
while step != 'stop':
    i = int(input('Введите номер строки: '))
    j = int(input('Введите номер столбца: '))
    step = input('Введите нужный знак (X или О) или введите stop для остановки игры: ')
    if step != 'stop':
        matrix[i-1][j-1] = step
    print_matrix()

