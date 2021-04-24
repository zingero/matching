class A:
	def __new__(cls, *args, **kwargs):
		print("new")
		return super(A, cls).__new__(cls)

	def __init__(self):
		print("init")


a = A()  # output: new\ninit


def foo():
	match a:
		case A():  # no output
			pass


foo()
