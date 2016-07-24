#!/usr/bin/python
"""Cplus code example in python"""
class employee:
	'common base class'
	empCount = 0

	def __init__(self, name, sal):
		self.name = name
		self.sal = sal
		employee.empCount += 1
	
	def display(self):
		print "name = ", self.name, ",sal = ", self.sal, ",EmpCount = ", employee.empCount

print "doc = ",employee.__doc__
print "module = ",employee.__module__
print "name = ",employee.__name__
print "base = ",employee.__bases__ 
print "dict = ",employee.__dict__
emp1 = employee("Suzuka", 1000)
emp2 = employee("Novitha", 2000)
emp1.display()
emp2.display()
	
