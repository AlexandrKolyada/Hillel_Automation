def fibonachi_generator(n: int):
    a, b = 0, 1
    while a <= n:
        yield a
        a, b = b, b + a

fibon = fibonachi_generator(10)
for num in fibon:
    print(num)