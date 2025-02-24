'''
Test 0002 Add Remove Elemnents Test
'''
#---------------------------------------------------
# Imports
#---------------------------------------------------
import pytest
from playwright.sync_api import sync_playwright
import random

@pytest.mark.smoke_test
@pytest.mark.happy_Path
@pytest.mark.partial_Happy

def test_add_remove_elements():
    # Arrange
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Act
        page.goto("https://the-internet.herokuapp.com/")
        assert page.inner_text("h1") == "Welcome to the-internet"
        
        #pytest.set_trace()#debugging
        # Find the "A/B Testing" link and click it
        test_name = page.locator('text=Add/Remove Elements')
        test_name.click()
		
	#assert

        # Check the h3 text for different conditions
        h3_text = page.inner_text("h3")
        assert h3_text == "Add/Remove Elements"
        num = 0
        num = int(num)
        num = random.random() * 20
        print(str(num) + " elements will be added")
        add_item_button = page.locator('"Add Element"')

        for i in range(0, int(num)):
           add_item_button.click()
           i+=1
        for i in range(0, int(num)):
          delete_button = page.locator('"Delete"').first
          delete_button.click()
          i+=1
        
        
        print("The browser is about to close...")

        
        page.wait_for_timeout(300)  #debuging pause

        # Close the browser
        browser.close()