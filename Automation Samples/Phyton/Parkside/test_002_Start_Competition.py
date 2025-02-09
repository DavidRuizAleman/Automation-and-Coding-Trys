'''
Test 002 Start competition
'''

#---------------------------------------------------
#Imports
#---------------------------------------------------
import pytest
from playwright.sync_api import sync_playwright


@pytest.mark.happy_Path
@pytest.mark.Partial_Happy

def main():
#Arrange
        with sync_playwright() as p:
                browser = p.chromium.launch(headless=True)
                page=browser.new_page()
#act
                page.goto('http://localhost:4200/')
                #Start_competition = page.query_selector('Start a competition')
                #Start_competition.click()
                #page.click("button:is(:text(Start a competition))")
                page.click("button:text-is('Start a competition')")

#Assert
				
                assert page.inner_text('p') == 'First things first, let\'s create our robot teams!'
                browser.close()

if __name__ == "__main__":
        main()
