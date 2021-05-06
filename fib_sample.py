
def fib(n):	# フィボナッチ数列を書き出す関数
	"""print a Fibonacci series up to n."""
	a, b = 0, 1
	while a < n:
		print(a, end=' ')
		a, b  = b, a+b
	print()

n = int(input('数字を入力：'))

fib(n)
