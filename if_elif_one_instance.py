import timeit
from dataclasses import dataclass


@dataclass()
class A:
	a: int
	b: int

	def __eq__(self, other):
		return self.a == other.a and self.b == other.b


a = A(1, 1)


def foo():
	if a == A(1, 1):
		pass


print(timeit.timeit(foo))  # 0.4610974980168976
