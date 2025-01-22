'''
This module contains basic unit test for math operations.
Their porpoise is to show how to use pytest framework by example.
'''

#---------------------------------------------------
#Imports
#---------------------------------------------------

import pytest

#---------------------------------------------------
#A most basic test function
#---------------------------------------------------

def test_one_plus_one():
	assert 1+1 ==2
	

#---------------------------------------------------
#A most basic failing test function it was fixed after wards
#---------------------------------------------------

@pytest.mark.math
def test_one_plus_two():
	a=1
	b=2
	c=0
	assert a+b ==3 
	
	

#---------------------------------------------------
#A most basic exceptions function
#---------------------------------------------------

@pytest.mark.math
def test_num_divided_by_zero():
	with pytest.raises(ZeroDivisionError) as e:
		num=1/0
	assert 'division by zero' in str(e.value)


#---------------------------------------------------
#Multiplications by parametrizations
#---------------------------------------------------


products = [
	(2,3,6),
	(1,99,99),
	(0,99,0),
	(3,-4,-12),
	(-5,-5,25),
	(2.5,6.7,16.75)
]

@pytest.mark.math
@pytest.mark.parametrize ('a,b,product',products)
def  test_multiplication (a,b,product):
	assert a * b == product