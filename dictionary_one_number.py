import timeit


d = {42: None}

x = 42


def foo():
	d[x]


print(timeit.timeit(foo))  # 0.08137985703069717
