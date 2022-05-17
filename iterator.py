nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]


class FlatIterator:
    def __init__(self, lst):
        self.start = -1
        self.lst = lst
        self.cursor = 0
        self.len_lst = len(lst)

    def __iter__(self):
        self.start += 1
        self.cursor = 0
        return self

    def __next__(self):
        while self.start - self.len_lst and self.cursor == len(self.lst[self.start]):
            iter(self)
        if self.start == self.len_lst:
            raise StopIteration
        self.cursor += 1
        return self.lst[self.start][self.cursor - 1]


if __name__ == '__main__':
    for item in FlatIterator(nested_list):
        print(item)
    flat_list = [item for item in FlatIterator(nested_list)]
    print(flat_list)
