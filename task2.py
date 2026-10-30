my_list = [7, 5, 3, 3, 2]
n = int(input("Новый элемент: "))
i = 0
while i < len(my_list) and my_list[i] >= n:
    i += 1
my_list.insert(i, n)
print(my_list)
