'''
Test 0009 Dropdown
'''
#---------------------------------------------------
# Imports
#---------------------------------------------------
import pytest
from playwright.sync_api import sync_playwright

@pytest.mark.smoke_test
@pytest.mark.happy_Path
@pytest.mark.partial_Happy


def test_dropdown():
    # Arrange
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False,slow_mo=1500)
        
        page = browser.new_page()
        

        # Act
        page.goto("https://the-internet.herokuapp.com/")
        assert page.inner_text("h1") == "Welcome to the-internet"
        
        #pytest.set_trace()#debugging
        test_name = page.locator('text=Dropdown')
        test_name.click()

        #Assert

        # Check the h3 text for different conditions
        h3_text = page.inner_text("h3")
        assert h3_text == "Dropdown List"

        page.select_option('select#dropdown', label='Option 1')
        page.select_option('select#dropdown', label='Option 2')


        print("The browser is about to close...")
        page.wait_for_timeout(300)  # #debuging pause
        

        # Close the browser
        browser.close()
