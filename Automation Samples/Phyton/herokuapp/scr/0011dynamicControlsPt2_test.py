'''
Test 0011 DynamicControls 2
'''
#---------------------------------------------------
# Imports
#---------------------------------------------------
import pytest
from playwright.sync_api import sync_playwright, expect

@pytest.mark.smoke_test
@pytest.mark.happy_Path
@pytest.mark.partial_Happy


def test_dynamic_controls_2():
    # Arrange
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False,slow_mo=1500)
        
        page = browser.new_page()
        

        # Act
        page.goto("https://the-internet.herokuapp.com/")
        assert page.inner_text("h1") == "Welcome to the-internet"
        
        #pytest.set_trace()#debugging
        test_name = page.locator('text=Dynamic Controls')
        test_name.click()

        #Assert

        # Check the h3 text for different conditions
        h4_text = page.inner_text("h4")
        assert h4_text == "Dynamic Controls"
        textbox = page.get_by_role("textbox")

        #expect(textbox.is_disabled())
        page.locator('"Enable"').click()
        #expect(textbox.is_enabled())
        textbox.fill("Test Passed")
        page.locator('"Disable"').click()
        #expect(textbox.is_disabled())


        
        #disable_textbox_button = page.locator('"Disable"').click()
        #"Wait for it"
        #It's disabled!
        #enable_textbox_button = page.locator('"Enable"')
        #enable_textbox_button.click()
        #It's enabled!
        #"Wait for it"





        print("The browser is about to close...")
        page.wait_for_timeout(300)  # #debuging pause
        

        # Close the browser
        browser.close()
