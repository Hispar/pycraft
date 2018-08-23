# import timeit
#
# t = timeit.Timer("test[5][5][5]",
#                  setup="test = [[['A' for x in range(512)] "
#                        "for y in range(512)] for z in range(64)]")
# print(t.timeit(number=100000))
# t2 = timeit.Timer("test2[(5, 5, 5)]",
#                   setup="test2 = {(x, y, z): 'A' for x in range(512) "
#                         "for y in range(512) for z in range(64)}")
# print(t2.timeit(number=100000))
from memory_profiler import memory_usage


def test1():
    test = [[['A' for x in range(512)] for y in range(512)] for z in range(64)]
    x = test[5][5][5]


def test2():
    test = {(x, y, z): 'A' for x in range(512) for y in range(512) for z in
            range(64)}
    x = test[(5, 5, 5)]


print(memory_usage(test1))
print(memory_usage(test2))
