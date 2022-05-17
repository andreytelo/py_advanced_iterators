nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    [1, 2, None],
]


def flat_generator(some_list):
    for item in some_list:
        for i in item:
            yield i


if __name__ == '__main__':
    for item in flat_generator(nested_list):
        print(item)
