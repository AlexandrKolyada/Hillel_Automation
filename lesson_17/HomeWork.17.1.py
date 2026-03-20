def my_generator(n: int):
    for i in range(n):
        if i % 2== 0:
            yield i

even_gen = my_generator(10)

for num in even_gen:
    print(num)