# Решение 3.
while True:
    s = input('Строка: ')
    m = [p.split() for p in s.split(',') if p.strip()]
    ok = len(m) > 0
    for p in m:
        if len(p) != 2 or not p[0].isalpha() or not p[1].isalpha() or p[0][0].isupper() == p[1][0].isupper():
            print('Не понял кусок:', ' '.join(p))
            ok = False
    if ok:
        break
    print('Пиши через запятую пары из двух слов: Имя с заглавной, занятие со строчной. Пример: Иван ест, поет Оля')

print(dict(sorted({(a if a[0].isupper() else b): (b if a[0].isupper() else a) for a, b in m}.items())))
