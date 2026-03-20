class ReverseIterator:
    def __init__(self, my_list):
        self.my_list = my_list
        self.index = len(my_list) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < 0:
            raise StopIteration
        else:
            item = self.my_list[self.index]
            self.index -= 1
            return item

my_iter = ReverseIterator([1, 2, 3, 4])
for i in my_iter:
    print(i)