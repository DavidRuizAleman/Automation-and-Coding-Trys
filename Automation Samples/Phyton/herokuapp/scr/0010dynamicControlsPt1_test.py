'''
Test 0010 DynamicControls 1
'''
#---------------------------------------------------
# Imports
#---------------------------------------------------
import pytest
from playwright.sync_api import sync_playwright, expect

@pytest.mark.smoke_test
@pytest.mark.happy_Path
@pytest.mark.partial_Happy


def test_dynamic_controls_1():
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

        expect(page.get_by_role('checkbox')).to_have_count(1)
        page.locator('"Remove"').click()
        expect(page.get_by_role('checkbox')).to_have_count(0)

        page.locator('"Add"').click()
        expect(page.get_by_role('checkbox')).to_have_count(1)

        print("The browser is about to close...")
        page.wait_for_timeout(300)  # #debuging pause
        

        # Close the browser
        browser.close()
