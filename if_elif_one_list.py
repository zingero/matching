import timeit


x = [1, 2, 3]


def foo():
	if x == [1, 2, 3]:
		pass


print(timeit.timeit(foo))  # 0.1201232880121097
