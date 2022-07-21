import unittest

class TestClass(unittest.TestCase):

	def test_func1(self):
		a = 101
		b = 20
		self.assertNotEqual(a, b)
		
	def test_func2(self):
		a = [1, 2, 3]
		b = 3
		self.assertTrue(b in a)
		
	def test_func3(self):
		a = "hello"
		self.assertEqual(a, a.lower()) 
		
