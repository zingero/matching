import timeit
from dataclasses import dataclass


@dataclass()
class A:
	a: int
	b: int

	def __eq__(self, other):
		return self.a == other.a and self.b == other.b

	def __hash__(self):
		return self.a


d = {A(1, 1): None}

a = A(1, 1)


def foo():
	d[a]


print(timeit.timeit(foo))  # 0.26946467300876975
