import re
class Mathcalculator():

	"""Class to handle arithmetic operations in
	functions. Add, Multiply, Subtract and Divide"""
	regex = "^-?[0-9]\d*(\.\d+)?$"
	p = re.compile(regex)


	# Add function
	def add(self, a, b):
		"""Addition function"""
		if bool(re.match(self.p,str(a))) and (re.match(self.p,str(b))):
			return a +b
		else:
			print("Warning Non numbers or Infinite numbers")
			return False

	# Multiply function
	def multiply(self, a, b):
		"""Multiplication function"""
		if bool(re.match(self.p, str(a))) and (re.match(self.p, str(b))):
			return a * b
		else:
			print("Warning Non numbers or Infinite numbers")
			return False

	# Divide function
	def divide(self, a, b):
		"""Division function"""
		if bool(re.match(self.p, str(a))) and (re.match(self.p, str(b))):
			if b!=0:
				return a / b
			else:
				print("Cannot divide by Zero")
				return False
		else:
			print("Warning Non numbers or Infinite numbers")
			return False

	# Subtract function
	def subtract(self, a, b):
		"""Subtraction function"""
		if bool(re.match(self.p, str(a))) and (re.match(self.p, str(b))):
			return a - b
		else:
			print("Warning Non numbers or Infinite numbers")
			return False
