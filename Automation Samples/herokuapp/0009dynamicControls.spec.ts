import { test, expect } from '@playwright/test';
//Test configurations

//Imports, test for the test locations and executions.
//Imports, expect is for assertions.
//Other possible values:
//defineConfig, devices, ElementHandle, etc

//High Level Test Strategy:
//
test('Dynamic Controls', async ({ page }) => {
  await page.goto('https://the-internet.herokuapp.com');


  // Click the Disappearing Elements link.
  await page.getByRole('link', { name: 'Dynamic Controls' }).click();
  await expect(page.getByRole('heading', { name: 'Dynamic Controls'})).toBeVisible();
  await page.getByRole('checkbox').first().click();
  await page.getByRole('Button', { name: 'Remove' }).click();
  await expect(page.getByRole('checkbox')).toHaveCount(0);
  await expect(page.getByText('It\'s gone!')).toBeVisible();
  await page.getByRole('Button', { name: 'Add'}).click();
  await expect(page.getByText('It\'s back!')).toBeVisible();
  await page.getByRole('checkbox').first().click();
  await page.getByRole('Button', { name: 'Enable' }).click();
  await expect(page.getByText('It\'s enabled!')).toBeVisible();
  await expect(page.getByText('It\'s disabled!')).toBeVisible();
  await page.getByRole('textbox').fill('Peter');
  await page.getByRole('Button', { name: 'Disable' }).click();
  await expect(page.getByText('It\'s disabled!')).toBeVisible();
  
	
});