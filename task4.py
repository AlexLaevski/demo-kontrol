from fractions import Fraction

def chislo(t):
    p = t.split()
    if len(p) == 2:
        return int(p[0]) + Fraction(p[1])
    return Fraction(p[0])

e = input("Выражение: ")
if " + " in e:
    a, b = e.split(" + ")
    r = chislo(a) + chislo(b)
else:
    a, b = e.split(" * ")
    r = chislo(a) * chislo(b)
cel = r.numerator // r.denominator
ost = r - cel
if cel and ost:
    print(cel, ost)
elif cel:
    print(cel)
else:
    print(ost)
