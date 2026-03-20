class EvenNumbers:
    def __init__(self, max_num):
        self.max_num = max_num
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.max_num:
            raise StopIteration
        else:
            item = self.current
            self.current += 2
            return item

ev_num = EvenNumbers(10)
for i in ev_num:
    print(i)