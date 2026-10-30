lst = [[1, 2], [3, 4, 4, 3, 1], [4, 1, 4, 5]]
for x in lst:
    if len(x) > 3:
        x[2] += sum(x[3:])
        del x[3:]
print(lst)
