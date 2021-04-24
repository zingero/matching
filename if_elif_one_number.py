import timeit


x = 42


def foo():
	if x == 42:
		pass


print(timeit.timeit(foo))  # 0.07581702899187803
