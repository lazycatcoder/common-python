'''
The Fibonacci sequence is a sequence of numbers, in which each element is equal to the sum of the previous two.

A super-Fibonacci sequence of order m will be considered a sequence of numbers in which each element is equal to 
the sum of m previous ones. We consider the first m elements (with serial numbers from 1 to m) as units.
'''

a = int(input()) #index
b = int(input()) #time

def s_fibonacci(n, m):
	l = []
	while m != 0:
		l.append(1)
		m -= 1
	f_list = len(l)-1
	while len(l) < n:
		l.append(sum(l[-1-f_list:]))
	return (l[-1])

print (s_fibonacci(a, b))