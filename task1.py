# Решение 1.
lst = [[1, 2], [3, 4, 4, 3, 1], [4, 1, 4, 5]]
for s in lst:
    if len(s) > 3:
        s[2] = s[2] + sum(s[3:])
        del s[3:]
print(lst)
