'''
Test 001 Smoke Sanity Test
'''

#---------------------------------------------------
#Imports
#---------------------------------------------------
import pytest
from playwright.sync_api import sync_playwright


@pytest.mark.smoke_test
@pytest.mark.happy_Path
@pytest.mark.partial_Happy
def main():
#Arrange
        with sync_playwright() as p:
                browser = p.chromium.launch(headless=True)
                page=browser.new_page()
#act
                page.goto('http://localhost:4200/')

#Assert
				
                assert page.inner_text('h1') == 'Welcome to the robot dance-offs!'
                browser.close()

if __name__ == "__main__":
        main()
