import timeit

test = [[['A' for x in range(10)] for y in range(10)] for z in range(10)]
test2 = {(x, y, z): 'A' for x in range(10) for y in range(10) for z in
         range(10)}

# print(test)
# print(test[0][0][0])
# print(test2)
# print(test2[(0, 0, 0)])

t = timeit.Timer("test[0][0][0]",
              setup="test = [[['A' for x in range(10)] for y in range(10)] for z in range(10)]")
t.timeit()
# timeit.timeit(test2[(0, 0, 0)], number=10000)
