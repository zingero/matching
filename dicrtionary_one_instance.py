import timeit
from dataclasses import dataclass


@dataclass()
class A:
	a: int
	b: int

	def __hash__(self):
		return self.a


d = {A(1, 1): None}

a = A(1, 1)


def foo():
	d[a]


print(timeit.timeit(foo))  # 0.38361275603529066
