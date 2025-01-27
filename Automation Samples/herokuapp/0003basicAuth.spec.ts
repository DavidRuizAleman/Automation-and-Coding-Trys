import { test, expect } from '@playwright/test';
//Test configurations

//Imports, test for the test locations and executions.
//Imports, expect is for assertions.
//Other possible values:
//defineConfig, devices, ElementHandle, etc

test.use({httpCredentials : {username : 'admin', password : 'admin'}});
//Place to place variables for the authentifications

//High Level Test Strategy:
//Save credentials and ensure that they are sent.   
test('basic Authentification', async ({ page }) => {
  await page.goto('https://the-internet.herokuapp.com');


  // Click the Basic Auth link.
  await page.getByRole('link', { name: 'Basic Auth' }).click();
  //ensure that the page loaded properly. 
  await expect(page.getByRole('heading', { name: 'Basic Auth'})).toBeVisible();
  
  //timeout for debugging
  await page.waitForTimeout(30);
});