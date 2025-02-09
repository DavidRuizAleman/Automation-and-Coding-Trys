'''
Test 030 LeaderBoards Direct
'''

#---------------------------------------------------
#Imports
#---------------------------------------------------
import pytest
from playwright.sync_api import sync_playwright


@pytest.mark.edge_Case
@pytest.mark.full_Happy

def main():
#Arrange
        with sync_playwright() as p:
                browser = p.chromium.launch(headless=True)
                page=browser.new_page()
#act
                page.goto('http://localhost:4200/Leaderboards')
                #Assert
                assert page.url == 'http://localhost:4200/'
                browser.close()

if __name__ == "__main__":
        main()
