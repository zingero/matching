import timeit


x = [1, 2, 3]


def foo():
	match x:
		case [1, 2, 3]:
			pass


print(timeit.timeit(foo))  # 0.1328382269712165
