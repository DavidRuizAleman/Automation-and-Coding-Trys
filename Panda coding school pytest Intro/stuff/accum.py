'''
This module contains basic accumulator class
Their porpoise is to show how to use pytest framework class.
'''

#---------------------------------------------------
#class: accumulator
#---------------------------------------------------

class Accumulator:

	def __init__(self):
		self._count=0

	@property
	def count(self):
		return self._count

	def add(self,more=1):
		self._count += more