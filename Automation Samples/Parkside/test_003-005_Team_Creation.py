'''
Test 003-005 Start competition
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
                user_input = page.query_selector('[id="mat-input-0"]')
                user_input.type("Team000")

                page.click("button:text-is('Create a team ')")
                page.wait_for_timeout(100)
                user_input = page.query_selector('[id="mat-input-1"]')
                user_input.type("Team001")
                page.click("button:text-is('Create a team ')")

#Assert
                page.wait_for_timeout(200)
                assert page.inner_text('xpath=/html/body/app-root/div/app-competition/div/app-team[1]/h3') == 'Team000'
                assert page.inner_text('xpath=/html/body/app-root/div/app-competition/div/app-team[2]/h3') == 'Team001'
		#assert page.inner_text('h3') == 'Team000'
                #assert page.inner_text('h3') == 'Team001'
                #unable to make this work, will circle back for next try.
                browser.close()

if __name__ == "__main__":
        main()
