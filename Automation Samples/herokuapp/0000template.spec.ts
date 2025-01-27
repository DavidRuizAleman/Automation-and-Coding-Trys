import { test, expect } from '@playwright/test';
//Test configurations

//Imports, test for the test locations and executions.
//Imports, expect is for assertions.
//Other possible values:
//defineConfig, devices, ElementHandle, etc

//High Level Test Strategy:
//
test('test name, please replace', async ({ page }) => {
  await page.goto('https://the-internet.herokuapp.com');


  // Click the Disappearing Elements link.
  await page.getByRole('link', { name: 'Disappearing Elements' }).click();
  await expect(page.getByRole('heading', { name: 'Disappearing Elements'})).toBeVisible();
  
  	
	})
	
});