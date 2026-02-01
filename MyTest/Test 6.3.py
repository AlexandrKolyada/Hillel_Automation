lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']

list2 = []

for el in lst1:
    if type(el) == str:
        list2.append(el)
print(list2)