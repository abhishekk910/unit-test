import unittest

class TestClass(unittest.TestCase):

	def test_func1(self):
		a = 10
		b = 20
		self.assertNotEqual(a, b)
		
	def test_func2(self):
		a = [1, 2, 3]
		b = 3
		self.assertTrue(b in a)
		
		
