import { test, expect } from '@playwright/test';
//Test configurations

//Imports, test for the test locations and executions.
//Imports, expect is for assertions.
//Other possible values:
//defineConfig, devices, ElementHandle, etc

//High Level test strategy:
//basic smoke test to check if main page is alive. 
test('its alive', async ({ page }) => {
  //Load the base page.
  await page.goto('https://the-internet.herokuapp.com');

  // Expect a title "to contain" a substring.
  await expect(page).toHaveTitle("The Internet");
});