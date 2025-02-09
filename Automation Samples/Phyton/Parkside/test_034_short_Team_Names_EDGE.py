'''
Test 034 Short Name on one team
'''

#---------------------------------------------------
#Imports
#---------------------------------------------------
import pytest
from playwright.sync_api import sync_playwright


@pytest.mark.edge_Case

def main():
#Arrange
        with sync_playwright() as p:
                browser = p.chromium.launch(headless=False)
                page=browser.new_page()
#act
                page.goto('http://localhost:4200/')
                #Start_competition = page.query_selector('Start a competition')
                #Start_competition.click()
                #page.click("button:is(:text(Start a competition))")
                page.click("button:text-is('Start a competition')")
                user_input = page.query_selector('[id="mat-input-0"]')
                user_input.type("123.")

                page.click("button:text-is('Create a team ')")
                page.wait_for_timeout(100)
                user_input = page.query_selector('[id="mat-input-1"]')
                user_input.type("Team001")
                page.click("button:text-is('Create a team ')")

#Assert

                #assert page.inner_text('xpath=/html/body/app-root/div/app-competition/div/app-team[1]/h3') == 'Bacon ipsum dolor amet capicola jerky porchetta salami, chislic sirloin shankle pig. Buffalo pork belly cupim andouille chislic pork chop bacon salami, tenderloin turducken. Prosciutto brisket burgdoggen chuck shank meatball buffalo pig pork chop chicken. Doner jowl kevin meatloaf shank. Pig picanha tail filet mignon pork chuck brisket pork loin corned beef frankfurter pork chop beef ribs biltong. Drumstick flank ham, buffalo turkey alcatra short loin spare ribs. Sausage pig ham hock buffalo, rump ribeye flank shank prosciutto bacon pork.'
                #assert page.inner_text('xpath=/html/body/app-root/div/app-competition/div/app-team[2]/h3') == 'Bacon ipsum dolor amet capicola jerky porchetta salami, chislic sirloin shankle pig. Buffalo pork belly cupim andouille chislic pork chop bacon salami, tenderloin turducken. Prosciutto brisket burgdoggen chuck shank meatball buffalo pig pork chop chicken. Doner jowl kevin meatloaf shank. Pig picanha tail filet mignon pork chuck brisket pork loin corned beef frankfurter pork chop beef ribs biltong. Drumstick flank ham, buffalo turkey alcatra short loin spare ribs. Sausage pig ham hock buffalo, rump ribeye flank shank prosciutto bacon pork.'

                browser.close()

if __name__ == "__main__":
        main()
