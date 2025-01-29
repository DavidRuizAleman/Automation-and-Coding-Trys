import { test, expect } from '@playwright/test';
//Test configurations

//Imports, test for the test locations and executions.
//Imports, expect is for assertions.
//Other possible values:
//defineConfig, devices, ElementHandle, etc

//High Level Test Strategy:
//
test('Dynamic Loading 1', async ({ page }) => {
  await page.goto('https://the-internet.herokuapp.com');


  // Click the Disappearing Elements link.
  await page.getByRole('link', { name: 'Dynamic Loading' }).click();
  await expect(page.getByRole('heading', { name: 'Dynamically Loaded Page Elements'})).toBeVisible();
  await page.getByRole('link', { name: 'Example 1: Element on page that is hidden' }).click();
  await expect(page.getByRole('heading', { name: 'Dynamically Loaded Page Elements'})).toBeVisible();
  await expect(page.getByRole('heading', { name: 'Example 1: Element on page that is hidden'})).toBeVisible();
  await page.getByRole('Button', { name: 'Start' }).click();
  await expect(page.getByText('Loading...')).toBeVisible();
  await expect(page.getByRole('heading', { name: 'Hello World!'})).toBeVisible({ timeout: 6000});
});