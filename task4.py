# Решение 4.
from fractions import Fraction

def chislo(t):
    # t - части одного числа: ['5'], ['2/3'] или ['1', '3/5']
    if len(t) == 1 and t[0].isdigit():
        return Fraction(int(t[0]))
    if len(t) == 1:
        cel = 0
        drob = t[0]
    elif len(t) == 2 and t[0].isdigit():
        cel = int(t[0])
        drob = t[1]
    else:
        raise ValueError
    p = drob.split('/')
    if len(p) != 2 or not p[0].isdigit() or not p[1].isdigit():
        raise ValueError
    if int(p[1]) == 0:
        raise ZeroDivisionError
    return cel + Fraction(int(p[0]), int(p[1]))

while True:
    s = input('Выражение: ').replace('+', ' + ').replace('*', ' * ').split()
    if s.count('+') + s.count('*') != 1:
        print('Ошибка: нужна ровно одна операция + или *. Пример: 1 3/5 + 2/3')
        continue
    oper = '+' if '+' in s else '*'
    k = s.index(oper)
    try:
        f1 = chislo(s[:k])
        f2 = chislo(s[k + 1:])
        break
    except ValueError:
        print('Ошибка: числа пишутся так: 5, 2/3 или 1 3/5')
    except ZeroDivisionError:
        print('Ошибка: знаменатель не может быть 0')

if oper == '+':
    ans = f1 + f2
else:
    ans = f1 * f2

cel = ans.numerator // ans.denominator
ost = ans - cel
if cel != 0 and ost != 0:
    otvet = str(cel) + ' ' + str(ost)
elif cel != 0:
    otvet = str(cel)
else:
    otvet = str(ost)
print(' '.join(s), '->', otvet)
