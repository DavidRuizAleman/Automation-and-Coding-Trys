import { test, expect } from '@playwright/test';
//Test configurations

//Imports, test for the test locations and executions.
//Imports, expect is for assertions.
//Other possible values:
//defineConfig, devices, ElementHandle, etc

//High Level Test Strategy:
//
test('Drag and Drop', async ({ page }) => {
  await page.goto('https://the-internet.herokuapp.com');


  // Click the drag and drop link.
  await page.getByRole('link', { name: 'Drag and Drop' }).click();
  await expect(page.getByRole('heading', { name: 'Drag and Drop'})).toBeVisible();
  
  await page.locator('#column-a').dragTo(page.locator('#column-b'));
  
  
});