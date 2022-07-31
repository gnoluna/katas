from snail import snail


def test_n_3_square():
    array = [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]]
    assert snail(array) == [1, 2, 3, 6, 9, 8, 7, 4, 5]


def test_another_n_3_square():
    array = [[1, 2, 3],
             [8, 9, 4],
             [7, 6, 5]]
    assert snail(array) == [1, 2, 3, 4, 5, 6, 7, 8, 9]


def test_benchmark(benchmark):
    array = [[1, 2, 3],
             [8, 9, 4],
             [7, 6, 5]]
    benchmark(snail, array)
