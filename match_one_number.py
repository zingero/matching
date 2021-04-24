import timeit


x = 42

def foo():
	match x:
		case 42:
			pass

print(timeit.timeit(foo))  # 0.0765328030101955


# for i in range(1000):
# 	print(f"\t\tcase {i}:\n\t\t\tpass")
