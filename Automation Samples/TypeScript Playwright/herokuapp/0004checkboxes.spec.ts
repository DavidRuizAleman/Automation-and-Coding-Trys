import { test, expect } from '@playwright/test';
//Test configurations

//Imports, test for the test locations and executions.
//Imports, expect is for assertions.
//Other possible values:
//defineConfig, devices, ElementHandle, etc

//High Level Test Strategy:
//Click the checkboxes. [needs to be expanded to ensure that all are checked, but this is in the future. ]
test('checkboxes', async ({ page }) => {
  await page.goto('https://the-internet.herokuapp.com');

  // Click the Checkboxes link.
  await page.getByRole('link', { name: 'Checkboxes' }).click();

  // Expects page to have a heading with the name of Installation.
  
  await expect(page.getByRole('heading', { name: 'Checkboxes'})).toBeVisible();
  page.getByRole('checkbox').first().click();

  

});


