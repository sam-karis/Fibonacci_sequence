import unittest

from  Fibonacci_sequence import  Fibonacci_sequence

class  FibonacciSequenceTest(unittest.TestCase):

	def test_non_integer(self):
		self.assertEqual('not an integer',Fibonacci_sequence('sam') )
	def test_list_num(self):
		self.assertEqual('num is a list instead of integer', Fibonacci_sequence([1,3,4]))

	def test_zero_num(self):
		self.assertEqual([0], Fibonacci_sequence(0))

	def test_two_num(self):
		self.assertEqual([0,1], Fibonacci_sequence(2))


if __name__ == '__main__':
  unittest.main()