'''
Test 0000 Smoke Sanity Test
'''

#---------------------------------------------------
# Imports
#---------------------------------------------------
import pytest
from playwright.sync_api import sync_playwright


@pytest.mark.smoke_test
@pytest.mark.happy_Path
@pytest.mark.partial_Happy
def test_hero_smoke():
#Arrange
        with sync_playwright() as p:
                browser = p.chromium.launch(headless=True)
                page=browser.new_page()
#act
                page.goto('https://the-internet.herokuapp.com')

#Assert
				
                assert page.inner_text('h1') == 'Welcome to the-internet'
                browser.close()
