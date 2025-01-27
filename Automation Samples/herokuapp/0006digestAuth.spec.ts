import { test, expect } from '@playwright/test';
//Test configurations

//Imports, test for the test locations and executions.
//Imports, expect is for assertions.
//Other possible values:
//defineConfig, devices, ElementHandle, etc
test.use({httpCredentials : {username : 'admin', password : 'admin'}});
//Authentication place, for credentials. 

//High Level Test Strategy:
//Ensure that Saved credentials are sent different auth method [digest]
test('Digsest Authentification', async ({ page }) => {
  await page.goto('https://the-internet.herokuapp.com');


  // Click the Digest Authentication link.
  await page.getByRole('link', { name: 'Digest Authentication' }).click();
  
  await expect(page.getByRole('heading', { name: 'Digest Auth'})).toBeVisible();
  

  
  
});