import { test, expect } from '@playwright/test';
//Test configurations

//Imports, test for the test locations and executions.
//Imports, expect is for assertions.
//Other possible values:
//defineConfig, devices, ElementHandle, etc

//High Level Test Strategy:
//
test('Entry Ad', async ({ page }) => {
  await page.goto('https://the-internet.herokuapp.com');


  // Click the Disappearing Elements link.
  await page.getByRole('link', { name: 'Entry Ad' }).click();
  await expect(page.locator('.modal')).toBeVisible();
  await page.on('dialog', dialog => dialog.accept());
  await page.getByText('Close', { exact: true }).click();
  await expect(page.getByRole('heading', { name: 'Entry Ad'})).toBeVisible();
  
  
  	

});