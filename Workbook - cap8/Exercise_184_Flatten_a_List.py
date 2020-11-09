def appiattire(x):
    if not x:
        return []

    if type(x[0]) == list:
        return flatten(x[0]) + flatten(x[1:])
    else:
        return [x[0]] + flatten(x[1:])


def main():
    print(flatten([1, [2, 3], [4, [5, [6, 7]]], [[[8], 9], [10]]]))

    print(flatten([1, [2, [3, [4, [5, [6, [7, [8, [9, [10]]]]]]]]]]))
    print(flatten([[[[[[[[[[1], 2], 3], 4], 5], 6], 7], 8], 9], 10]))
    print(flatten([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    print(flatten([]))


main()
