'''
Test 0003 Basic Auth
'''
#---------------------------------------------------
# Imports
#---------------------------------------------------
import pytest
from playwright.sync_api import sync_playwright

@pytest.mark.smoke_test
@pytest.mark.happy_Path
@pytest.mark.partial_Happy


def test_add_remove_elements():
    # Arrange
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False,slow_mo=1500)
        context = browser.new_context(
            http_credentials={'username':'admin', 'password':'admin'}
        )
        
        page = context.new_page()
        

        # Act
        page.goto("https://the-internet.herokuapp.com/")
        assert page.inner_text("h1") == "Welcome to the-internet"
        
        #pytest.set_trace()#debugging
        # Find the "A/B Testing" link and click it
        test_name = page.locator('text=Basic Auth')
        test_name.click()

        #Assert

        # Check the h3 text for different conditions
        h3_text = page.inner_text("h3")
        assert h3_text == "Basic Auth"
       
        
        print("The browser is about to close...")

        # Wait before closing the browser (if needed, consider replacing this)
        page.wait_for_timeout(300)  # Replace sleep(300) with Playwright's built-in waiting mechanism
        context.close()

        # Close the browser
        browser.close()

##--
