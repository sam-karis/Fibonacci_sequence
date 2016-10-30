def  Fibonacci_sequence(num):
	frst_fib = 0
	snd_fib = 1
	fib_lst = []
	if type(num) == str:
		return "not an integer"
	elif type(num) == list:
		return 'num is a list instead of integer'
	elif num == 0:
		return [0]
	for i in range(num):
		fib_lst.append(frst_fib)
		next_fib = frst_fib + snd_fib
		snd_fib = frst_fib
		frst_fib = next_fib
	return fib_lst


#print (Fibonacci_sequence(3))