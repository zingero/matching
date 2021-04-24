import timeit
from dataclasses import dataclass


@dataclass()
class A:
	a: int
	b: int


a = A(1, 1)


def foo():
	if a == A(1, 1):
		pass


print(timeit.timeit(foo))  # 0.5689109929953702
