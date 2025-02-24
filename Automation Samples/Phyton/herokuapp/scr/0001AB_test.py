'''
Test 0001 AB Test
'''

#---------------------------------------------------
# Imports
#---------------------------------------------------
import pytest
from playwright.sync_api import sync_playwright


@pytest.mark.smoke_test
@pytest.mark.happy_Path
@pytest.mark.partial_Happy
def test_load_page_ab():
    # Arrange
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

	# Act
        page.goto("https://the-internet.herokuapp.com/")
        assert page.inner_text("h1") == "Welcome to the-internet"
        
        # Find the "A/B Testing" link and click it
        test_name = page.locator('text=A/B Testing')
        test_name.click()
	# Assert
        # Check the h3 text for different conditions
        h3_text = page.inner_text("h3")
        assert h3_text in [
            "A/B Test Control",
            "A/B Test Variation 1",
            "A/B Test Variation 2",
        ], f"Unexpected heading: {h3_text}"

        print("The browser is about to close...")

        # Wait before closing the browser (if needed, consider replacing this)
        page.wait_for_timeout(300)  #debuging pause

        # Close the browser
        browser.close()
