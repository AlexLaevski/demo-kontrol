# Решение 2.
my_list = [7, 5, 3, 3, 2]

while True:
    s = input('Новый элемент: ').strip()
    try:
        n = int(s)
        break
    except ValueError:
        print('Ошибка: нужно целое число, например 4. Попробуй ещё раз')

i = 0
while i < len(my_list) and my_list[i] >= n:
    i += 1
my_list.insert(i, n)
print(my_list)
