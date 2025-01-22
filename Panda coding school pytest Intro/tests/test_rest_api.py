'''
This module contains basic unit test for requests api
Their porpoise is to show how to use requests for api testing.
'''

#---------------------------------------------------
#Imports
#---------------------------------------------------


import requests
import pytest

@pytest.mark.duckduckgo
@pytest.mark.rest_api
def test_duckduckgo_instant_answer_api():
	
	#arrange
	url = 'https://api.duckduckgo.com/?q=Python&format=json'
	
	#act
	response = requests.get(url)
	body = response.json()
	print (body)
	
	#assert
	assert response.status_code == 200
	assert 'Python' in body['Heading']
	#had to change Heading from abstract text since AT was showing ''
	