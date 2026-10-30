s = "Иван ест, поет Оля, дома Борис, закупается Женя"
d = dict(sorted({(a if a[0].isupper() else b): (b if a[0].isupper() else a) for a, b in (p.split() for p in s.split(", "))}.items()))
print(d)
