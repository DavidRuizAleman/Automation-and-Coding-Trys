import pytest
from playwright.sync_api import sync_playwright

def main():
#Arrange
        with sync_playwright() as p:
                browser = p.chromium.launch(headless=True)
                page=browser.new_page()
#act
                page.goto('http://localhost:4200/')
                print (page.url)
                #print (page.url())



if __name__ == "__main__":
        main()
